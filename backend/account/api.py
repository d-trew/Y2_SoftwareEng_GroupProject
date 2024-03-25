from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .forms import SignUpForm

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data = request.data
    message = 'You have signed up successfully'

    form = SignUpForm(data)
    if form.is_valid():
        form.save()

        # send verification email
    else:
        message = 'There was an error signing up'
    return JsonResponse({'status': message})