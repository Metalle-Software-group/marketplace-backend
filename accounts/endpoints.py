from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import  generics, status,views, permissions as pm
from rest_framework.response import Response
from django.contrib.auth import authenticate
from accounts.models import CustomUser
from rest_framework import status
from accounts import permissions

from accounts.serializers import UserSerializer

class LoginView(views.APIView):
    def post(self, request):
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
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminOrUnAthenticatedUser]

# Create your views here.
class UserListRetrieveView(generics.ListCreateAPIView, generics.RetrieveUpdateAPIView):
    permission_classes = [
        permissions.IsAdminOrUserSelf
        # pm.IsAuthenticated
        ]

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"