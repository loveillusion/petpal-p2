from django.urls import path
from . import views

appname = 'notification'
urlpatterns = [
    path('create/', views.create_notification, name='create-notification'),
    path('update/<int:notification_id>/', views.update_notification, name='update-notification'),
    path('list/', views.list_notifications, name='list-notifications'),
    path('delete/<int:notification_id>/', views.delete_notification, name='delete-notification'),
]