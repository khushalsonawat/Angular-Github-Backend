from rest_framework import serializers


class RepositorySerializer(serializers.Serializer):
    title = serializers.CharField()
    url = serializers.CharField()
    topics = serializers.ListField(allow_empty=True)
    description = serializers.CharField(allow_blank=True)
