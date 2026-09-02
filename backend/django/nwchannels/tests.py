from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from django.test import TestCase

from nwchannels.models import NWChannel
from nwusers.models import NWUser, NWMembership, NWSubscription
from nwgroups.models import NWGroup

MAX_USERS = 5
USERS_IN_GROUP = 3
CHANNEL_COUNT = 2

class NWChannelTest(TestCase):
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


        new_channel = NWChannel.objects.create(
            name = "test_channel_1",
            owning_group=self.sample_group
        )

        NWSubscription.objects.create(
            user = nwusers[0],
            channel = new_channel,
            role = NWSubscription.Role.ADMIN,
        )

        NWSubscription.objects.create(
            user = nwusers[1],
            channel = new_channel,
        )

    def test_nwchannel_population(self):
        assert NWSubscription.objects.all().count() == 2