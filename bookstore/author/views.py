from django.shortcuts import render, get_object_or_404
from .models import author

def AuthorList(request):
    return render(request,'author/index.html',{
        'authors':author.objects.all()
        })
def AuthorInfo(request,authid):
    auth = author.objects.get(id=authid)
    return render(request, 'author/id.html', {'author': auth} )
def AuthorInfoSlug(request,authslug):
    auth = author.objects.get(slug=authslug)
    return render(request, 'author/id.html', {'author': auth} )