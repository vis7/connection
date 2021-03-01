from django.db import models
from django.urls import reverse

from user.models import User

# Create your models here.
class Friend(models.Model):
    # model table will keep record of friendrequest only but it's method had other functionality too
    # fr_id = models.AutoField()
    fr_send_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="fr_send_by")
    fr_send_to = models.ForeignKey(User ,on_delete=models.CASCADE, related_name="fr_send_to")

    # class method
    def send_friend_request(self, user_from, user_to):
        user_from = user_from

    def process_friend_request(self):
        pass

    def unfriend(self):
        pass

    def follow(self):
        pass

    def unfollow(self):
        pass

    def block(self):
        pass

    def unblock(self):
        pass

    def add_to_acquaintance(self):
        pass

    def remove_from_acquaintance(self):
        pass

    # check whether friend, following block
    def friendship_status(self):
        pass

    def check_friend_of_friend(self):
        pass

    # class Meta:
    #     verbose_name = _("Friend")
    #     verbose_name_plural = _("Friends")

    # this method need to return more meaningful content
    def __str__(self):
        # description = self.fr_send_by.username + " send frined request to " + self.fr_send_to.username
        description = self.fr_send_by
        return description

    def get_absolute_url(self):
        return reverse("friend:friend_detail", kwargs={"pk": self.pk})

