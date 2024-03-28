from django.conf import settings
from django.http import JsonResponse
from django.core.mail import send_mail
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import User, ConnectionRequest
# from notification.utils import create_notification
from .forms import SignUpForm

@api_view(['GET'])
def me(request):
    return JsonResponse({
        'id': request.user.id,
        'name': request.user.name,
        'email': request.user.email,
        'avatar': request.user.get_avatar()
    })

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data = request.data
    message = 'success'

    form = SignUpForm({
        'email': data.get('email'),
        'name': data.get('name'),
        'password1': data.get('password1'),
        'password2': data.get('password2'),
    })

    if form.is_valid():
        user = form.save()
        user.is_active = False
        user.save()

        url = f'{settings.WEBSITE_URL}/activateemail/?email={user.email}&id={user.id}'

        send_mail(
            "Please verify your email",
            f"The url for activating your account is: {url}",
            "noreply@wey.com",
            [user.email],
            fail_silently=False,
        )
    else:
        message = form.errors.as_json()
    
    print(message)

    return JsonResponse({'message': message}, safe=False)

@api_view(['POST'])
def send_connection_request(request, pk):
    user = User.objects.get(pk=pk)

    check1 = ConnectionRequest.objects.filter(created_for=request.user).filter(created_by=user)
    check2 = ConnectionRequest.objects.filter(created_for=user).filter(created_by=request.user)

    if not check1 or not check2:
        friendrequest = ConnectionRequest.objects.create(created_for=user, created_by=request.user)

        # notification = create_notification(request, 'new_friendrequest', friendrequest_id=friendrequest.id)

        return JsonResponse({'message': 'connection request created'})
    else:
        return JsonResponse({'message': 'request already sent'})
