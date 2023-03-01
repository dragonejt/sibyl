from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from profiles.models import UserProfile, ServerProfile, UserProfileSerializer, ServerProfileSerializer
# Create your views here.

@api_view(["POST"])
@permission_classes([AllowAny])
def ingest_message(request: Request) -> Response:
    print(request.data)
    return Response(status=status.HTTP_200_OK)

class UserProfiles(APIView):

    def get(self, request: Request) -> Response:
        profile = UserProfile.objects.get(platform_id=request.get("ID"))
        return Response(status=status.HTTP_200_OK)