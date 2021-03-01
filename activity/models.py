from django.db import models
from django.urls import reverse

from user.models import User

# Create your models here.
class Activity(models.Model):
    activity_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    activity_type = models.CharField(max_length=50) # this can be enum
    description = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    # class method
    def record_activity(self):
        pass

    def remove_activity(self):
        pass

    def backup(self):
        pass

    def restore(self):
        pass

    # this will clear all activity of user
    def clear_all_activity(self):
        pass


    # class Meta:
    #     verbose_name = _("Activity")
    #     verbose_name_plural = _("Activitys")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Activity_detail", kwargs={"pk": self.pk})