from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from psychopass.models import UserPsychoPass, UserPsychoPassSerializer, CommunityPsychoPass, CommunityPsychoPassSerializer
from dominator.models import MemberDominator, MessageDominator
# Create your views here.


@api_view(["POST"])
@permission_classes([IsAdminUser])
def ingest_message(request: Request) -> Response:
    psycho_pass, _ = UserPsychoPass.objects.get_or_create(
        platform=request.user, user_id=request.data.get("userID"))
    community_psycho_pass, _ = CommunityPsychoPass.objects.get_or_create(
        platform=request.user, community_id=request.data.get("communityID"))

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
        if psycho_pass is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
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
        community_psycho_pass = CommunityPsychoPass.objects.get(
            community_id=request.query_params.get("id"))
        if community_psycho_pass is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serialize_community(community_psycho_pass), status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        community_psycho_pass = CommunityPsychoPass.objects.create(
            platform=request.user, community_id=request.data.get("communityID"))
        community_psycho_pass.save()
        member_dominator = MemberDominator.objects.create(
            psycho_pass=community_psycho_pass)
        member_dominator.save()
        message_dominator = MessageDominator.objects.create(
            psycho_pass=community_psycho_pass)
        message_dominator.save()
        return Response(serialize_community(community_psycho_pass), status=status.HTTP_201_CREATED)

    def delete(self, request: Request) -> Response:
        community_psycho_ass = CommunityPsychoPass.objects.get(
            community_id=request.query_params.get("id"))
        community_psycho_ass.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


def serialize_user(psycho_pass: UserPsychoPass) -> dict:
    data = UserPsychoPassSerializer(psycho_pass).data
    data["crime_coefficient"] = psycho_pass.crime_coefficient()
    data["hue"] = psycho_pass.hue()
    return data


def serialize_community(community_psycho_ass: CommunityPsychoPass) -> dict:
    data = CommunityPsychoPassSerializer(community_psycho_ass).data
    data["area_stress_level"] = community_psycho_ass.area_stress_level()
    return data
