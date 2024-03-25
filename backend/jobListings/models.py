import uuid
from django.conf import settings
from django.db import models
from django.utils.timesince import timesince
from account.models import User

class JobCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class JobAttachment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    document = models.FileField(upload_to='job_attachments')
    created_by = models.ForeignKey(User, related_name='job_attachments', on_delete=models.CASCADE)

    def get_document_url(self):
        if self.document:
            return settings.WEBSITE_URL + self.document.url
        else:
            return ''

class Job(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(JobCategory, on_delete=models.CASCADE)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    is_remote = models.BooleanField(default=False)
    attachments = models.ManyToManyField(JobAttachment, blank=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='jobs', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_at',)

    def created_at_formatted(self):
        return timesince(self.created_at)

class Job(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    salary = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    is_remote = models.BooleanField(default=False)
    duration = models.CharField(max_length=100)
    posted_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()

    categories = models.ManyToManyField(JobCategory, related_name='categories')
    attachments = models.ManyToManyField(JobAttachment, related_name='attachments', blank=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='jobs', on_delete=models.CASCADE)

    def __str__(self):
        return self.title