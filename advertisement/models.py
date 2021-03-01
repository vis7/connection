from django.db import models
from django.urls import reverse
# from user.models import Advertiser

from user.models import User, Advertiser

# Create your models here.
class Advertisement(models.Model):
    ACTIVE = 'A'
    DEACTIVE = 'D'
    EXPIRED = 'E'
    BLOCKED = 'B'
    ADVERTISEMENT_STATUS = [
        (ACTIVE, 'A'),
        (DEACTIVE, 'D'),
        (EXPIRED, 'E'),
        (BLOCKED, 'B')
    ]
    advertisement_id = models.AutoField(primary_key=True)
    # content will be image only
    content = models.ImageField(upload_to='advertisement/advertisement', height_field=None, width_field=None, max_length=None, blank=True)
    text_description = models.TextField()
    audience_details = models.TextField() # this can be change
    advertise_id = models.ForeignKey(Advertiser,on_delete=models.CASCADE)
    advertisement_link = models.URLField(max_length=200)
    user_preference = models.CharField(max_length=50) # this can be change
    money_credit = models.DecimalField(max_digits=5, decimal_places=2)
    view_need_to_shown = models.IntegerField()
    status = models.CharField(max_length=50, choices=ADVERTISEMENT_STATUS)
    user_who_watched = models.ForeignKey(User,on_delete=models.CASCADE)

    # method of class
    def create_advertisement(self):
        pass

    def edit_advertisement(self):
        pass

    def delete_advertisement(self):
        pass

    def get_details_of_ta(self):
        pass

    def update_details_of_ta(self):
        pass

    def get_advertisement(self):
        pass

    def watched_by_user(self):
        pass


    # class Meta:
    #     verbose_name = _("Advertisement")
    #     verbose_name_plural = _("Advertisements")

    def __str__(self):
        return self.text_description

    def get_absolute_url(self):
        return reverse("advertisement:advertisement_detail", kwargs={"pk": self.pk})


