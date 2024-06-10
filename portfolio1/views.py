from django.shortcuts import render
from .models import Intro, MeByMe,TechPresentation,allApp,HandsOnDjango, Visita

def intro_view(request):
    intros = Intro.objects.first()
    return render(request, 'portfolio1/intro.html', {'intros': intros})

def mebyme_detail(request):
    mebymes = MeByMe.objects.all()  # Retrieve all MeByMe instances
    return render(request, 'portfolio1/aboutMe.html', {'mebymes': mebymes})



def tech_presentation(request):
    presentation = TechPresentation.objects.first()
    return render(request, 'portfolio1/Techpresentation.html', {'presentation': presentation})


def allApp_view(request):
    images = allApp.objects.all()
    return render(request, 'portfolio1/allApp.html', {'images': images})




def video_view(request):
    hands_on_django_videos = HandsOnDjango.objects.all()
    visita_videos = Visita.objects.all()
    return render(request, 'portfolio1/video.html', {
        'hands_on_django_videos': hands_on_django_videos,
        'visita_videos': visita_videos,
    })







