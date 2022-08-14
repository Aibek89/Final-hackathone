from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView

from account.serializers import RegisterSerializer, LoginSerializer, ForgotPasswordSerializer, \
    ForgotPasswordCompleteSerializer

User = get_user_model()

class RegisterApiView(APIView):
    def post(self, request):
        data = request.data
        serializers = RegisterSerializer(data=data)

        if serializers.is_valid(raise_exception=True):
            serializers.save()
            message = f'Вы успешно зарегистрированы, вам отправлено письмо на почту!'
            return Response(message, status=201)


class ActivationApiView(APIView):
    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response({'msg': 'Успешно!'})
        except User.DoesNotExist:
            return Response({'msg': 'Неверный код'})


class LoginApiView(ObtainAuthToken):
    serializer_class = LoginSerializer


class ForgotPasswordView(APIView):
    def post(self, request):
        data = request.data
        serializer = ForgotPasswordSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.send_code()
        return Response('Вам отправлено письмо для восстановления пароля!')


class ForgotPasswordComplete(APIView):
    def post(self, request):
        data = request.data
        serializer = ForgotPasswordCompleteSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.set_new_pass()
        return Response('Пароль успешно обновлен!')

