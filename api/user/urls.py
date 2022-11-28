from django.urls import path
from user.apis import RegisterApi, LoginApi, UserAPI, LogoutApi

urlpatterns = [
    path("register/", RegisterApi.as_view(), name="register"),
    path("login/", LoginApi.as_view(), name="Login"),
    path("me/", UserAPI.as_view(), name="me"),
    path("logout/", LogoutApi.as_view(), name="logout"),
]
