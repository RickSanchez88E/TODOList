"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# myproject/urls.py
from django.contrib import admin
from django.urls import path
from myapp.views import *
from myproject import settings
from django.conf.urls.static import static
from myapp.models import *
from myapp.forms import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('index/<str:song_name>', play_song, name='play_song'),
    path('', home, name='home'),
    path('contact/', contact_view, name='contact'),
    path('success/', lambda request: render(request, 'success.html'), name='success'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
    path('edit_task/<int:task_id>/', edit_task, name='edit_task'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
