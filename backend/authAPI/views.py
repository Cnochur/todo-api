from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer


from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def auth_login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)

        return Response({
            "id": user.id,
            "username": user.username
        }, status=200)

    return Response({"error": "Invalid credentials"}, status=400)



@api_view(['POST'])
@permission_classes([AllowAny])
def auth_register(request):
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        user = User.objects.create_user(
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"]
        )

        login(request, user)

        return Response({
            "id": user.id,
            "username": user.username
        }, status=201)

    return Response(serializer.errors, status=400)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def auth_logout(request):
    logout(request)
    return Response({"message": "Logged out"}, status=200)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def me(request):
    return Response({
        "id": request.user.id,
        "username": request.user.username
    })