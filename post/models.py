from django.db import models
from django.urls import reverse

from user.models import User

FRIENDS = 'F'
FRIENDS_OF_FRIEND = 'FOF'
PUBLIC = 'P'
SHARED_WITH = [
    (FRIENDS, 'Friends'),
    (FRIENDS_OF_FRIEND, 'Friends of Friends'),
    (PUBLIC, 'Public'),
]

# Create your models here.
class Post(models.Model):
    ACTIVE = 'A'
    REPORTED = 'R'
    BLOCKED = 'B'
    STATUS = [
        (ACTIVE, 'Active'),
        (REPORTED, 'Reported'),
        (BLOCKED, 'Blocked'),
    ]
    post_id = models.AutoField(primary_key=True)
    text_description = models.TextField()
    # note that currnty user only allowed to share images
    content = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None, blank=True)
    user_who_posted = models.ForeignKey(User,on_delete=models.CASCADE, related_name="user_who_posted")
    post_type = models.CharField(max_length=50)
    likes = models.DecimalField(max_digits=5, decimal_places=0, default=0)
    dislikes = models.DecimalField(max_digits=5, decimal_places=0, default=0)
    status = models.CharField(max_length=50, choices=STATUS)
    shared_with = models.CharField(max_length=20, choices=SHARED_WITH)
    user_who_liked = models.ManyToManyField(User, related_name="user_who_liked", blank=True)
    user_who_disliked = models.ManyToManyField(User, related_name="user_who_disliked", blank=True)
    datetime = models.DateTimeField(auto_now=False, auto_now_add=True)

    # class method
    def do_post(self):
        pass

    # user also can edit to shared with
    def edit_post(self):
        pass

    def delete_post(self):
        pass

    def like(self):
        pass

    def dislike(self):
        pass

    def report_post(self):
        pass

    def save_post(self):
        pass

    def change_status(self):
        pass


    # django specific
    # class Meta:
    #     verbose_name = _("Post")
    #     verbose_name_plural = _("Posts")

    def __str__(self):
        return self.text_description

    def get_absolute_url(self):
        return reverse("post:post_detail", kwargs={"pk": self.pk})
        # return reverse("post:post_detail", kwargs={"post_id": self.post_id})


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comment_text = models.TextField()
    user_id = models.ForeignKey(User ,on_delete=models.CASCADE, related_name="user_who_commented")
    on_post = models.ForeignKey(Post, on_delete=models.CASCADE)

    # method of class
    def do_comment(self):
        pass

    def edit_comment(self):
        pass

    def delete_comment(self):
        pass

    def fetch_comment(self):
        pass



    # class Meta:
    #     verbose_name = _("Comment")
    #     verbose_name_plural = _("Comments")

    def __str__(self):
        return self.comment_text

    def get_absolute_url(self):
        # return reverse("post:comment_detail", kwargs={"post_id":self.on_post, "comment_id": self.comment_id })
        return reverse("post:comment_detail", kwargs={"pk": self.pk })


