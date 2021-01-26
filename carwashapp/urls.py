from django.urls import path

from carwashapp.views import branch_listing

urlpatterns = [
    path('', branch_listing, name='store_listing')

]