from django.db import models

# Create your models here.

# this model will not have database entry
class Search(models.Model):
    # startdate and enddate will be used in searching event, post
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    location = models.CharField(max_length=50)
    item_name_to_search = models.CharField(max_length=50)
    # item_type could be json because we are searching more then onetype at a time
    item_type_to_search = models.CharField(max_length=50)

    # class method
    def search(self):
        pass

    def change_startdate(self):
        pass

    def change_enddate(self):
        pass

    def change_location(self):
        pass

    def change_item_type_to_search(self):
        pass

    def change_item_name_to_search(self):
        pass

    # django stuff
    # class Meta:
    #     verbose_name = _("Search")
    #     verbose_name_plural = _("Searchs")

    def __str__(self):
        return self.item_name_to_search

    def get_absolute_url(self):
        return reverse("Search_detail", kwargs={"pk": self.pk})


