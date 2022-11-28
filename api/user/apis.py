from rest_framework import views, response, exceptions, permissions

from user import serializer as user_serializer
from .services import create_user, user_email_selector, create_token
from .authentication import CustomUserAuthentication


class RegisterApi(views.APIView):
    """
    Register Input api/register/
    {
        "first_name": "Helton",
        "last_name": "Teixeira",
        "email": "heltonteixeiradesouza@hotmail.com",
        "password": "123@mudar"
    }

    """

    def post(self, request):
        serializer = user_serializer.UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        serializer.instance = create_user(user_dc=data)

        return response.Response(data=serializer.data)


class LoginApi(views.APIView):
    """
    Login Input api/login/
    {
    "email": "heltonteixeiradesouza@hotmail.com",
     "password": "123@mudar"
    }
    """

    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]

        user = user_email_selector(email)

        if user is None:
            raise exceptions.AuthenticationFailed("Invalid Credentials")

        if not user.check_password(raw_password=password):
            raise exceptions.AuthenticationFailed("Invalid Credentials")

        token = create_token(user_id=user.pk)

        resp = response.Response()

        resp.set_cookie(key="jwt", value=token, httponly=True)

        return resp


class UserAPI(views.APIView):
    """
    api/me
    this endpoint can only be used
    if user is authenticated
    """

    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user

        serializer = user_serializer.UserSerializer(user)

        return response.Response(serializer.data)


class LogoutApi(views.APIView):
    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        resp = response.Response()
        resp.delete_cookie("jwt")
        resp.data = {"message": "so long farewall"}

        return resp
