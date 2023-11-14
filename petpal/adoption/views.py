from rest_framework import generics, permissions, status
from .models import Chat, Application
from .serializers import ChatSerializer, ApplicationDetailSerializer, ApplicationUpdateSerializer, ChatCreateSerializer
from rest_framework.response import Response


class ApplicationDetailView(generics.RetrieveAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_url_kwarg = 'application_id'


class ChatView(generics.ListAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        application_id = self.kwargs.get('application_id')
        return Chat.objects.filter(application__id=application_id)


class ChatCreateView(generics.CreateAPIView):
    serializer_class = ChatCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        application_id = self.kwargs.get('application_id')
        application = Application.objects.get(id=application_id)
        sender = self.request.user
        serializer.save(application=application, sender=sender)


class ApplicationStatusUpdateView(generics.UpdateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_url_kwarg = 'application_id'

    def perform_update(self, serializer):
        serializer.save()
