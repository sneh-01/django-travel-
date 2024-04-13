from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):

    return render(request,'index.html')


def aboutUs(request):
    return HttpResponse("<b>welcome to mysite.</b>")

def course(request):
    return HttpResponse("welcome to my course.")

def courseDetails(request, courseId):
    return HttpResponse(courseId)

# coursedetails function or kyay pan coursedetails par click karish to mane course id return thase and eni url ma b course id j hase.
# in shoer all is lese apse and url coursedetails it just func. show id thse.
    

# it is all about request and response.aboutus
