
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('media/<str:path>/', 특정view_function),
    path('posts/', include('posts.urls')),
    path('', views.index),
    path('members/', include('members.urls')),

] + static(
    prefix=settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)
