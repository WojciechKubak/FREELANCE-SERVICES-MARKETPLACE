from .serializers import UserSerializer
from .models import User
from app.email import EmailService
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import datetime


class UserView(APIView):

    def post(self, request) -> Response:
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            EmailService.send_activation_link(
                username=serializer.data["username"], email=serializer.data["email"]
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActivateUserView(APIView):

    def get(self, request) -> Response:
        timestamp = float(request.query_params.get("timestamp"))
        if timestamp < datetime.datetime.now().timestamp() * 1000:
            return Response(
                {"message": "Activation link expired"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        username = request.query_params.get("username")
        user = User.objects.filter(username=username).first()

        if user:

            if user.is_active:
                return Response(
                    {"message": "User already activated"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            user.is_active = True
            user.save()
            return Response({"message": "User activated"}, status=status.HTTP_200_OK)

        return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
