from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def pagetest(request):
    return HttpResponse("<h1> this is a test </h1>")


def json_test(request):
    return JsonResponse({'name':'ali'})

def index_view(request):
    return render(request,'website/index.html')

def about_view(request):
    return render(request,'about.html')

def contact_view(request):
    return render(request,'contact.html')