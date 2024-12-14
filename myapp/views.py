from django.shortcuts import render,redirect
from .forms import PersonForm
from .models import Person

# Create your views here.
def Personview(request):
    if request.method=='POST':
        form=PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form=PersonForm()
    return render(request,'person.html',{'form':form})

def user_list(request):
    users=Person.objects.all()
    return render(request,'user_list.html',{'users': users})
