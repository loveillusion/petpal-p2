from django.urls import path
from .views import ShelterReviewListView, ShelterReviewCreateView, ApplicationReviewListView, ApplicationReviewCreateView


appname = 'reviews'
urlpatterns = [
    path('shelter/<int:shelter_id>/', ShelterReviewListView.as_view(), name='shelter_reviews'),
    path('shelter/<int:shelter_id>/new/', ShelterReviewCreateView.as_view(), name='new_shelter_review'),
    path('application/<int:application_id>/', ApplicationReviewListView.as_view(), name='application_reviews'),
    path('application/<int:application_id>/new/', ApplicationReviewCreateView.as_view(), name='new_application_review'),
]
