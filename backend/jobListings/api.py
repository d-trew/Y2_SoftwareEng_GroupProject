from django.db.models import Q
from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from account.models import User, connectionRequest
from account.serializers import UserSerializer
# from notification.utils import create_notification

from .forms import JobForm, AttachmentForm
from .models import Job,JobAttachment,JobCategory
from .serializers import JobSerializer,JobCategorySerializer


@api_view(['GET'])
def job_list(request):
    user_ids = [request.user.id]

    for user in request.user.friends.all():
        user_ids.append(user.id)

    jobs = Job.objects.filter(created_by_id__in=list(user_ids))

    trend = request.GET.get('trend', '')

    if trend:
        jobs = jobs.filter(body__icontains='#' + trend).filter(is_private=False)

    serializer = JobSerializer(jobs, many=True)

    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def job_detail(request, pk):
    user_ids = [request.user.id]

    for user in request.user.friends.all():
        user_ids.append(user.id)

    job = job.objects.filter(Q(created_by_id__in=list(user_ids)) | Q(is_private=False)).get(pk=pk)

    return JsonResponse({
        'job': JobCategorySerializer(job).data
    })


@api_view(['GET'])
def job_list_profile(request, id):   
    user = User.objects.get(pk=id)
    jobs = Job.objects.filter(created_by_id=id)

    if not request.user in user.friends.all():
        jobs = jobs.filter(is_private=False)

    jobs_serializer = JobSerializer(jobs, many=True)
    user_serializer = UserSerializer(user)

    can_send_connection_request = True

    if request.user in user.friends.all():
        can_send_connection_request = False
    
    check1 = connectionRequest.objects.filter(created_for=request.user).filter(created_by=user)
    check2 = connectionRequest.objects.filter(created_for=user).filter(created_by=request.user)

    if check1 or check2:
        can_send_connection_request = False

    return JsonResponse({
        'jobs': jobs_serializer.data,
        'user': user_serializer.data,
        'can_send_connection_request': can_send_connection_request
    }, safe=False)


@api_view(['job'])
def job_create(request):
    form = JobForm(request.job)
    attachment = None
    attachment_form = AttachmentForm(request.job, request.FILES)

    if attachment_form.is_valid():
        attachment = attachment_form.save(commit=False)
        attachment.created_by = request.user
        attachment.save()

    if form.is_valid():
        job = form.save(commit=False)
        job.created_by = request.user
        job.save()

        if attachment:
            job.attachments.add(attachment)

        user = request.user
        user.jobs_count = user.jobs_count + 1
        user.save()

        serializer = JobSerializer(job)

        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'error': 'add somehting here later!...'})
    

@api_view(['DELETE'])
def job_delete(request, pk):
    job = job.objects.filter(created_by=request.user).get(pk=pk)
    job.delete()

    return JsonResponse({'message': 'job deleted'})


@api_view(['job'])
def job_report(request, pk):
    job = job.objects.get(pk=pk)
    job.reported_by_users.add(request.user)
    job.save()

    return JsonResponse({'message': 'job reported'})
