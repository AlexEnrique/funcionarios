from django.db import IntegrityError
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import CreateAPIView, DestroyAPIView

from rest_framework.authtoken.models import Token

from .serializers import LoginSerializer, EnterpriseSerializer, RegisterSerializer
from .models import Enterprise, User
from .permissions import IsPostRequest


class UserView(CreateAPIView, DestroyAPIView):

    permission_classes = [IsPostRequest | IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            user: User = User.objects.create(
                username=serializer.data["email"],
                email=serializer.data["email"],
            )

            user.set_password(serializer.data["senha"])
            user.save()

            enterprise = Enterprise.objects.create(
                user=user,
                empresa=serializer.data["empresa"],
            )

        except IntegrityError:
            return Response({
                "mensagem": "Um usuário com este email já existe",
            }, status=409)

        token = Token.objects.create(user=user)

        return Response({
            "mensagem": "Usuário criado com sucesso",
            "usuario": EnterpriseSerializer(enterprise).data,
            "token": token.key,
        })

    def delete(self, request, *args, **kwargs):
        token: Token = request.auth
        token.user.delete()

        return Response({
            "mensagem": "Usuário deletado com sucesso",
        })

@api_view(["POST"])
@permission_classes([AllowAny])
def login(request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    try:
        user: User = User.objects.get(username=serializer.data["email"])
        if not user.check_password(serializer.data["senha"]):
            raise ValueError

    except (User.DoesNotExist, ValueError):
        return Response({
            "mensagem": "Usuário e/ou senha inválidos"
        }, status=401)

    token, _ = Token.objects.get_or_create(user=user)

    return Response({
        "mensagem": "Login efetuado com sucesso",
        "token": token.key,
    })


@api_view(["POST"])
def logout(request: Request):
    token: Token = request.auth
    token.delete()

    return Response({
        "mensagem": "Logout realizado com sucesso",
    })
