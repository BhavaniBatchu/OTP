from django.shortcuts import render
from . forms import AadharForm
import random
# Create your views here.
def index(request):
    otp = random.randint(100000,999999)
    form = AadharForm()
    if request.method =="POST":
       form = AadharForm(request.POST,request.FILES)
       if form.is_valid():
          receiver_mail = form.cleaned_data['mail']
          form.save()
          print("added successfuly")

    return render(request,'index.html', {'form':form})