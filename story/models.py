from django.db import models

from user.models import User

# Create your models here.
class Story(models.Model):
    story_id = models.AutoField(primary_key=True)
    description = models.TextField()
    # currntly we are allowing user 
    content = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    user_id_who_posted = models.ForeignKey(User, on_delete=models.CASCADE)
    users_who_seen = models.ManyToManyField(User)

    def post_story(self):
        pass

    def delete_story(self):
        pass

    def get_stories(self):
        pass

    def watch_story(self):
        pass

    def user_who_seen(self):
        pass


    # class Meta:
    #     verbose_name = _("Story")
    #     verbose_name_plural = _("Storys")

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse("Story_detail", kwargs={"pk": self.pk})



