from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import LoginView, Logout, SignUp, UserViewSetClass, SendSMS, ResetPassword

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('logout/', Logout.as_view()),
    path('signup/', SignUp.as_view()),
    path('resetpassword/', SendSMS.as_view()),
    path('confirmcode/', ResetPassword.as_view())
]

router = DefaultRouter()
router.register('user', UserViewSetClass, basename='viewsetclass')

urlpatterns += [
    path('', include(router.urls))
]