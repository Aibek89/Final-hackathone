from django.urls import path

from account.views import RegisterApiView, ActivationApiView, LoginApiView, ForgotPasswordView, ForgotPasswordComplete

urlpatterns = [
    path('register/', RegisterApiView.as_view()),
    path('active/<uuid:activation_code>/', ActivationApiView.as_view()),
    path('login/', LoginApiView.as_view()),
    path('forgot_password/', ForgotPasswordView.as_view()),
    path('forgot_password_confirm/', ForgotPasswordComplete.as_view()),
]