from WhyTheName.ORMClasses.BasicContentModel import *
from rest_framework import serializers


class ContentSerializer(serializers.Serializer):
    searchText = serializers.CharField()
    whyTheName = serializers.CharField()

    def create(self, validated_data):
        return Content(searchText=validated_data.get('searchText'), whyTheName=validated_data.get('whyTheName'))

    def update(self, instance, validated_data):
        instance.title = validated_data.get('searchText', instance.searchText)
        instance.code = validated_data.get('whyTheName', instance.whyTheName)
        instance.save()
        return instance
