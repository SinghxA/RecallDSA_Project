from rest_framework import serializers
from .models import Problem




class ProblemSerializer(serializers.ModelSerializer):
    topic = serializers.CharField(source="topic.name", read_only=True)
    #   Is API field ke liye actual data kahan se lena hai?”     %%%%%%%%%%%   read_only=True ka matlab hai:Client is field ko GET mein read kar sakta hai, lekin POST/PUT ke through is particular serializer field ko directly write nahi kar sakta.
    class Meta:
        model=Problem
        fields = [
                "id",
                "title",
                "difficulty",
                "topic",
                "problem_url",
                "created_at",

        ]

        