from django.db import models
from django.urls import reverse

from user.models import User

# Create your models here.
class Notification(models.Model):
    BIRTHDAY_REMINDER = 'B'
    UPDATE_FOR_YOU = 'U' # this is for anyone commented on his post
    NOTIFICATION_TYPE = [
        (BIRTHDAY_REMINDER, 'B'),
        (UPDATE_FOR_YOU, 'U')
    ]
    READED = 'R'
    UNREADED = 'U'
    NOTIFICATION_STATUS = [
        (READED, 'R'),
        (UNREADED, 'U'),
    ]
    notification_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=150)
    n_type = models.CharField(max_length=50, choices=NOTIFICATION_TYPE)
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    user_id = models.ForeignKey(User ,on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=NOTIFICATION_TYPE)

    # methods
    def generate_notification(self):
        pass

    def read_notification(self):
        pass

    # notification will automatically deleted if it is more then 15 days old or user has more then 50
    # nonitication in that case old notification will be automatically deleted
    def automatic_delete_notification(self):
        pass

    # get notification for user
    def get_notification(self):
        pass

    # add notification to notification table
    def add_notification(sefl):
        pass




    # class Meta:
    #     verbose_name = _("Notification")
    #     verbose_name_plural = _("Notifications")

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse("notification:notification_detail", kwargs={"pk": self.pk})
