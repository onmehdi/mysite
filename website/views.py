from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from website.models import Person
from website.forms import NameForm, ContactForm, NewsletterForms

def pagetest(request):
    return HttpResponse("<h1> this is a test </h1>")


def json_test(request):
    return JsonResponse({'name':'ali'})

def index_view(request):
    return render(request,'website/index.html')
    

def about_view(request):
    return render(request,'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
       
    form = ContactForm()
    return render(request,'website/contact.html',{'form':form})

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
            
       

def test_view(request):
    return render(request,'website/test.html',{'firstname':'ali','lastname':'rezaei'})

def index1_view(request):
    return render(request,'website/index1.html')


def test1_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # name = form.cleaned_data['name']
            # email = form.cleaned_data['email']
            # subject = form.cleaned_data['subject']
            # message = form.cleaned_data['message']
            # print(name, email, message)
            return HttpResponse('Done')
        else:
            return HttpResponse('not valid')

        
    form = ContactForm()
    return render(request,'website/test1.html',{'form':form})
