from django.shortcuts import render
from .models import author

def AuthorList(request):
    authors=author.objects.all()
    return render(request,'author/index.html',{
        'authors':authors
        })
