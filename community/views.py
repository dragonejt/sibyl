from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.request import Request
from rest_framework.response import Response
from community.models import Community, CommunitySerializer
from psychopass.models import CommunityPsychoPass
from dominator.models import MessageDominator, MemberDominator

# Create your views here.


class CommunityView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request: Request) -> Response:
        community = Community.objects.get(
            platform=request.user, community_id=request.query_params.get("id"))

        return Response(CommunitySerializer(community).data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        community = Community.objects.create(
            platform=request.user, community_id=request.data.get("communityID"))
        community.save()
        community_psycho_pass = CommunityPsychoPass.objects.create(
            community=community)
        community_psycho_pass.save()
        member_dominator = MemberDominator.objects.create(community=community)
        member_dominator.save()
        message_dominator = MessageDominator.objects.create(
            community=community)
        message_dominator.save()

        return Response(CommunitySerializer(community).data, status=status.HTTP_201_CREATED)

    def put(self, request: Request) -> Response:
        community = Community.objects.get(
            community_id=request.data.get("communityID"))
        community_data = request.data.copy()
        community_data["platform"] = community.platform.id
        community_data["community_id"] = request.data.get("communityID")
        serializer = CommunitySerializer(community, data=community_data)
        serializer.is_valid(raise_exception=True)
        community = serializer.save()

        return Response(CommunitySerializer(community).data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request: Request) -> Response:
        community = Community.objects.get(
            platform=request.user, community_id=request.query_params.get("id"))
        community.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
