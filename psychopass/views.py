from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from community.models import Community
from psychopass.models import UserPsychoPass, UserPsychoPassSerializer, CommunityPsychoPass, CommunityPsychoPassSerializer
# Create your views here.


@api_view(["POST"])
@permission_classes([IsAdminUser])
def ingest_message(request: Request) -> Response:
    psycho_pass, _ = UserPsychoPass.objects.get_or_create(
        platform=request.user, user_id=request.data.get("userID"))
    community = Community.objects.get(
        platform=request.user, community_id=request.data.get("communityID"))
    community_psycho_pass = CommunityPsychoPass.objects.get(
        community=community)

    psycho_pass.ingest_message(request.data.get("attributeScores"))
    psycho_pass.save()
    community_psycho_pass.users.add(psycho_pass)
    community_psycho_pass.save()

    return Response({
        "user": serialize_user(psycho_pass),
        "community": serialize_community(community_psycho_pass)
    }, status=status.HTTP_202_ACCEPTED)


class UserPsychoPassView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request: Request) -> Response:
        psycho_pass = UserPsychoPass.objects.get(
            user_id=request.query_params.get("id"))

        return Response(serialize_user(psycho_pass), status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        psycho_pass = UserPsychoPass.objects.create(
            platform=request.user, user_id=request.data.get("userID"))
        psycho_pass.save()

        return Response(serialize_user(psycho_pass), status=status.HTTP_201_CREATED)

    def delete(self, request: Request) -> Response:
        psycho_pass = UserPsychoPass.objects.get(
            user_id=request.query_params.get("id"))
        psycho_pass.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class CommunityPsychoPassView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request: Request) -> Response:
        community = Community.objects.get(
            platform=request.user, community_id=request.query_params.get("id"))
        community_psycho_pass = CommunityPsychoPass.objects.get(
            community=community)

        return Response(serialize_community(community_psycho_pass), status=status.HTTP_200_OK)

    def put(self, request: Request) -> Response:
        community = Community.objects.get(
            platform=request.user, community_id=request.data.get("communityID"))
        community_psycho_pass = CommunityPsychoPass.objects.get(
            community=community)
        psycho_pass = UserPsychoPass.objects.get(
            user_id=request.data.get("userID"))
        community_psycho_pass.users.remove(psycho_pass)
        community_psycho_pass.save()

        return Response(serialize_community(community_psycho_pass), status=status.HTTP_204_NO_CONTENT)


def serialize_user(psycho_pass: UserPsychoPass) -> dict:
    data = UserPsychoPassSerializer(psycho_pass).data
    data["crime_coefficient"] = psycho_pass.crime_coefficient()
    data["hue"] = psycho_pass.hue()
    return data


def serialize_community(community_psycho_pass: CommunityPsychoPass) -> dict:
    data = CommunityPsychoPassSerializer(community_psycho_pass).data
    data["area_stress_level"] = community_psycho_pass.area_stress_level()
    return data
