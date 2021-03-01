from django.db import models

from user.models import User

FRIENDS = 'F'
FRIENDS_OF_FRIEND = 'FOF'
PUBLIC = 'PU'
PRIVATE = 'PR'
SHARED_WITH = [
    (PRIVATE, 'PR'),
    (FRIENDS, 'Friends'),
    (FRIENDS_OF_FRIEND, 'Friends of Friends'),
    (PUBLIC, 'Public'),
]

# Create your models here.
class UserSetting(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    notification_preference = models.TextField() # store as json
    newsfeed_preference = models.TextField() # store as json
    post_default_shared_with = models.CharField(max_length=50, choices=SHARED_WITH)
    profile_details_shared_with = models.CharField(max_length=50, choices=SHARED_WITH)

    # class method
    def change_user_privacy_setting(self):
        pass

    def change_user_notification_preference(self):
        pass

    def change_user_newsfeed_preference(self):
        pass

    def change_post_default_shared_with(self):
        pass

    def change_profile_detail_shared_with(self):
        pass


    # django stuff
    # class Meta:
    #     verbose_name = _("UserSetting")
    #     verbose_name_plural = _("UserSettings")

    def __str__(self):
        return self.user_id

    def get_absolute_url(self):
        return reverse("UserSetting_detail", kwargs={"pk": self.pk})
