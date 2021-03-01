from django.db import models
from django.urls import reverse

from user.models import User

# Create your models here.
class Community(models.Model):
    community_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    admin_id = models.OneToOneField(User,on_delete=models.CASCADE)
    rules = models.TextField()
    registration_time = models.DateField(auto_now=False, auto_now_add=True)
    total_number_of_subscribers = models.DecimalField(max_digits=5, decimal_places=0, default=0)
    description = models.TextField()
    community_posts = models.ManyToManyField("post.Post", related_name="community_post")
    pinned_posts = models.ManyToManyField("post.Post", related_name="pinned_post")

    # methods of class
    def add_post_to_community(self):
        pass

    # post can be removed by user who posted or admin if he feels it inappropriate
    def remove_post_from_community(self):
        pass

    def add_description(self):
        pass

    def edit_description(self):
        pass

    def edit_rules(self):
        pass


    # django thing
    # class Meta:
    #     verbose_name = _("Community")
    #     verbose_name_plural = _("Communitys")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("community:community_detail", kwargs={"pk": self.pk})
