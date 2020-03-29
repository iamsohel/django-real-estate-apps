from django.urls import path

from .views import ListingAPIView, RealtorAPIView

urlpatterns = [
    path('', RealtorAPIView.as_view()),
    path('listings/', ListingAPIView.as_view()),
]