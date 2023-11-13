from rest_framework import generics, permissions, status
from .models import Chat, Application
from .serializers import ChatSerializer, ApplicationStatusSerializer
from rest_framework.response import Response


class ApplicationDetailView(generics.RetrieveUpdateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationStatusSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_url_kwarg = 'application_id'


class ChatView(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        application_id = self.kwargs.get('application_id')
        return Chat.objects.filter(application__id=application_id)


class ApplicationStatusUpdateView(generics.UpdateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationStatusSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_url_kwarg = 'application_id'

    def perform_update(self, serializer):
        # Add logic for any additional processing after application status update
        serializer.save()
