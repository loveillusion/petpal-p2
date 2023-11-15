from django.urls import path
from .views import ApplicationDetailView, ChatView, ApplicationStatusUpdateView, ChatCreateView, ShelterViewSeekerProfile
from .views import ApplicationListView

appname = 'application'
urlpatterns = [
    path('<int:application_id>/detail/', ApplicationDetailView.as_view(), name='application_detail'),
    path('<int:application_id>/chats/', ChatView.as_view(), name='application_chat'),
    path('<int:application_id>/message/', ChatCreateView.as_view(), name='application_send'),
    path('<int:application_id>/status/', ApplicationStatusUpdateView.as_view(), name='application_status'),
    path('<int:application_id>/profile/', ShelterViewSeekerProfile.as_view(), name='view_seeker'),
    path('all/<int:shelter_id>/', ApplicationListView.as_view(), name='all_applications')

]
