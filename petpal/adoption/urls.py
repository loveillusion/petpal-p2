from django.urls import path
from .views import ApplicationDetailView, ChatView, ApplicationStatusUpdateView


appname = 'application'
urlpatterns = [
    path('<int:application_id>/detail/', ApplicationDetailView.as_view(), name='application_detail'),
    path('<int:application_id>/', ChatView.as_view(), name='application_chat'),
    path('<int:application_id>/status/', ApplicationStatusUpdateView.as_view(), name='application_status'),
]
