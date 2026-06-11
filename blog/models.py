from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


# Create your models here.
class Post(models.Model):
    image = models.ImageField(upload_to='blog/',default='blog/default.jpg')
    auther = models.ForeignKey(User,models.SET_NULL,null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    # tag
    category = models.ManyToManyField(Category)
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return "{} - {}".format(self.id,self.title)

# 2026-06-09 12:01:03.937334

# 2026-06-09 12:29:54.992774
# 2026-06-09 12:06:40.634158

