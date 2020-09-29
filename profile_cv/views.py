from django.shortcuts import render

# Create your views here.
from profile_cv.models import Draco_Profile


def home_page(request):
    intro = Draco_Profile.objects.get(user=1)
    return render(request,'profile/home.html',{'intro': intro})
