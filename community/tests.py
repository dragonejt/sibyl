from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from community.views import Community, CommunitySerializer

# Create your tests here.


class TestCommunityView(APITestCase):
    def setUp(self) -> None:
        self.url = "/community"
        self.user = get_user_model().objects.create_superuser(
            username=get_random_string(10), email=None, password=None
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")
        self.community = Community.objects.create(
            platform=self.user, community_id=get_random_string(20)
        )

    def test_get(self) -> None:
        response = self.client.get(f"{self.url}?id={self.community.community_id}", format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), CommunitySerializer(self.community).data)

    def test_head_ok(self) -> None:
        response = self.client.head(f"{self.url}?id={self.community.community_id}")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_head_forbidden(self) -> None:
        user = get_user_model().objects.create(
            username=get_random_string(10),
            email=get_random_string(10),
            password=get_random_string(10),
        )
        community = Community.objects.create(platform=user, community_id=get_random_string(20))
        response = self.client.head(f"{self.url}?id={community.community_id}")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post(self) -> None:
        community_id = get_random_string(20)
        response = self.client.post(self.url, data={"communityID": community_id}, format="json")
        community = Community.objects.get(platform=self.user, community_id=community_id)

        self.assertEqual(response.json().get("platform"), self.user.id)
        self.assertEqual(community.platform.id, self.user.id)
        self.assertEqual(response.json().get("community_id"), community_id)
        self.assertEqual(community.community_id, community_id)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put(self) -> None:
        self.assertEqual(
            self.community.discord_log_channel,
            Community._meta.get_field("discord_log_channel").get_default(),
        )
        self.assertEqual(
            self.community.discord_notify_target,
            Community._meta.get_field("discord_notify_target").get_default(),
        )
        discord_log_channel = get_random_string(20)
        discord_notify_target = get_random_string(20)

        response = self.client.put(
            self.url,
            data={
                "communityID": self.community.community_id,
                "discord_log_channel": discord_log_channel,
                "discord_notify_target": discord_notify_target,
            },
            format="json",
        )

        self.community = Community.objects.get(community_id=self.community.community_id)

        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(self.community.discord_log_channel, discord_log_channel)
        self.assertEqual(self.community.discord_notify_target, discord_notify_target)

    def test_delete(self) -> None:
        community_id = self.community.community_id
        response = self.client.delete(f"{self.url}?id={self.community.community_id}", format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Community.DoesNotExist):
            Community.objects.get(platform=self.user, community_id=community_id)
