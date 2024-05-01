from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import  generics, status,viewsets
from rest_framework.response import Response
from accounts.serializers import UserSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
from accounts.models import CustomUser
from rest_framework import status

class LoginView(ObtainAuthToken):
    view_permissions = {
        "post": {"admin": True, "anon": True},
        "options": {"any": True},
    }

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        if username is None or password is None:
            return Response({'error': 'Username and password are required'}, status=status.HTTP_401_UNAUTHORIZED)

        user = authenticate(username=username, password=password)
        if user is not None:
            # Use Django's built-in login function if session authentication is desired
            # login(request, user)  # Uncomment for session-based authentication

            # Generate a JSON Web Token (JWT) for token-based authentication (recommended)
            refresh = RefreshToken.for_user(user)

            return Response({"refresh": str(refresh), 'access': str(refresh.access_token)}, status=status.HTTP_200_OK)

        else:
            return Response({'error': 'Invalid credentials provided'}, status=status.HTTP_401_UNAUTHORIZED)

class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    view_permissions = {
        "post": {"admin": True, "anon": True},
        "options": {"any": True},
    }

    def perform_create(self, serializer):
        user = serializer.save()
        user_group, _ = Group.objects.get_or_create(name="customer")
        user.groups.add(user_group)


# Create your views here.
class UserListRetrieveView(viewsets.GenericViewSet,generics.ListAPIView, generics.RetrieveUpdateAPIView):
    view_permissions = {
        "put": {"user": True, "admin_or_owner": True},
        "options": {"any": True},
        "patch": {"user": True},
        "get": {"admin": True},
    }

    queryset = CustomUser.objects.filter(vendor__isnull = True)
    serializer_class = UserSerializer
    lookup_field = "pk"

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class UserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    view_permissions = {
        "get": {"admin": True},
        "options": {"any": True},
    }


class UserRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    view_permissions = {
        "put": {"user": True, "admin_or_owner": True},
        "delete" : {"admin_or_owner": True},
        "patch": {"admin_or_owner": True},
        "get": {"admin_or_owner": True},
        "options": {"any": True},
    }


    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)