from django.urls import path
from . import views

urlpatterns = [
    path('submit_request/', views.submit_request, name='submit_request'),
    path('track_requests/', views.track_requests, name='track_requests'),
    path('account_info/', views.account_info, name='account_info'),
]
