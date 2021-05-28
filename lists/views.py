from typing import NewType
from lists.models import Item
from django.shortcuts import redirect, render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    if request.method =='POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
        
    Items=Item.objects.all()
    return render(request,'home.html',{'items':Items})
