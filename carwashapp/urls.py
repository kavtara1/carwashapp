from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from carwashapp.views import branch_listing, branch_detail_view, washers_view

urlpatterns = [
    path('', branch_listing, name='branches_listing'),
    path('detail/<int:pk>/', branch_detail_view),
    path("washer/<int:pk>", washers_view )
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)