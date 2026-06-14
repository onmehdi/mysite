from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from website.models import Person

def pagetest(request):
    return HttpResponse("<h1> this is a test </h1>")


def json_test(request):
    return JsonResponse({'name':'ali'})

def index_view(request):
    return render(request,'website/index.html')
    

def about_view(request):
    return render(request,'website/about.html')

def contact_view(request):
    return render(request,'website/contact.html')

def test_view(request):
    return render(request,'website/test.html',{'firstname':'ali','lastname':'rezaei'})

def index1_view(request):
    return render(request,'website/index1.html')

def test1_view(request):
    people = Person.objects.all()
    context = {'people' : people}
    return render(request,'website/test1.html',context)
