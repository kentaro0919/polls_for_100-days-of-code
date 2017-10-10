from django.shortcuts import render

def index(request):
    context = {"text": "text"}
    return render(request, "polls/index.html", context)
