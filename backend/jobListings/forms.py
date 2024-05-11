from django.forms import ModelForm

from .models import Job, JobAttachment


class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ('title','description','deadline')


class AttachmentForm(ModelForm):
    class Meta:
        model = JobAttachment
        fields = ('document',)