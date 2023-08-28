from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserSerializer, LoginSerializer, TokenSerializer, RegistrationSerializer
from .models import CustomUser
from .permissions import IsClientUser, IsAdminUser

@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user:
                refresh = RefreshToken.for_user(user)
                access_token = refresh.access_token
                return Response({
                    'access_token': str(access_token),
                    'refresh_token': str(refresh),
                })
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientAccess(APIView):
    permission_classes = (IsAuthenticated, IsClientUser)

    def get(self, request):
        return Response({'message': 'Client access granted.'})

class AdminAccess(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)

    def get(self, request):
        return Response({'message': 'Admin access granted.'})
        

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



