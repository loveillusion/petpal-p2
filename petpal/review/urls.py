from django.urls import path
from .views import ReviewCreateView, ReviewListView


urlpatterns = [
    path('create/', ReviewCreateView.as_view(), name='create_review'),
    path('<str:model_type>/<int:object_id>/', ReviewListView.as_view(), name='list_reviews'),
]
