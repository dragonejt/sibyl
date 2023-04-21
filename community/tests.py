from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from rest_framework.authtoken.models import Token
from community.views import Community, CommunitySerializer

# Create your tests here.


class TestCommunityView(APITestCase):

    def setUp(self) -> None:
        self.url = "/community"
        self.user = User.objects.create_superuser(username="discord")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")
        self.community = Community.objects.create(
            platform=self.user, community_id=get_random_string(20))

    def test_get(self) -> None:
        response = self.client.get(
            f"{self.url}?id={self.community.community_id}", format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(), CommunitySerializer(self.community).data)

    def test_post(self) -> None:
        community_id = get_random_string(20)
        response = self.client.post(
            self.url, data={"communityID": community_id}, format="json")
        community = Community.objects.get(
            platform=self.user, community_id=community_id)

        self.assertEqual(response.json().get("platform"), self.user.id)
        self.assertEqual(community.platform.id, self.user.id)
        self.assertEqual(response.json().get("community_id"), community_id)
        self.assertEqual(community.community_id, community_id)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete(self) -> None:
        community_id = self.community.community_id
        response = self.client.delete(
            f"{self.url}?id={self.community.community_id}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Community.DoesNotExist):
            Community.objects.get(platform=self.user,
                                  community_id=community_id)