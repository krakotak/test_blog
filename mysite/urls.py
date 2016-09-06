
from django.conf.urls import url, include
from django.contrib import admin


import blog.urls
from mysite import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include(blog.urls)),

]