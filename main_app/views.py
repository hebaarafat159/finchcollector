from django.shortcuts import render

from .models import Finch
# Create your views here.
# finchs = [
#   {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
#   {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
# ]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finchs_index(request):
    finchs = Finch.objects.all()
    return render(request, 'finchs/index.html',{
        'finchs': finchs
    })

def finchs_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  return render(request, 'finchs/detail.html', { 'finch':finch})