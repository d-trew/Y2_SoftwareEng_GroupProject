from rest_framework import serializers
from .models import JobCategory, JobAttachment, Job

from account.serializers import UserSerializer

class JobCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields = ['id', 'name']

class JobAttachmentSerializer(serializers.ModelSerializer):
    document_url = serializers.SerializerMethodField()

    class Meta:
        model = JobAttachment
        fields = ['id', 'document', 'document_url']

    def get_document_url(self, obj):
        if obj.document:
            return obj.get_document_url()
        return None

class JobSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    categories = JobCategorySerializer(many=True)
    attachments = JobAttachmentSerializer(many=True)

    class Meta:
        model = Job
        fields = ['id', 'title', 'description', 'salary', 'company', 'location', 'is_remote', 'duration', 'posted_at', 'deadline', 'categories', 'attachments', 'is_active', 'created_at', 'created_by']
        read_only_fields = ['posted_at', 'created_at', 'created_by']
