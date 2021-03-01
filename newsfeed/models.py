from django.db import models
from django.urls import reverse

from user.models import User

# Create your models here.
class NewsFeed(models.Model):
    newsfeed_id = models.AutoField(primary_key=True)
    post_id = models.ForeignKey("post.Post",on_delete=models.CASCADE)
    # priority = # this will be say 1 to 5
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_datetime = models.DateTimeField(auto_now=False, auto_now_add=True)

    # class method
    def get_newsfeed(self):
        pass

    def get_ads(self):
        pass

    def get_newsfeed_with_ads(self):
        pass

    def change_newsfeed_preference(self):
        pass

    def change_newsfeed_priority(self):
        pass

    # class Meta:
    #     verbose_name = _("NewsFeed")
    #     verbose_name_plural = _("NewsFeeds")

    def __str__(self):
        return self.newsfeed_id

    def get_absolute_url(self):
        return reverse("newsfeed:newsFeed_detail", kwargs={"pk": self.pk})
