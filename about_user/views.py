from django.http.response import HttpResponse
from django.shortcuts import render
# Create your views here.
def about(request):
    return render(request, "frontend/form_about.html")