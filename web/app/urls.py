from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import AuthorizeView, HomePageView


urlpatterns = [
    path('authorize/', AuthorizeView.as_view(), name='authorize'),
    path('homepage', HomePageView.as_view(), name='home'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)