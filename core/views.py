from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Problem
from .serializers import ProblemSerializer


# def home(request):
#     return JsonResponse({
#         "message": "Welcome to RecallDSA!"
#     })

@api_view(["GET","POST"])
def problem_list(request):
    if request.method == "POST":
        serializer = ProblemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors,status=400)
        
    problems= Problem.objects.all()
    serializer = ProblemSerializer(problems,many=True)

    return Response(serializer.data)