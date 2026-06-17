# from website.views import pagetest,json_test
from blog.views import *
from django.urls import path


app_name = 'blog'

urlpatterns = [
    # path('urladdress','view','name')
    # path('pagetest', pagetest),
    # path('json-test', json_test),

    path('', blog_view, name='index'),
    path('category/<str:catname>', blog_view, name='postcat'),
    path('auther/<str:auther_username>', blog_view, name='post_auther'),
    path('<int:pid>', blog_single, name='single'),
    path('test',test_view, name='test'),
    # path('post-<int:pid>',test_view, name='test'),
]
