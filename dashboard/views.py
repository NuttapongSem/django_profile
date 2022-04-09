from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Skill


# Create your views here.
def index(request):
    skill = Skill.objects.all()
    return render(request, "frontend/index.html", {'skills': skill})


def abouts(request):
    if request.POST:
        skillname = request.POST.get('skill_name')
        new_skill = Skill()
        new_skill.name_skill = skillname
        new_skill.save()
        print(skillname)
        return HttpResponseRedirect(reverse('abouts'))
    skill = Skill.objects.all()
    return render(request, "frontend/abouts.html", {'skills': skill})


def deleteSkil(request, id):
    data_skil = Skill.objects.get(id=id)
    data_skil.delete()
    return redirect("abouts")
    # return render(request, "frontend/abouts.html")
