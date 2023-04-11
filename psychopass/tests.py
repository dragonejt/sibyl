from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from rest_framework import status
from rest_framework.authtoken.models import Token
from psychopass.views import UserPsychoPass, serialize_user, CommunityPsychoPass, serialize_community

# Create your tests here.


class TestUserPsychoPassView(APITestCase):

    def setUp(self) -> None:
        self.url = "/psychopass/user"
        self.user = User.objects.create_superuser(username="discord")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")
        self.psycho_pass = UserPsychoPass.objects.create(
            platform=self.user, user_id=get_random_string(20))

    def test_get(self) -> None:
        response = self.client.get(
            f"{self.url}?id={self.psycho_pass.user_id}", format="json")
        self.assertEqual(response.json(), serialize_user(self.psycho_pass))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self) -> None:
        user_id = get_random_string(20)
        response = self.client.post(
            self.url, data={"userID": user_id}, format="json")
        psycho_pass = UserPsychoPass.objects.get(user_id=user_id)
        self.assertEqual(response.json().get("user_id"), user_id)
        self.assertEqual(psycho_pass.user_id, user_id)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete(self) -> None:
        user_id = self.psycho_pass.user_id
        self.assertEqual(self.psycho_pass.user_id, user_id)
        response = self.client.delete(
            f"{self.url}?id={self.psycho_pass.user_id}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(UserPsychoPass.DoesNotExist):
            UserPsychoPass.objects.get(user_id=user_id)


class TestCommunityPsychoPassView(APITestCase):

    def setUp(self) -> None:
        self.url = "/psychopass/community"
        self.user = User.objects.create_superuser(username="discord")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")
        self.psycho_pass = CommunityPsychoPass.objects.create(
            platform=self.user, community_id=get_random_string(20))

    def test_get(self) -> None:
        response = self.client.get(
            f"{self.url}?id={self.psycho_pass.community_id}", format="json")
        self.assertEqual(
            response.json(), serialize_community(self.psycho_pass))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self) -> None:
        community_id = get_random_string(20)
        response = self.client.post(
            self.url, data={"communityID": community_id}, format="json")
        psycho_pass = CommunityPsychoPass.objects.get(community_id=community_id)
        self.assertEqual(response.json().get("community_id"), community_id)
        self.assertEqual(psycho_pass.community_id, community_id)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete(self) -> None:
        community_id = self.psycho_pass.community_id
        self.assertEqual(self.psycho_pass.community_id, community_id)
        response = self.client.delete(
            f"{self.url}?id={self.psycho_pass.community_id}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(CommunityPsychoPass.DoesNotExist):
            CommunityPsychoPass.objects.get(community_id=community_id)


class TestIngestMessage(APITestCase):

    def setUp(self) -> None:
        self.url = "/psychopass/message"
        self.user = User.objects.create_superuser(username="discord")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

    def test_ingest_message(self) -> None:
        response = self.client.post(self.url, data={
            "attributeScores": {
                "TOXICITY": {
                    "summaryScore": {
                        "value": 0.5,
                        "type": "PROBABILITY"
                    }
                },
                "SEVERE_TOXICITY": {
                    "summaryScore": {
                        "value": 0.5,
                        "type": "PROBABILITY"
                    }
                },
                "IDENTITY_ATTACK": {
                    "summaryScore": {
                        "value": 0.5,
                        "type": "PROBABILITY"
                    }
                },
                "INSULT": {
                    "summaryScore": {
                        "value": 0.5,
                        "type": "PROBABILITY"
                    }
                },
                "THREAT": {
                    "summaryScore": {
                        "value": 0.5,
                        "type": "PROBABILITY"
                    }
                },
                "PROFANITY": {
                    "summaryScore": {
                        "value": 0.5,
                        "type": "PROBABILITY"
                    }
                },
                "SEXUALLY_EXPLICIT": {
                    "summaryScore": {
                        "value": 0.5,
                        "type": "PROBABILITY"
                    }
                }
            },
            "languages": ["en"],
            "userID": get_random_string(20),
            "communityID": get_random_string(20)
        }, format="json")

        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
