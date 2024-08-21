from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
def feedbackform(request):
    if request.method == 'POST': #True
        enter_username = request.POST['username']
        print(enter_username)
 
        if enter_username == "":
            return render(request,'userprofile/feedback.html',{
                'haserror':True
            })
 
        return HttpResponseRedirect('thankyou')
 
    return render(request,'user/feedback.html')
 
def thanku(request):
    return render(request,'user/thank_you.html')