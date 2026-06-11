# from website.views import pagetest,json_test
from blog.views import *
from django.urls import path


app_name = 'blog'

urlpatterns = [
    # path('urladdress','view','name')
    # path('pagetest', pagetest),
    # path('json-test', json_test),

    path('', blog_view, name='index'),
    path('<int:pid>', blog_single, name='single'),
    # path('post-<int:pid>',test_view, name='test'),
]
