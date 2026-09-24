from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Problem
from .serializers import ProblemSerializer


# def home(request):
#     return JsonResponse({
#         "message": "Welcome to RecallDSA!"
#     })

@api_view(["GET"])
def problem_list(request):
    problems= Problem.objects.all()
    serializer = ProblemSerializer(problems,many=True)

    return Response(serializer.data)