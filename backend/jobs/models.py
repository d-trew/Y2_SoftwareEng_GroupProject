import uuid

from django.db import models

from account.models import User

class Job(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    company_name = models.CharField(max_length=200)
    company_logo = models.ImageField(upload_to='company_logos/', null=True, blank=True)
    location = models.CharField(max_length=200)
    type = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    posted_date = models.DateTimeField(auto_now_add=True)