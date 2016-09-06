from django.conf.urls import url
from django.conf.urls.static import static

from mysite import settings
from . import views


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/new/$', views.post_new, name='post_new'),
   # url(r'^*\.jpg$', views.post_new, name='post_new'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
