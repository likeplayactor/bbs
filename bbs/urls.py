"""bbs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from post import views as post_views
from user import views as user_views

urlpatterns = [
    url('post/list/', post_views.post_list),
    url('post/create/', post_views.create_post),
    url('post/edit/', post_views.edit_post),
    url('post/read/', post_views.read_post),
    url('post/search/', post_views.search),

    url('^user/register/', user_views.register),
    url('^user/login/', user_views.login),
    url('^user/logout/', user_views.logout),
    url('^user/info/', user_views.user_info),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
