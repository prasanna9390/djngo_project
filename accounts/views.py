from django.shortcuts import render
from accounts.forms import userform


# Create your views here.


def index(request):
    return render(request,'index.html')

def userreg(request):
    if request.method == 'POST':
        form=userform(request.POST)
        if form.is_valid():
            name=form.cleaned_data['first_name']
            print(name)
            # form.save()
            # print('<=====================>',)
           
    form=userform()
    return render(request,'userreg.html',{'form':form})
