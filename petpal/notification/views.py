from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .serializers import NotificationCreateSerializer, NotificationSerializer
from .models import Notification
from accounts.models import User
from django.core import serializers
from django.contrib.contenttypes.models import ContentType


@api_view(['POST'])
def create_notification(request):
    if request.method == 'POST':
        serializer = NotificationCreateSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data

            user_id = validated_data['user_id']
            message = validated_data['message']
            content_type_str = validated_data['content_type']
            object_id = validated_data['object_id']

            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                return Response({'error': 'User does not exist'}, status=400)

            try:
                content_type = ContentType.objects.get(model=content_type_str)
            except ContentType.DoesNotExist:
                return Response({'error': 'Invalid content type'}, status=400)

            notification = Notification.objects.create(
                user=user,
                message=message,
                read=False,
                timestamp=timezone.now(),
                content_type=content_type,
                object_id=object_id
            )

            return Response({'success': 'Notification created successfully', 'notification_id': notification.id})

        return Response(serializer.errors, status=400)

    return Response({'error': 'Invalid request method'}, status=405)


@api_view(['PUT'])
def update_notification(request, notification_id):
    try:
        notification = Notification.objects.get(pk=notification_id)
    except Notification.DoesNotExist:
        return Response({'error': 'Notification not found'}, status=404)

    # Mark the notification as read
    notification.read = True
    notification.save()

    return Response({'success': 'Notification marked as read'})


@api_view(['GET'])
def list_notifications(request):
    user = request.user

    if user.is_authenticated:
        notifications = Notification.objects.filter(user=user)

        notifications = notifications.order_by('-timestamp')

        # Filter notifications by read/unread
        is_read = request.GET.get('read')
        if is_read is not None:
            is_read = is_read.lower() == 'true'
            notifications = notifications.filter(read=is_read)

        # Pagination support
        paginator = PageNumberPagination()
        paginator.page_size = 10  # Number of notifications per page
        paginated_notifications = paginator.paginate_queryset(notifications, request)
        serialized_notifications = NotificationSerializer(paginated_notifications, many=True).data

        return paginator.get_paginated_response(serialized_notifications)

    return Response({'error': 'User is not authenticated'}, status=401)


@api_view(['DELETE'])
def delete_notification(request, notification_id):
    try:
        notification = Notification.objects.get(pk=notification_id)
    except Notification.DoesNotExist:
        return Response({'error': 'Notification not found'}, status=404)

    notification.delete()

    return Response({'success': 'Notification deleted'})

