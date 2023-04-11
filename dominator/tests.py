import random
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from rest_framework.authtoken.models import Token
from dominator.views import CommunityPsychoPass, MemberDominator, MemberDominatorSerializer, MessageDominator, MessageDominatorSerializer

# Create your tests here.


class TestMemberDominatorView(APITestCase):

    def setUp(self) -> None:
        self.url = "/dominator/member"
        self.user = User.objects.create_superuser(username="discord")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")
        self.community_psycho_pass = CommunityPsychoPass.objects.create(
            platform=self.user, community_id=get_random_string(20))
        self.dominator = MemberDominator.objects.create(
            psycho_pass=self.community_psycho_pass)

    def test_get(self) -> None:
        response = self.client.get(
            f"{self.url}?id={self.community_psycho_pass.community_id}", format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(), MemberDominatorSerializer(self.dominator).data)

    def test_put(self) -> None:
        self.assertEqual(self.dominator.toxicity_action,
                         MemberDominator._meta.get_field("toxicity_action").get_default())
        self.assertEqual(self.dominator.toxicity_threshold,
                         MemberDominator._meta.get_field("toxicity_threshold").get_default())
        toxicity_action = random.randint(0, 4)
        toxicity_threshold = random.random()

        response = self.client.put(self.url, data={
            "communityID": self.community_psycho_pass.community_id,
            "toxicity_action": toxicity_action,
            "toxicity_threshold": toxicity_threshold
        })

        self.dominator = MemberDominator.objects.get(
            psycho_pass=self.community_psycho_pass)

        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(self.dominator.toxicity_action, toxicity_action)
        self.assertEqual(self.dominator.toxicity_threshold, toxicity_threshold)

    def test_delete(self) -> None:
        community_id = self.community_psycho_pass.community_id
        self.assertEqual(self.community_psycho_pass.community_id, community_id)

        response = self.client.delete(
            f"{self.url}?id={self.community_psycho_pass.community_id}", format="json")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(MemberDominator.DoesNotExist):
            MemberDominator.objects.get(psycho_pass=self.community_psycho_pass)


class TestMessageDominatorView(APITestCase):

    def setUp(self) -> None:
        self.url = "/dominator/message"
        self.user = User.objects.create_superuser(username="discord")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")
        self.community_psycho_pass = CommunityPsychoPass.objects.create(
            platform=self.user, community_id=get_random_string(20))
        self.dominator = MessageDominator.objects.create(
            psycho_pass=self.community_psycho_pass)

    def test_get(self) -> None:
        response = self.client.get(
            f"{self.url}?id={self.community_psycho_pass.community_id}", format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(), MessageDominatorSerializer(self.dominator).data)

    def test_put(self) -> None:
        self.assertEqual(self.dominator.toxicity_action,
                         MessageDominator._meta.get_field("toxicity_action").get_default())
        self.assertEqual(self.dominator.toxicity_threshold,
                         MessageDominator._meta.get_field("toxicity_threshold").get_default())
        toxicity_action = random.randint(0, 4)
        toxicity_threshold = random.random()

        response = self.client.put(self.url, data={
            "communityID": self.community_psycho_pass.community_id,
            "toxicity_action": toxicity_action,
            "toxicity_threshold": toxicity_threshold
        })

        self.dominator = MessageDominator.objects.get(
            psycho_pass=self.community_psycho_pass)

        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(self.dominator.toxicity_action, toxicity_action)
        self.assertEqual(self.dominator.toxicity_threshold, toxicity_threshold)

    def test_delete(self) -> None:
        community_id = self.community_psycho_pass.community_id
        self.assertEqual(self.community_psycho_pass.community_id, community_id)

        response = self.client.delete(
            f"{self.url}?id={self.community_psycho_pass.community_id}", format="json")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(MessageDominator.DoesNotExist):
            MessageDominator.objects.get(
                psycho_pass=self.community_psycho_pass)
