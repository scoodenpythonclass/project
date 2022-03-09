from django.shortcuts import render
from .forms import Feedbackform
# Create your views here.
def index(r):
    return render(r,'formapp/index.html')

def show(r):
    form =Feedbackform()
    if r.method =="POST":
        form = Feedbackform(r.POST)
        if form.is_valid():
            print(form.cleaned_data)

    return render(r,'formapp/studentfeedback.html', {'form':form})
