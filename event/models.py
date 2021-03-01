from django.db import models
from django.urls import reverse

from user.models import User

# Create your models here.
class Event(models.Model):
    BIRTHDAY = 'B'
    MARRIAGE = 'MR'
    MEET = 'ME' # friend meet
    EDUCATION_EVENT = 'EE'
    EVENT_TYPE = [
        (BIRTHDAY, 'B'),
        (MARRIAGE, 'MR'),
        (MEET, 'ME'),
        (EDUCATION_EVENT, 'EE'),
    ]

    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=50)
    description = models.TextField()
    location = models.CharField(max_length=50)
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    event_type = models.CharField(max_length=50, choices=EVENT_TYPE)
    intrested_user = models.ManyToManyField(User, blank=True, related_name='interested_user')
    going_user = models.ManyToManyField(User, blank=True, related_name='going_user')

    # class method
    def create_event(self):
        pass

    def update_event(self):
        pass

    def delete_event(self):
        pass

    def add_intrested_user(self):
        pass

    def add_going_user(self):
        pass

    def remove_intrested_user(self):
        pass

    def remove_going_user(self):
        pass

    def get_event_by_attributes(self):
        pass


    # class Meta:
    #     verbose_name = _("Event")
    #     verbose_name_plural = _("Events")

    def __str__(self):
        return self.event_name

    def get_absolute_url(self):
        return reverse("event:event_detail", kwargs={"pk": self.pk})
