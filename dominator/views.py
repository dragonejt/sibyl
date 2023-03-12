from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from psychopass.models import CommunityPsychoPass
from dominator.models import MemberDominator, MemberDominatorSerializer, MessageDominator, MessageDominatorSerializer

# Create your views here.


class MemberDominatorView(APIView):

    def get(self, request: Request) -> Response:
        community_profile = CommunityPsychoPass.objects.get(
            platform_id=request.query_params.get("id"))
        dominator = MemberDominator.objects.get(profile=community_profile)

        return Response(MemberDominatorSerializer(dominator).data, status=status.HTTP_200_OK)

    def put(self, request: Request) -> Response:
        community_profile = CommunityPsychoPass.objects.get(
            platform_id=request.data.get("communityID"))
        dominator = MemberDominator.objects.get(
            profile=community_profile)
        trigger_data = request.data
        trigger_data.pop("communityID")
        trigger_data["profile"] = community_profile.id
        serializer = MemberDominatorSerializer(
            dominator, data=trigger_data)
        serializer.is_valid(raise_exception=True)
        dominator = serializer.save()

        return Response(MemberDominatorSerializer(dominator).data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request: Request) -> Response:
        community_profile = CommunityPsychoPass.objects.get(
            platform_id=request.query_params.get("id"))
        dominator = MemberDominator.objects.get(profile=community_profile)
        dominator.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class MessageDominatorView(APIView):

    def get(self, request: Request) -> Response:
        community_profile = CommunityPsychoPass.objects.get(
            platform_id=request.query_params.get("id"))
        dominator = MessageDominator.objects.get(profile=community_profile)

        return Response(MessageDominatorSerializer(dominator).data, status=status.HTTP_200_OK)

    def put(self, request: Request) -> Response:
        community_profile = CommunityPsychoPass.objects.get(
            platform_id=request.data.get("communityID"))
        dominator = MessageDominator.objects.get(
            profile=community_profile)
        trigger_data = request.data
        trigger_data.pop("communityID")
        trigger_data["profile"] = community_profile.id
        serializer = MessageDominatorSerializer(
            dominator, data=trigger_data)
        serializer.is_valid(raise_exception=True)
        dominator = serializer.save()

        return Response(MessageDominatorSerializer(dominator).data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request: Request) -> Response:
        community_profile = CommunityPsychoPass.objects.get(
            platform_id=request.query_params.get("id"))
        dominator = MessageDominator.objects.get(profile=community_profile)
        dominator.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
