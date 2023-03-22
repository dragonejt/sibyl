from django.test import TestCase
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from psychopass.views import UserPsychoPass, serialize_user, CommunityPsychoPass, serialize_community

# Create your tests here.


class TestUserPsychoPassView(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_superuser(username="discord")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")
        self.psycho_pass = UserPsychoPass.objects.create(
            platform=self.user.username, platform_id=get_random_string(20))

    def test_get(self) -> None:
        response = self.client.get(
            f"/psychopass/user?id={self.psycho_pass.platform_id}", format="json")
        self.assertEqual(response.json(), serialize_user(self.psycho_pass))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self) -> None:
        user_id = get_random_string(20)
        response = self.client.post(
            "/psychopass/user", data={"userID": user_id}, format="json")
        psycho_pass = UserPsychoPass.objects.get(platform_id=user_id)
        self.assertEqual(response.json().get("platform_id"), user_id)
        self.assertEqual(psycho_pass.platform_id, user_id)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete(self) -> None:
        user_id = self.psycho_pass.platform_id
        self.assertEqual(self.psycho_pass.platform_id, user_id)
        response = self.client.delete(
            f"/psychopass/user?id={self.psycho_pass.platform_id}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(UserPsychoPass.DoesNotExist):
            UserPsychoPass.objects.get(platform_id=user_id)


class TestCommunityPsychoPassView(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_superuser(username="discord")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")
        self.psycho_pass = CommunityPsychoPass.objects.create(
            platform=self.user.username, platform_id=get_random_string(20))

    def test_get(self) -> None:
        response = self.client.get(
            f"/psychopass/community?id={self.psycho_pass.platform_id}", format="json")
        self.assertEqual(
            response.json(), serialize_community(self.psycho_pass))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self) -> None:
        community_id = get_random_string(20)
        response = self.client.post(
            "/psychopass/community", data={"communityID": community_id}, format="json")
        psycho_pass = CommunityPsychoPass.objects.get(platform_id=community_id)
        self.assertEqual(response.json().get("platform_id"), community_id)
        self.assertEqual(psycho_pass.platform_id, community_id)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete(self) -> None:
        community_id = self.psycho_pass.platform_id
        self.assertEqual(self.psycho_pass.platform_id, community_id)
        response = self.client.delete(
            f"/psychopass/community?id={self.psycho_pass.platform_id}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(CommunityPsychoPass.DoesNotExist):
            CommunityPsychoPass.objects.get(platform_id=community_id)
