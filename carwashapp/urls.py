from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from carwashapp.views import branch_listing

urlpatterns = [
    path('', branch_listing, name='store_listing')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)