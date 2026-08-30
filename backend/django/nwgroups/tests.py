from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from nwusers.models import NWUser, NWMembership
from nwgroups.models import NWGroup

MAX_USERS = 5
USERS_IN_GROUP = 3

class NWGroupModelTest(TestCase):
    """
    Extremely basic tests for NWGroup model due to time constraints
    """
    def setUp(self):
        self.sample_group = NWGroup.objects.create(name="test")

        nwusers = []

        for i in range(1,MAX_USERS+1):
            new_user = User.objects.create(username=f"test_user_{i}", password=f"test_user_{i}")
            nwusers.append(NWUser.objects.create(user=new_user))

        NWMembership.objects.create(user=nwusers[0], group=self.sample_group, role=NWMembership.Role.ADMIN)

        for i in range(1,USERS_IN_GROUP):
            NWMembership.objects.create(user=nwusers[i], group=self.sample_group)

    # Testing getting members in a group
    def test_membership_get_success(self):
        response = self.client.get(f"/groups/{self.sample_group.id}/get_members/")
        assert response.status_code == 200

    def test_membership_group_not_found(self):
        response = self.client.get(f"/groups/{self.sample_group.id+1}/get_members/")
        assert response.status_code == 404








