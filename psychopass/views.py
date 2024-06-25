from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from sentry_sdk import set_user
from community.models import Community
from psychopass.models import (
    UserPsychoPass,
    UserPsychoPassSerializer,
    CommunityPsychoPass,
    CommunityPsychoPassSerializer,
)

# Create your views here.


@api_view(["POST"])
@permission_classes([IsAdminUser])
def ingest_message(request: Request) -> Response:
    set_user(
        {
            "id": request.data.get("userID"),
            "username": f"{request.user.username}/{request.data.get("userID")}",
        }
    )
    psycho_pass, _ = UserPsychoPass.objects.get_or_create(
        platform=request.user, user_id=request.data.get("userID")
    )
    community = get_object_or_404(
        Community, platform=request.user, community_id=request.data.get("communityID")
    )
    community_psycho_pass = get_object_or_404(CommunityPsychoPass, community=community)

    attribute_scores = request.data["attributeScores"]
    psycho_pass.toxicity = psycho_pass.update_score(
        attribute_scores["TOXICITY"], psycho_pass.toxicity, psycho_pass.messages
    )
    psycho_pass.severe_toxicity = psycho_pass.update_score(
        attribute_scores["SEVERE_TOXICITY"],
        psycho_pass.severe_toxicity,
        psycho_pass.messages,
    )
    psycho_pass.identity_attack = psycho_pass.update_score(
        attribute_scores["IDENTITY_ATTACK"],
        psycho_pass.identity_attack,
        psycho_pass.messages,
    )
    psycho_pass.insult = psycho_pass.update_score(
        attribute_scores["INSULT"], psycho_pass.insult, psycho_pass.messages
    )
    psycho_pass.threat = psycho_pass.update_score(
        attribute_scores["THREAT"], psycho_pass.threat, psycho_pass.messages
    )
    psycho_pass.profanity = psycho_pass.update_score(
        attribute_scores["PROFANITY"], psycho_pass.profanity, psycho_pass.messages
    )
    psycho_pass.sexually_explicit = psycho_pass.update_score(
        attribute_scores["SEXUALLY_EXPLICIT"],
        psycho_pass.sexually_explicit,
        psycho_pass.messages,
    )
    psycho_pass.messages = max(0, min(500, psycho_pass.messages + 1))

    psycho_pass.save()
    community_psycho_pass.users.add(psycho_pass)
    community_psycho_pass.save()

    return Response(
        {
            "user": UserPsychoPassSerializer(psycho_pass).data,
            "community": CommunityPsychoPassSerializer(community_psycho_pass).data,
        },
        status=status.HTTP_202_ACCEPTED,
    )


class UserPsychoPassView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request: Request) -> Response:
        set_user(
            {
                "id": request.query_params.get("id"),
                "username": f"{request.user.username}/{request.query_params.get("id")}",
            }
        )
        psycho_pass = get_object_or_404(
            UserPsychoPass, user_id=request.query_params.get("id")
        )

        return Response(
            UserPsychoPassSerializer(psycho_pass).data, status=status.HTTP_200_OK
        )

    def head(self, request: Request) -> Response:
        set_user(
            {
                "id": request.query_params.get("id"),
                "username": f"{request.user.username}/{request.query_params.get("id")}",
            }
        )
        psycho_pass = get_object_or_404(
            UserPsychoPass, user_id=request.query_params.get("id")
        )
        if request.user == psycho_pass.platform:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_403_FORBIDDEN)

    def post(self, request: Request) -> Response:
        set_user(
            {
                "id": request.data.get("userID"),
                "username": f"{request.user.username}/{request.data.get("userID")}",
            }
        )
        psycho_pass = UserPsychoPass.objects.create(
            platform=request.user, user_id=request.data.get("userID")
        )
        psycho_pass.save()

        return Response(
            UserPsychoPassSerializer(psycho_pass).data, status=status.HTTP_201_CREATED
        )

    def delete(self, request: Request) -> Response:
        set_user(
            {
                "id": request.query_params.get("id"),
                "username": f"{request.user.username}/{request.query_params.get("id")}",
            }
        )
        psycho_pass = get_object_or_404(
            UserPsychoPass, user_id=request.query_params.get("id")
        )
        psycho_pass.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class CommunityPsychoPassView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request: Request) -> Response:
        community = get_object_or_404(
            Community,
            platform=request.user,
            community_id=request.query_params.get("id"),
        )
        community_psycho_pass = get_object_or_404(
            CommunityPsychoPass, community=community
        )

        return Response(
            CommunityPsychoPassSerializer(community_psycho_pass).data,
            status=status.HTTP_200_OK,
        )

    def put(self, request: Request) -> Response:
        community = get_object_or_404(
            Community,
            platform=request.user,
            community_id=request.data.get("communityID"),
        )
        community_psycho_pass = get_object_or_404(
            CommunityPsychoPass, community=community
        )
        psycho_pass = get_object_or_404(
            UserPsychoPass, user_id=request.data.get("userID")
        )
        community_psycho_pass.users.remove(psycho_pass)
        community_psycho_pass.save()

        return Response(
            CommunityPsychoPassSerializer(community_psycho_pass).data,
            status=status.HTTP_202_ACCEPTED,
        )
