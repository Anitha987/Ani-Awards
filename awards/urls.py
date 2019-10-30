from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url('^$',views.get,name = 'get'),
    url('^new/post$',views.new_post,name='new_post'),
    url(r'^profile/',views.profile,name='profile'),
    url(r'^accounts/profileform', views.profile_form, name='profileform'),
    url(r'^votes/',views.review_form,name='reviewform'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
