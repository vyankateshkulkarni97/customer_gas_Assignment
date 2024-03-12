# gas_utility_app/urls.py
from django.urls import path
from .views import submit_request, request_tracking , manage_account

urlpatterns = [
    path('submit_request/', submit_request, name='submit_request'),
    path('request_tracking/', request_tracking, name='request_tracking'),
    path('manage_account/', manage_account, name='manage_account'),

]
