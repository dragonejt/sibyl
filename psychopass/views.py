from http import HTTPStatus

from django.shortcuts import get_object_or_404
from drf_spectacular.utils import (
    OpenApiParameter,
    OpenApiResponse,
    extend_schema,
    inline_serializer,
)
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.fields import CharField
from rest_framework.permissions import IsAdminUser
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from sentry_sdk import set_user

from community.models import Community
from psychopass.models import (
    CommunityPsychoPass,
    CommunityPsychoPassSerializer,
    UserPsychoPass,
    UserPsychoPassSerializer,
)

# Create your views here.


@api_view(["POST"])
@permission_classes([IsAdminUser])
def ingest_message(request: Request) -> Response:
    set_user(
        {
            "id": request.data.get("user_id"),
            "username": f"{request.user.username}/{request.data.get('user_id')}",
        }
    )
    psycho_pass, _ = UserPsychoPass.objects.get_or_create(
        platform=request.user, user_id=request.data.get("user_id")
    )
    community = get_object_or_404(
        Community, platform=request.user, community_id=request.data.get("community_id")
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

    @extend_schema(
        operation_id="read user psycho pass",
        parameters=[
            OpenApiParameter(
                "id",
                str,
                required=True,
                description="retrieves the user psycho pass with this id",
            )
        ],
        responses={
            "200": UserPsychoPassSerializer,
            "400": OpenApiResponse(description="Missing field in query params or body"),
            "404": OpenApiResponse(description="Item not found with provided details"),
            "500": OpenApiResponse(description=HTTPStatus.INTERNAL_SERVER_ERROR.description),
        },
    )
    def get(self, request: Request) -> Response:
        set_user(
            {
                "id": request.query_params.get("id"),
                "username": f"{request.user.username}/{request.query_params.get('id')}",
            }
        )
        psycho_pass = get_object_or_404(UserPsychoPass, user_id=request.query_params.get("id"))

        return Response(UserPsychoPassSerializer(psycho_pass).data, status=status.HTTP_200_OK)

    @extend_schema(
        operation_id="create user psycho pass",
        request=inline_serializer(
            "create_community_serializer",
            {
                "user_id": CharField(max_length=20),
            },
        ),
        responses={
            "200": UserPsychoPassSerializer,
            "400": OpenApiResponse(description="Missing field in query params or body"),
            "404": OpenApiResponse(description="Item not found with provided details"),
            "500": OpenApiResponse(description=HTTPStatus.INTERNAL_SERVER_ERROR.description),
        },
    )
    def post(self, request: Request) -> Response:
        set_user(
            {
                "id": request.data.get("user_id"),
                "username": f"{request.user.username}/{request.data.get('user_id')}",
            }
        )
        psycho_pass = UserPsychoPass.objects.create(
            platform=request.user, user_id=request.data.get("user_id")
        )
        psycho_pass.save()

        return Response(UserPsychoPassSerializer(psycho_pass).data, status=status.HTTP_201_CREATED)

    @extend_schema(
        operation_id="delete user psycho pass",
        parameters=[
            OpenApiParameter(
                "id",
                str,
                required=True,
                description="deletes the user psycho pass with this id",
            )
        ],
        responses={
            "204": OpenApiResponse(description=HTTPStatus.NO_CONTENT.description),
            "400": OpenApiResponse(description="Missing field in query params or body"),
            "404": OpenApiResponse(description="Item not found with provided details"),
            "500": OpenApiResponse(description=HTTPStatus.INTERNAL_SERVER_ERROR.description),
        },
    )
    def delete(self, request: Request) -> Response:
        set_user(
            {
                "id": request.query_params.get("id"),
                "username": f"{request.user.username}/{request.query_params.get('id')}",
            }
        )
        psycho_pass = get_object_or_404(UserPsychoPass, user_id=request.query_params.get("id"))
        psycho_pass.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class CommunityPsychoPassView(APIView):
    permission_classes = [IsAdminUser]

    @extend_schema(
        operation_id="read community psycho pass",
        parameters=[
            OpenApiParameter(
                "id",
                str,
                required=True,
                description="retrieves the community psycho pass with this id",
            )
        ],
        responses={
            "200": CommunityPsychoPassSerializer,
            "400": OpenApiResponse(description="Missing field in query params or body"),
            "404": OpenApiResponse(description="Item not found with provided details"),
            "500": OpenApiResponse(description=HTTPStatus.INTERNAL_SERVER_ERROR.description),
        },
    )
    def get(self, request: Request) -> Response:
        community = get_object_or_404(
            Community,
            platform=request.user,
            community_id=request.query_params.get("id"),
        )
        community_psycho_pass = get_object_or_404(CommunityPsychoPass, community=community)

        return Response(
            CommunityPsychoPassSerializer(community_psycho_pass).data,
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        operation_id="remove user from community",
        request=inline_serializer(
            "remove_user_serializer",
            {
                "user_id": CharField(max_length=20),
                "community_id": CharField(max_length=20),
            },
        ),
        responses={
            "200": CommunityPsychoPassSerializer,
            "400": OpenApiResponse(description="Missing field in query params or body"),
            "404": OpenApiResponse(description="Item not found with provided details"),
            "500": OpenApiResponse(description=HTTPStatus.INTERNAL_SERVER_ERROR.description),
        },
    )
    def patch(self, request: Request) -> Response:
        community = get_object_or_404(
            Community,
            platform=request.user,
            community_id=request.data.get("community_id"),
        )
        community_psycho_pass = get_object_or_404(CommunityPsychoPass, community=community)
        psycho_pass = get_object_or_404(UserPsychoPass, user_id=request.data.get("user_id"))
        community_psycho_pass.users.remove(psycho_pass)
        community_psycho_pass.save()

        return Response(
            CommunityPsychoPassSerializer(community_psycho_pass).data,
            status=status.HTTP_202_ACCEPTED,
        )
