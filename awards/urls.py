from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.get,name = 'get'),
    url('^new/post$',views.new_post,name='new_post'),
]