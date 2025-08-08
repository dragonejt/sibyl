from random import random

from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from psychopass.views import (
    Community,
    CommunityPsychoPass,
    CommunityPsychoPassSerializer,
    UserPsychoPass,
    UserPsychoPassSerializer,
)

# Create your tests here.


class TestUserPsychoPassView(APITestCase):
    def setUp(self) -> None:
        self.url = "/psychopass/user"
        self.user = get_user_model().objects.create_superuser(
            username=get_random_string(10), email=None, password=None
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")
        self.psycho_pass = UserPsychoPass.objects.create(
            platform=self.user, user_id=get_random_string(20)
        )

    def test_get(self) -> None:
        response = self.client.get(f"{self.url}?id={self.psycho_pass.user_id}", format="json")
        self.assertEqual(response.json(), UserPsychoPassSerializer(self.psycho_pass).data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_head_ok(self) -> None:
        response = self.client.head(f"{self.url}?id={self.psycho_pass.user_id}")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_head_forbidden(self) -> None:
        user = get_user_model().objects.create(
            username=get_random_string(10),
            email=get_random_string(10),
            password=get_random_string(10),
        )
        psycho_pass = UserPsychoPass.objects.create(platform=user, user_id=get_random_string(20))
        response = self.client.head(f"{self.url}?id={psycho_pass.user_id}")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post(self) -> None:
        user_id = get_random_string(20)
        response = self.client.post(self.url, data={"userID": user_id}, format="json")
        psycho_pass = UserPsychoPass.objects.get(platform=self.user, user_id=user_id)
        self.assertEqual(response.json().get("platform"), self.user.id)
        self.assertEqual(psycho_pass.platform.id, self.user.id)
        self.assertEqual(response.json().get("user_id"), user_id)
        self.assertEqual(psycho_pass.user_id, user_id)
        self.assertEqual(response.json(), UserPsychoPassSerializer(psycho_pass).data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete(self) -> None:
        user_id = self.psycho_pass.user_id
        response = self.client.delete(f"{self.url}?id={self.psycho_pass.user_id}", format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(UserPsychoPass.DoesNotExist):
            UserPsychoPass.objects.get(platform=self.user, user_id=user_id)


class TestCommunityPsychoPassView(APITestCase):
    def setUp(self) -> None:
        self.url = "/psychopass/community"
        self.user = get_user_model().objects.create_superuser(
            username=get_random_string(10), email=None, password=None
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")
        self.community = Community.objects.create(
            platform=self.user, community_id=get_random_string(20)
        )
        self.psycho_pass = CommunityPsychoPass.objects.create(community=self.community)

    def test_get(self) -> None:
        response = self.client.get(f"{self.url}?id={self.community.community_id}", format="json")

        self.assertEqual(response.json(), CommunityPsychoPassSerializer(self.psycho_pass).data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put(self) -> None:
        self.assertEqual(self.psycho_pass.users.all().count(), 0)
        self.user_psycho_pass = UserPsychoPass.objects.create(
            platform=self.user, user_id=get_random_string(20)
        )
        self.psycho_pass.users.add(self.user_psycho_pass)
        self.assertEqual(self.psycho_pass.users.all().count(), 1)

        response = self.client.put(
            self.url,
            data={
                "communityID": self.community.community_id,
                "userID": self.user_psycho_pass.user_id,
            },
            format="json",
        )

        self.psycho_pass = CommunityPsychoPass.objects.get(community=self.community)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(response.json(), CommunityPsychoPassSerializer(self.psycho_pass).data)
        self.assertEqual(self.psycho_pass.users.all().count(), 0)


class TestIngestMessage(APITestCase):
    def setUp(self) -> None:
        self.url = "/psychopass/message"
        self.user = get_user_model().objects.create_superuser(
            username=get_random_string(10), email=None, password=None
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")
        self.community = Community.objects.create(
            platform=self.user, community_id=get_random_string(20)
        )
        self.psycho_pass = CommunityPsychoPass.objects.create(community=self.community)

    def test_ingest_message(self) -> None:
        response = self.client.post(
            self.url,
            data={
                "attributeScores": {
                    "TOXICITY": {"summaryScore": {"value": random(), "type": "PROBABILITY"}},
                    "SEVERE_TOXICITY": {"summaryScore": {"value": random(), "type": "PROBABILITY"}},
                    "IDENTITY_ATTACK": {"summaryScore": {"value": random(), "type": "PROBABILITY"}},
                    "INSULT": {"summaryScore": {"value": random(), "type": "PROBABILITY"}},
                    "THREAT": {"summaryScore": {"value": random(), "type": "PROBABILITY"}},
                    "PROFANITY": {"summaryScore": {"value": random(), "type": "PROBABILITY"}},
                    "SEXUALLY_EXPLICIT": {
                        "summaryScore": {"value": random(), "type": "PROBABILITY"}
                    },
                },
                "languages": ["en"],
                "userID": get_random_string(20),
                "communityID": self.community.community_id,
            },
            format="json",
        )

        self.assertEqual(
            response.json().get("community"),
            CommunityPsychoPassSerializer(self.psycho_pass).data,
        )
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
