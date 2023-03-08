from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from psychopass.models import UserPsychoPass, UserPsychoPassSerializer, CommunityPsychoPass, CommunityPsychoPassSerializer
from dominator.models import Dominator
# Create your views here.


@api_view(["POST"])
@permission_classes([IsAdminUser])
def ingest_message(request: Request) -> Response:
    user_profile, _ = UserPsychoPass.objects.get_or_create(
        platform=request.user.username, platform_id=request.data.get("userID"))
    community_profile, _ = CommunityPsychoPass.objects.get_or_create(
        platform=request.user.username, platform_id=request.data.get("communityID"))

    user_profile.ingest_message(request.data.get("attributeScores"))
    user_profile.save()
    community_profile.users.add(user_profile)
    community_profile.save()
    return Response({
        "user": serialize_user(user_profile),
        "community": serialize_community(community_profile)
    }, status=status.HTTP_202_ACCEPTED)


class UserPsychoPassView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request: Request) -> Response:
        user_profile = UserPsychoPass.objects.get(
            platform_id=request.query_params.get("id"))
        if user_profile is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serialize_user(user_profile), status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        user_profile = UserPsychoPass.objects.create(
            platform=request.user.username, platform_id=request.data.get("userID"))
        user_profile.save()
        return Response(serialize_user(user_profile), status=status.HTTP_201_CREATED)

    def delete(self, request: Request) -> Response:
        user_profile = UserPsychoPass.objects.get(
            platform_id=request.query_params.get("ID"))
        user_profile.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class CommunityPsychoPassView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request: Request) -> Response:
        community_profile = CommunityPsychoPass.objects.get(
            platform_id=request.query_params.get("id"))
        if community_profile is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serialize_community(community_profile), status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        community_profile = CommunityPsychoPass.objects.create(
            platform=request.user.username, platform_id=request.data.get("communityID"))
        community_profile.save()
        dominator = Dominator.objects.create(profile=community_profile)
        dominator.save()
        return Response(serialize_community(community_profile), status=status.HTTP_201_CREATED)

    def delete(self, request: Request) -> Response:
        community_profile = CommunityPsychoPass.objects.get(
            platform_id=request.query_params.get("id"))
        community_profile.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


def serialize_user(user_profile: UserPsychoPass) -> dict:
    data = UserPsychoPassSerializer(user_profile).data
    data["crime_coefficient"] = user_profile.crime_coefficient()
    data["hue"] = user_profile.hue()
    return data


def serialize_community(community_profile: CommunityPsychoPass) -> dict:
    data = CommunityPsychoPassSerializer(community_profile).data
    data["area_stress_level"] = community_profile.area_stress_level()
    return data
