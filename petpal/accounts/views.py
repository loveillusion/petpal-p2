from django.contrib.auth import authenticate
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, Seeker, Shelter
from .serializers import UserSerializer, SeekerSerializer, ShelterSerializer
from .serializers import UserLoginSerializer, EditProfileSerializer
from django.core.exceptions import ValidationError


# =================SEEKER VIEWS=================
class SeekerRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.is_seeker = True
        user.save()
        seeker = Seeker(user=user)
        seeker.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SeekerLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=serializer.validated_data['username'],
                            password=serializer.validated_data['password'])
        if user is not None and user.is_seeker:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Username or password is invalid"}, status=status.HTTP_401_UNAUTHORIZED)


class SeekerProfileView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SeekerSerializer

    def get_object(self):
        return Seeker.objects.get(user=self.request.user)


class SeekerEditProfileView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EditProfileSerializer

    def get_object(self):
        return self.request.user.seeker


class SeekerUploadProfilePictureView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SeekerSerializer

    def get_object(self):
        return Seeker.objects.get(user=self.request.user)


# =================SHELTER VIEWS=================
class ShelterRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.is_shelter = True
        user.save()
        shelter = Shelter(user=user)
        shelter.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ShelterLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=serializer.validated_data['username'],
                            password=serializer.validated_data['password'])
        if user is not None and user.is_shelter:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Username or password is invalid"}, status=status.HTTP_401_UNAUTHORIZED)


class ShelterProfileView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ShelterSerializer

    def get_object(self):
        return Shelter.objects.get(user=self.request.user)


class ShelterEditProfileView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EditProfileSerializer

    def get_object(self):
        return self.request.user.shelter


class ShelterUploadProfilePictureView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ShelterSerializer

    def get_object(self):
        return Shelter.objects.get(user=self.request.user)
