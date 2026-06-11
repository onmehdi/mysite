from django.db import models

# Create your models here.
class Post(models.Model):
    # image
    # auther
    title = models.CharField(max_length=200)
    content = models.TextField()
    # tag
    # category
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

