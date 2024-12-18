from django.contrib import admin
from django.urls import path, include, re_path # re_path = regular expresions
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path("admin/", admin.site.urls),
    path("", views.homepage),
    path("about/", views.about),
    # Look inside the posts app for the urls file:
    path("posts/", include("posts.urls")),
    path("users/", include("users.urls"))
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
