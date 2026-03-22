from rest_framework import serializers

class ResearchInputSerializer(serializers.Serializer):
    thesis = serializers.CharField(max_length=250)