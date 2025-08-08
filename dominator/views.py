from http import HTTPStatus

from django.shortcuts import get_object_or_404
from drf_spectacular.utils import (
    OpenApiParameter,
    OpenApiResponse,
    extend_schema,
)
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from community.models import Community
from dominator.models import (
    MemberDominator,
    MemberDominatorSerializer,
    MessageDominator,
    MessageDominatorSerializer,
)

# Create your views here.


class MemberDominatorView(APIView):
    permission_classes = [IsAdminUser]

    @extend_schema(
        operation_id="read member dominator",
        parameters=[
            OpenApiParameter(
                "id",
                str,
                required=True,
                description="retrieves the member dominator of the community with this id",
            )
        ],
        responses={
            "200": MemberDominatorSerializer,
            "400": OpenApiResponse(description="Missing field in query params or body"),
            "404": OpenApiResponse(description="Item not found with provided details"),
            "500": OpenApiResponse(description=HTTPStatus.INTERNAL_SERVER_ERROR.description),
        },
    )
    def get(self, request: Request) -> Response:
        community = get_object_or_404(Community, community_id=request.query_params.get("id"))
        dominator = get_object_or_404(MemberDominator, community=community)

        return Response(MemberDominatorSerializer(dominator).data, status=status.HTTP_200_OK)

    @extend_schema(
        operation_id="update member dominator",
        request=MemberDominatorSerializer,
        responses={
            "202": MemberDominatorSerializer,
            "400": OpenApiResponse(description="Missing field in query params or body"),
            "404": OpenApiResponse(description="Item not found with provided details"),
            "500": OpenApiResponse(description=HTTPStatus.INTERNAL_SERVER_ERROR.description),
        },
    )
    def patch(self, request: Request) -> Response:
        community = get_object_or_404(Community, community_id=request.data.get("community_id"))
        dominator = get_object_or_404(MemberDominator, community=community)
        trigger_data = request.data.copy()
        trigger_data.pop("community_id")
        trigger_data["community"] = community.id
        serializer = MemberDominatorSerializer(dominator, data=trigger_data)
        serializer.is_valid(raise_exception=True)
        dominator = serializer.save()

        return Response(MemberDominatorSerializer(dominator).data, status=status.HTTP_202_ACCEPTED)

    @extend_schema(
        operation_id="delete member dominator",
        parameters=[
            OpenApiParameter(
                "id",
                str,
                required=True,
                description="deletes the member dominator of the community with this id",
            )
        ],
        responses={
            "204": OpenApiResponse(description=HTTPStatus.NO_CONTENT.description),
            "400": OpenApiResponse(description="Missing field in query params or body"),
            "404": OpenApiResponse(description="Item not found with provided details"),
            "500": OpenApiResponse(description=HTTPStatus.INTERNAL_SERVER_ERROR.description),
        },
    )
    def delete(self, request: Request) -> Response:
        community = get_object_or_404(Community, community_id=request.query_params.get("id"))
        dominator = get_object_or_404(MemberDominator, community=community)
        dominator.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class MessageDominatorView(APIView):
    permission_classes = [IsAdminUser]

    @extend_schema(
        operation_id="read message dominator",
        parameters=[
            OpenApiParameter(
                "id",
                str,
                required=True,
                description="retrieves the message dominator of the community with this id",
            )
        ],
        responses={
            "200": MessageDominatorSerializer,
            "400": OpenApiResponse(description="Missing field in query params or body"),
            "404": OpenApiResponse(description="Item not found with provided details"),
            "500": OpenApiResponse(description=HTTPStatus.INTERNAL_SERVER_ERROR.description),
        },
    )
    def get(self, request: Request) -> Response:
        community = get_object_or_404(Community, community_id=request.query_params.get("id"))
        dominator = get_object_or_404(MessageDominator, community=community)

        return Response(MessageDominatorSerializer(dominator).data, status=status.HTTP_200_OK)

    @extend_schema(
        operation_id="update message dominator",
        request=MessageDominatorSerializer,
        responses={
            "202": MessageDominatorSerializer,
            "400": OpenApiResponse(description="Missing field in query params or body"),
            "404": OpenApiResponse(description="Item not found with provided details"),
            "500": OpenApiResponse(description=HTTPStatus.INTERNAL_SERVER_ERROR.description),
        },
    )
    def patch(self, request: Request) -> Response:
        community = get_object_or_404(Community, community_id=request.data.get("community_id"))
        dominator = get_object_or_404(MessageDominator, community=community)
        trigger_data = request.data.copy()
        trigger_data.pop("community_id")
        trigger_data["community"] = community.id
        serializer = MessageDominatorSerializer(dominator, data=trigger_data)
        serializer.is_valid(raise_exception=True)
        dominator = serializer.save()

        return Response(MessageDominatorSerializer(dominator).data, status=status.HTTP_202_ACCEPTED)

    @extend_schema(
        operation_id="delete message dominator",
        parameters=[
            OpenApiParameter(
                "id",
                str,
                required=True,
                description="deletes the message dominator of the community with this id",
            )
        ],
        responses={
            "204": OpenApiResponse(description=HTTPStatus.NO_CONTENT.description),
            "400": OpenApiResponse(description="Missing field in query params or body"),
            "404": OpenApiResponse(description="Item not found with provided details"),
            "500": OpenApiResponse(description=HTTPStatus.INTERNAL_SERVER_ERROR.description),
        },
    )
    def delete(self, request: Request) -> Response:
        community = get_object_or_404(Community, community_id=request.query_params.get("id"))
        dominator = get_object_or_404(MessageDominator, community=community)
        dominator.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
