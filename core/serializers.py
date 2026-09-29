from rest_framework import serializers
from .models import Problem,Topic




class ProblemSerializer(serializers.ModelSerializer):
    topic_name = serializers.SlugRelatedField(
    source="topic",
    slug_field="name",
    queryset=Topic.objects.all(),
    write_only=True   #"DRF, is field ko input mein accept karo, lekin output mein mat bhejo."
)
    topic = serializers.CharField(source="topic.name", read_only=True)
    #   Is API field ke liye actual data kahan se lena hai?”     %%%%%%%%%%%   read_only=True ka matlab hai:Client is field ko GET mein read kar sakta hai, lekin POST/PUT ke through is particular serializer field ko directly write nahi kar sakta.
    class Meta:
        model=Problem
        fields = [
                "id",
                "title",
                "difficulty",
                "topic",
                "topic_name",
                "problem_url",
                "created_at",

        ]

