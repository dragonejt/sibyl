from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from community.models import Community
from dominator.models import MemberDominator, MemberDominatorSerializer, MessageDominator, MessageDominatorSerializer

# Create your views here.


class MemberDominatorView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request: Request) -> Response:
        community = get_object_or_404(
            Community, community_id=request.query_params.get("id"))
        dominator = get_object_or_404(MemberDominator, community=community)

        return Response(MemberDominatorSerializer(dominator).data, status=status.HTTP_200_OK)

    def put(self, request: Request) -> Response:
        community = get_object_or_404(
            Community, community_id=request.data.get("communityID"))
        dominator = get_object_or_404(MemberDominator, community=community)
        trigger_data = request.data.copy()
        trigger_data.pop("communityID")
        trigger_data["community"] = community.id
        serializer = MemberDominatorSerializer(
            dominator, data=trigger_data)
        serializer.is_valid(raise_exception=True)
        dominator = serializer.save()

        return Response(MemberDominatorSerializer(dominator).data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request: Request) -> Response:
        community = get_object_or_404(
            Community, community_id=request.query_params.get("id"))
        dominator = get_object_or_404(MemberDominator, community=community)
        dominator.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class MessageDominatorView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request: Request) -> Response:
        community = get_object_or_404(
            Community, community_id=request.query_params.get("id"))
        dominator = get_object_or_404(MessageDominator, community=community)

        return Response(MessageDominatorSerializer(dominator).data, status=status.HTTP_200_OK)

    def put(self, request: Request) -> Response:
        community = get_object_or_404(
            Community, community_id=request.data.get("communityID"))
        dominator = get_object_or_404(MessageDominator, community=community)
        trigger_data = request.data.copy()
        trigger_data.pop("communityID")
        trigger_data["community"] = community.id
        serializer = MessageDominatorSerializer(
            dominator, data=trigger_data)
        serializer.is_valid(raise_exception=True)
        dominator = serializer.save()

        return Response(MessageDominatorSerializer(dominator).data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request: Request) -> Response:
        community = get_object_or_404(
            Community, community_id=request.query_params.get("id"))
        dominator = get_object_or_404(MessageDominator, community=community)
        dominator.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
