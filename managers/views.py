from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from profiles.models import CommunityProfile, CommunityProfileSerializer
from managers.models import MessageManager, MessageManagerSerializer, MemberManager, MemberManagerSerializer

# Create your views here.
