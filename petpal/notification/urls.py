from django.urls import path
from . import views

appname = 'notification'
urlpatterns = [
    path('creation/', views.create_notification, name='create-notification'),
    path('read/<int:notification_id>/', views.update_notification, name='update-notification'),
    path('list/', views.list_notifications, name='list-notifications'),
    path('details/<int:notification_id>/', views.get_notification, name='get-notification'),
    path('deletion/<int:notification_id>/', views.delete_notification, name='delete-notification'),
]