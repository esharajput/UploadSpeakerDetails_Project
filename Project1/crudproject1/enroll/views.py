
from django.shortcuts import render, HttpResponseRedirect
from .forms import SpeakerRegistration
from .models import Speaker

# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm = SpeakerRegistration(request.POST)  
        if fm.is_valid():
         nm = fm.cleaned_data['name']
         em = fm.cleaned_data['email']
         pw = fm.cleaned_data['password']
         reg = Speaker(name=nm, email=em, password=pw)
         reg.save()
        fm = SpeakerRegistration()
    else:
        fm = SpeakerRegistration()  
    stud = Speaker.objects.all()   
    return render(request, 'enroll/addandshow.html', {'form':fm, 'stu':stud})
    
def update_data(request, id):    
    if request.method == 'POST':
        pi = Speaker.objects.get(pk=id)
        fm = SpeakerRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        else:
            pi = Speaker.objects.get(pk=id)
            fm = SpeakerRegistration(request.POST, instance=pi)

    return render(request, 'enroll/updatespeaker.html', {'id':id})

def delete_data(request, id):
        if request.method == 'POST':
            pi = Speaker.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/')

    