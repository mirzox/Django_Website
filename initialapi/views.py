from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .serializers import UserSerializer
from .utils import SendMessageFromEmail, generate_password


class UserViewSetClass(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = (TokenAuthentication,)

    def list(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(data=serializer.data,
                        status=status.HTTP_200_OK)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    # def update(self, request, pk):
    #     user = get_object_or_404(User, pk=pk)
    #     serializer = NotebookModelSerializer(user, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({"request": "your data is updated"},
    #                         status=status.HTTP_200_OK)
    #     else:
    #         return Response({"request": "your data is not updated"},
    #                         status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        notebook = get_object_or_404(User, pk=pk)
        try:
            notebook.delete()
            data = {
                'request': 'Data successfully deleted'
            }
            return Response(data=data, status=status.HTTP_204_NO_CONTENT)
        except Exception:
            data = {
                'request': 'Oops Some thing went wrong'
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


class LoginView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        print(created)
        print(token)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        }, status=status.HTTP_201_CREATED)


class Logout(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response({'response': 'token deleted'}, status=status.HTTP_200_OK)


class SignUp(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SendSMS(APIView):
    def post(self, request):
        user = get_object_or_404(User, username=request.data.get('username'))
        sendmsg = SendMessageFromEmail(
            sender_email="forsettechbackend@gmail.com",
            sender_email_password='yzfjwqqjghkxqjix',
        )
        email = request.data.get('email')
        if user.email == email:
            password = generate_password(20)

            sendmsg.send_message(email,
                                 'This is test subject',
                                 'This message from python and your new password = {}'.format(password)
                                 )
            return Response({'request': "Your new password send to your email"})
        return Response({'request': "Your email is invalid"})


class ResetPassword(APIView):
    def post(self, request):
        pass


