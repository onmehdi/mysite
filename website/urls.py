# from website.views import pagetest,json_test
from website.views import *
from django.urls import path


urlpatterns = [
    # path('urladdress','view','name')
    # path('pagetest', pagetest),
    # path('json-test', json_test),

    path('', index_view),
    path('about', about_view),
    path('contact', contact_view),
]
