from .models import Notification

from jobListings.models import Job
from account.models import ConnectionRequest

# create_notification(request, 'post_like', 'lskjf-j12l3-jlas-jdfa', 'lskjf-j12l3-jlas-jdfa')


def create_notification(request, type_of_notification, post_id=None, connectionrequest_id=None):
    created_for = None

    if type_of_notification == 'post_like':
        body = f'{request.user.name} liked one of your posts!'
        post = Job.objects.get(pk=post_id)
        created_for = post.created_by
    elif type_of_notification == 'new_connectionrequest':
        connectionrequest = ConnectionRequest.objects.get(pk=connectionrequest_id)
        created_for = connectionrequest.created_for
        body = f'{request.user.name} sent you a connection request!'
    elif type_of_notification == 'accepted_connectionrequest':
        connectionrequest = ConnectionRequest.objects.get(pk=connectionrequest_id)
        created_for = connectionrequest.created_for
        body = f'{request.user.name} accepted your connection request!'
    elif type_of_notification == 'rejected_connectionrequest':
        connectionrequest = ConnectionRequest.objects.get(pk=connectionrequest_id)
        created_for = connectionrequest.created_for
        body = f'{request.user.name} rejected your connection request!'

    notification = Notification.objects.create(
        body=body,
        type_of_notification=type_of_notification,
        created_by=request.user,
        post_id=post_id,
        created_for=created_for
    )

    return notification