from rest_framework import serializers
from . import models


class AthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Athlete
        fields = ("id", "name", "last_name", "is_male", "birth_date")


class CompleteInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CompleteInfo
        fields = "__all__"


class BodySizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BodySize
        fields = "__all__"


class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Disease
        fields = "__all__"


class PracticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Athlete
        fields = "__all__"
