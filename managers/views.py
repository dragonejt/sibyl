from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from profiles.models import CommunityProfile
from managers.models import MessageManager, MessageManagerSerializer, MemberManager, MemberManagerSerializer

# Create your views here.


class MessageManagerView(APIView):

    def get(self, request: Request) -> Response:
        community_profile = CommunityProfile.objects.get(
            platform_id=request.query_params.get("id"))
        message_manager = MessageManager.objects.get(profile=community_profile)

        return Response(MessageManagerSerializer(message_manager).data, status=status.HTTP_200_OK)

    def put(self, request: Request) -> Response:
        community_profile = CommunityProfile.objects.get(
            platform_id=request.data.get("communityID"))
        message_manager = MessageManager.objects.get(
            profile=community_profile)
        serializer = MessageManagerSerializer(
            message_manager, data=request.data.get("triggers"))
        serializer.is_valid(raise_exception=True)
        message_manager = serializer.save()

        return Response(MessageManagerSerializer(message_manager).data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request: Request) -> Response:
        community_profile = CommunityProfile.objects.get(
            platform_id=request.query_params.get("id"))
        message_manager = MessageManager.objects.get(profile=community_profile)
        message_manager.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class MemberManagerView(APIView):

    def get(self, request: Request) -> Response:
        community_profile = CommunityProfile.objects.get(
            platform_id=request.query_params.get("id"))
        member_manager = MemberManager.objects.get(profile=community_profile)

        return Response(MemberManagerSerializer(member_manager).data, status=status.HTTP_200_OK)

    def put(self, request: Request) -> Response:
        community_profile = CommunityProfile.objects.get(
            platform_id=request.data.get("communityID"))
        member_manager = MemberManager.objects.get(
            profile=community_profile)
        serializer = MemberManagerSerializer(
            member_manager, data=request.data.get("triggers"))
        serializer.is_valid(raise_exception=True)
        member_manager = serializer.save()

        return Response(MemberManagerSerializer(member_manager).data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request: Request) -> Response:
        community_profile = CommunityProfile.objects.get(
            platform_id=request.query_params.get("id"))
        member_manager = MemberManager.objects.get(profile=community_profile)
        member_manager.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
