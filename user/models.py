from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
import datetime


# classes for which there is no main role in application but used in Field of Model
class WorkPlace(models.Model):
    name = models.CharField(max_length=32)

class Education(models.Model):
    degree_name = models.CharField(max_length=32)
    University_name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

class CityInLived(models.Model):
    city = models.CharField(max_length=32)

MALE = 'M'
FEMALE = 'F'
OTHER = 'O'
GENDER = [
    (MALE, 'Male'),
    (FEMALE, 'Female'),
    (OTHER, 'Other'),
]
USER = 'U'
ADMIN = 'ADM'
ADVERTISER = 'ADV'
USER_TYPE = [
    (USER, 'User'),
    (ADMIN, 'Admin'),
    (ADVERTISER, 'Advertiser'),
]

# Create your models here.
class BaseUser(AbstractUser):
    # user_id = models.AutoField(primary_key=True)
    # duser = models.OneToOneField(DUser, on_delete=models.CASCADE)
    # username = models.CharField(max_length=32)
    dob = models.DateField(null=True)
    location = models.CharField(max_length=15) # only cityname
    country = models.CharField(max_length=10)
    mobile = models.DecimalField(max_digits=10, decimal_places=0, null=True)
    # email = models.EmailField()
    # password = models.CharField(max_length=4096)
    gender = models.CharField(max_length=6, choices=GENDER, null=True)
#     user_type = models.CharField(max_length=50, choices=USER_TYPE, null=True, default=USER)


class User(models.Model):
    SINGLE = 'S'
    IN_RELETIONSHIP = 'IR'
    MARRIED = 'M'
    RELATIONSHIP_STATUS = [
        (SINGLE, 'Single'),
        (IN_RELETIONSHIP, 'In a relationship'),
        (MARRIED, 'Married'),
    ]
    FREE = 'F'
    PREMIUM = 'P'
    SUBSCRIPTION_STATUS = [
        (FREE, 'Free'),
        (PREMIUM, 'Premium'),
    ]
    ACTIVE = 'A'
    BLOCKED = 'B'
    USER_STAUS = [
        (ACTIVE, 'Active'),
        (BLOCKED, 'Blocked'),
    ]
    # user_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE)
    # username = models.CharField(max_length=32)
    # dob = models.DateField(null=True)
    # location = models.CharField(max_length=15) # only cityname
    # country = models.CharField(max_length=10)
    # mobile = models.DecimalField(max_digits=10, decimal_places=0, null=True)
    # email = models.EmailField()
    # password = models.CharField(max_length=4096)
    # gender = models.CharField(max_length=6, choices=GENDER, null=True)
    # user_type = models.CharField(max_length=50, choices=USER_TYPE, null=True, default=USER)
    # work_experiance = models.ManyToManyField(WorkPlace)
    # education = models.ManyToManyField(Education)
    # place_where_you_lived = models.CharField(max_length=50)
    language = models.CharField(max_length=50, blank=True)
    relationship_status = models.CharField(max_length=15, choices=RELATIONSHIP_STATUS, blank=True)
    family_members = models.ManyToManyField("self", blank=True) # need to add relation also
    hobbies = models.CharField(max_length=150, blank=True)
    movies = models.CharField(max_length=150, blank=True)
    tv_shows = models.CharField(max_length=150, blank=True)
    books = models.CharField(max_length=150, blank=True)
    # registration_time = models.DateTimeField(auto_now_add=True)
    profile_pic = models.ImageField(upload_to='user/profile_pic', blank=True, default='profile_pic.jpeg')
    cover_pic = models.ImageField(upload_to='user/cover_pic', blank=True)
    # status = # active, deactive
    # user_subscribed_community =
    # user_pinned_community =
    friends = models.ManyToManyField("self", blank=True)
    follow = models.ManyToManyField("self", blank=True)
    aquaintances = models.ManyToManyField("self", blank=True)
    subscription_status = models.CharField(max_length=15, choices=SUBSCRIPTION_STATUS)
    subscription_exp_date = models.DateField(auto_now_add=True)
    saved_post = models.ManyToManyField("post.Post", blank=True)
    # community user joined
    user_community = models.ManyToManyField("community.Community", blank=True)

    def pay_subscription(self):
        pass

    def give_feedback(self):
        pass

    def update_profile(self):
        pass

    # this method delete account. This method is also overriden
    def delete_account(self):
        pass

    def add_details(self):
        pass

    def get_privacy_setting(self):
        pass

    def set_privacy_setting(self):
        pass

    def remove_details(self):
        pass

    def update_profile_pic(self):
        pass

    def update_cover_pic(self):
        pass

    # django stuff
    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("user:user_detail", kwargs={"pk": self.pk})


# class Admin(BaseUser):
#     # class method
#     def remove_post(self):
#         pass

#     def deactivate_account(self):
#         pass

#     def check_feedback(self):
#         pass

#     # this method is overriden
#     def delete_account(self):
#         pass

#     def remove_story(self):
#         pass

#     def watch_feedback(self):
#         pass

#     # django stuff
#     # class Meta:
#     #     verbose_name = _("Admin")
#     #     verbose_name_plural = _("Admins")

#     def __str__(self):
#         return self.username

#     def get_absolute_url(self):
#         return reverse("user:admin_detail", kwargs={"pk": self.pk})

class Advertiser(models.Model):
    # user_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE)
    # username = models.CharField(max_length=32)
    # email = models.EmailField()
    # password = models.CharField(max_length=4096)
    # dob = models.DateField(null=True)
    # location = models.CharField(max_length=15) # only cityname
    # country = models.CharField(max_length=10)
    # mobile = models.DecimalField(max_digits=10, decimal_places=0, null=True)
    # gender = models.CharField(max_length=6, choices=GENDER, null=True)
    # user_type = models.CharField(max_length=50, choices=USER_TYPE, null=True, default=USER)
    balance = models.DecimalField(max_digits=5, decimal_places=2)

    # methods of class
    # def post_advertisement(self):
    #     pass

    # def pay_money(self):
    #     pass

    # def give_feedback(self):
    #     pass

    # def delete_account(self):
    #     pass

    # django stuff
    # class Meta:
    #     verbose_name = _("Advertiser")
    #     verbose_name_plural = _("Advertisers")

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("user:advertiser_detail", kwargs={"pk": self.pk})

# class Advertiser(models.Model):
#     balance = models.DecimalField(max_digits=5, decimal_places=2)
