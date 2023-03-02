from datetime import datetime
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from profiles.models import UserProfile, UserProfileSerializer, CommunityProfile, CommunityProfileSerializer
from clients.discord import get_server_info
# Create your views here.


@api_view(["POST"])
@permission_classes([IsAdminUser])
def ingest_message(request: Request) -> Response:
    user_profile = UserProfile.objects.get(
        platform_id=request.data.get("userID"))
    community_profile = CommunityProfile.objects.get(
        platform_id=request.data.get("communityID"))
    if user_profile is None:
        user_profile = UserProfile.objects.create(
            platform=request.user.name, platform_id=request.data.get("userID"), last_flag=datetime.utcnow())
    if community_profile is None:
        num_users = get_server_info(request.data.get(
            "communityID")).get("approximate_member_count")
        community_profile = CommunityProfile.objects.create(platform=request.user.name, platform_id=request.data.get(
            "userID"), last_flag=datetime.utcnow(), users=num_users)

    user_profile.ingest_message(request.data.get("attributeScores"))
    user_profile.save()
    community_profile.ingest_message(request.data.get("attributeScores"))
    community_profile.save()
    return Response(status=status.HTTP_200_OK)


class UserProfiles(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request: Request) -> Response:
        user_profile = UserProfile.objects.get(platform_id=request.query_params.get("ID"))
        if user_profile is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        data = UserProfileSerializer(user_profile).data
        data["crime_coefficient"] = user_profile.crime_coefficient()
        data["hue"] = user_profile.hue()
        return Response(data, status=status.HTTP_200_OK)
