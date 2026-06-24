# from website.views import pagetest,json_test
from website.views import *
from django.urls import path



app_name = 'website'

urlpatterns = [
    # path('urladdress','view','name')
    # path('pagetest', pagetest),
    # path('json-test', json_test),

    path('', index_view,name='index'),
    path('about', about_view,name='about'),
    path('contact', contact_view,name='contact'),
    path('test', test_view,name='test'),
    path('index1',index1_view),
    path('test1',test1_view,name='test1'),
    path('newsletter',newsletter_view,name='newsletter')
]
