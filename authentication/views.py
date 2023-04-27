from rest_framework import generics
from rest_framework.permissions import AllowAny
from authentication.serializers import EmailSerializer, ResetPasswordSerializer, RegisterSerializer
from users.models import UserCar
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.urls import reverse
from rest_framework import response, status


class RegisterView(generics.CreateAPIView):
    queryset = UserCar.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class ResetPassword(generics.GenericAPIView):
    serializer_class = EmailSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data["email"]
        user = UserCar.objects.filter(email=email).first()
        if user:
            encoded_pk = urlsafe_base64_encode(force_bytes(user.pk))
            token = PasswordResetTokenGenerator().make_token(user)
            reset_url = reverse("reset_password_url",
                                kwargs={"encoded_pk": encoded_pk, "token": token})
            reset_url = f"0.0.0.0:8000{reset_url}"
            return response.Response(
                {
                    "message": f"Your password reset link: {reset_url}"
                },
                status=status.HTTP_200_OK
            )
        else:
            return response.Response(
                {"message": "User does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )


class ResetPasswordAPI(generics.GenericAPIView):
    """
    Verify and Reset Password Token View.
    """

    serializer_class = ResetPasswordSerializer

    def patch(self, request, *args, **kwargs):
        """
        Verify token & encoded_pk and then reset the password.
        """
        serializer = self.serializer_class(
            data=request.data, context={"kwargs": kwargs}
        )
        serializer.is_valid(raise_exception=True)
        return response.Response(
            {"message": "Password reset complete"},
            status=status.HTTP_200_OK,
        )
