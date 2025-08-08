from http import HTTPStatus

from django.shortcuts import get_object_or_404
from drf_spectacular.utils import (
    OpenApiParameter,
    OpenApiResponse,
    extend_schema,
    inline_serializer,
)
from rest_framework import status
from rest_framework.fields import CharField
from rest_framework.permissions import IsAdminUser
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from community.models import Community, CommunitySerializer
from dominator.models import MemberDominator, MessageDominator
from psychopass.models import CommunityPsychoPass

# Create your views here.


class CommunityView(APIView):
    permission_classes = [IsAdminUser]

    @extend_schema(
        operation_id="read community",
        parameters=[
            OpenApiParameter(
                "id",
                str,
                required=True,
                description="retrieves the community with this id",
            )
        ],
        responses={
            "200": CommunitySerializer,
            "400": OpenApiResponse(description="Missing field in query params or body"),
            "404": OpenApiResponse(description="Item not found with provided details"),
            "500": OpenApiResponse(description=HTTPStatus.INTERNAL_SERVER_ERROR.description),
        },
    )
    def get(self, request: Request) -> Response:
        community = get_object_or_404(
            Community,
            platform=request.user,
            community_id=request.query_params.get("id"),
        )

        return Response(CommunitySerializer(community).data, status=status.HTTP_200_OK)

    @extend_schema(
        operation_id="create community",
        request=inline_serializer(
            "create_community_serializer",
            {
                "community_id": CharField(max_length=20),
            },
        ),
        responses={
            "200": CommunitySerializer,
            "400": OpenApiResponse(description="Missing field in query params or body"),
            "404": OpenApiResponse(description="Item not found with provided details"),
            "500": OpenApiResponse(description=HTTPStatus.INTERNAL_SERVER_ERROR.description),
        },
    )
    def post(self, request: Request) -> Response:
        community = Community.objects.create(
            platform=request.user, community_id=request.data.get("community_id")
        )
        CommunityPsychoPass.objects.create(community=community)
        MemberDominator.objects.create(community=community)
        MessageDominator.objects.create(community=community)

        return Response(CommunitySerializer(community).data, status=status.HTTP_201_CREATED)

    @extend_schema(
        operation_id="update community",
        request=CommunitySerializer,
        responses={
            "202": CommunitySerializer,
            "400": OpenApiResponse(description="Missing field in query params or body"),
            "404": OpenApiResponse(description="Item not found with provided details"),
            "500": OpenApiResponse(description=HTTPStatus.INTERNAL_SERVER_ERROR.description),
        },
    )
    def patch(self, request: Request) -> Response:
        community = get_object_or_404(
            Community, platform=request.user, community_id=request.data.get("community_id")
        )
        serializer = CommunitySerializer(community, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        community = serializer.save()

        return Response(CommunitySerializer(community).data, status=status.HTTP_202_ACCEPTED)

    @extend_schema(
        operation_id="delete community",
        parameters=[
            OpenApiParameter(
                "id",
                str,
                required=True,
                description="deletes the community with this id",
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
        community = get_object_or_404(
            Community,
            platform=request.user,
            community_id=request.query_params.get("id"),
        )
        community.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
