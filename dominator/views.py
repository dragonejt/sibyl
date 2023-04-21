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
        community = Community.objects.get(
            community_id=request.query_params.get("id"))
        dominator = MemberDominator.objects.get(community=community)

        return Response(MemberDominatorSerializer(dominator).data, status=status.HTTP_200_OK)

    def put(self, request: Request) -> Response:
        community = Community.objects.get(
            community_id=request.query_params.get("id"))
        dominator = MemberDominator.objects.get(community=community)
        trigger_data = request.data.copy()
        trigger_data["community"] = community.id
        serializer = MemberDominatorSerializer(
            dominator, data=trigger_data)
        serializer.is_valid(raise_exception=True)
        dominator = serializer.save()

        return Response(MemberDominatorSerializer(dominator).data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request: Request) -> Response:
        community = Community.objects.get(
            community_id=request.query_params.get("id"))
        dominator = MemberDominator.objects.get(community=community)
        dominator.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class MessageDominatorView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request: Request) -> Response:
        community = Community.objects.get(
            community_id=request.query_params.get("id"))
        dominator = MessageDominator.objects.get(community=community)

        return Response(MessageDominatorSerializer(dominator).data, status=status.HTTP_200_OK)

    def put(self, request: Request) -> Response:
        community = Community.objects.get(
            community_id=request.query_params.get("id"))
        dominator = MessageDominator.objects.get(community=community)
        trigger_data = request.data.copy()
        trigger_data["community"] = community.id
        serializer = MessageDominatorSerializer(
            dominator, data=trigger_data)
        serializer.is_valid(raise_exception=True)
        dominator = serializer.save()

        return Response(MessageDominatorSerializer(dominator).data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request: Request) -> Response:
        community = Community.objects.get(
            community_id=request.query_params.get("id"))
        dominator = MessageDominator.objects.get(community=community)
        dominator.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
