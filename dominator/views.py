from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from psychopass.models import CommunityPsychoPass
from dominator.models import MemberDominator, MemberDominatorSerializer, MessageDominator, MessageDominatorSerializer

# Create your views here.


class MemberDominatorView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request: Request) -> Response:
        community_psycho_pass = CommunityPsychoPass.objects.get(
            platform_id=request.query_params.get("id"))
        dominator = MemberDominator.objects.get(
            psycho_pass=community_psycho_pass)

        return Response(MemberDominatorSerializer(dominator).data, status=status.HTTP_200_OK)

    def put(self, request: Request) -> Response:
        community_psycho_pass = CommunityPsychoPass.objects.get(
            platform_id=request.data.get("communityID"))
        dominator = MemberDominator.objects.get(
            psycho_pass=community_psycho_pass)
        trigger_data = request.data.copy()
        trigger_data.pop("communityID")
        trigger_data["psycho_pass"] = community_psycho_pass.id
        serializer = MemberDominatorSerializer(
            dominator, data=trigger_data)
        serializer.is_valid(raise_exception=True)
        dominator = serializer.save()

        return Response(MemberDominatorSerializer(dominator).data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request: Request) -> Response:
        community_psycho_pass = CommunityPsychoPass.objects.get(
            platform_id=request.query_params.get("id"))
        dominator = MemberDominator.objects.get(
            psycho_pass=community_psycho_pass)
        dominator.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class MessageDominatorView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request: Request) -> Response:
        community_psycho_pass = CommunityPsychoPass.objects.get(
            platform_id=request.query_params.get("id"))
        dominator = MessageDominator.objects.get(
            psycho_pass=community_psycho_pass)

        return Response(MessageDominatorSerializer(dominator).data, status=status.HTTP_200_OK)

    def put(self, request: Request) -> Response:
        community_psycho_pass = CommunityPsychoPass.objects.get(
            platform_id=request.data.get("communityID"))
        dominator = MessageDominator.objects.get(
            psycho_pass=community_psycho_pass)
        trigger_data = request.data.copy()
        trigger_data.pop("communityID")
        trigger_data["psycho_pass"] = community_psycho_pass.id
        serializer = MessageDominatorSerializer(
            dominator, data=trigger_data)
        serializer.is_valid(raise_exception=True)
        dominator = serializer.save()

        return Response(MessageDominatorSerializer(dominator).data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request: Request) -> Response:
        community_psycho_pass = CommunityPsychoPass.objects.get(
            platform_id=request.query_params.get("id"))
        dominator = MessageDominator.objects.get(
            psycho_pass=community_psycho_pass)
        dominator.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
