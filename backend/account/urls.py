from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import api   

urlpatterns = [
    path('me/', api.me, name='me'),
    path('signup/', api.signup, name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('connections/<uuid:pk>/request/', api.send_connection_request, name='send_connection_request'),
    path('editprofile/', api.editprofile, name='edit_profile'),
    path('editpassword/', api.editpassword, name='edit_password'),
]
