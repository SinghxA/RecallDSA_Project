# from django.http import HttpResponse
# We're importing Django's tool for creating an HTTP response.
# def home(request):
#     return HttpResponse("Welcome to RecallDSA!")

# /////////////////////////////////////////////////


from django.http import JsonResponse


def home(request):
    return JsonResponse({
        "message": "Welcome to RecallDSA!"
    })