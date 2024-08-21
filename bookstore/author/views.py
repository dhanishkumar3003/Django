from django.shortcuts import render
from .models import author
from django.db.models import Avg
def AuthorList(request):
    auth = author.objects.all().order_by('first_name')
    authcount=auth.count()
    avgrating=auth.aggregate(Avg('rating'))
    return render(request,'author/index.html',{
        'authors':auth,
        'authcount':authcount,
        'avgrating':avgrating['rating__avg']
        })

def AuthorInfo(request,authid):
    auth = author.objects.get(id=authid)
    return render(request, 'author/authinfo.html', {'author': auth} )

def AuthorInfoSlug(request,authslug):
    auth = author.objects.get(slug=authslug)
    return render(request, 'author/authinfo.html', {'author': auth} )
