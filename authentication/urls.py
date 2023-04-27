from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from authentication.views import RegisterView, ResetPassword, ResetPasswordAPI

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name='token_obtain'),
    path("token/refresh/", TokenRefreshView.as_view(), name='token_refresh'),
    path("token/verify/", TokenVerifyView.as_view(), name='token_verify'),
    path("register/", RegisterView.as_view(), name="registration"),
    path("password-reset/<str:encoded_pk>/<str:token>", ResetPasswordAPI.as_view(), name='reset_password_url'),
    path("resetting_password/", ResetPassword.as_view(), name='reset_password')
]
