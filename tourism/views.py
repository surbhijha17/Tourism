from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from contact.forms import ContactForm
from places.models import Category,Article,Gallery
def homepage(request):
    categories=Category.objects.all()
    posts=Article.objects.all()
   
    if request.method=='POST':
    	form=ContactForm(request.POST )
    	if form.is_valid():
    		form.save()
    else:
    	form=ContactForm()

    return render(request,'home.html',{'posts':posts,'categories':categories,'form':form})
def about(request):
    #return HttpResponse('hey!!! this is surbhi ')
    return render(request,"about.html")

def gallery(request):
    
    articles=Article.objects.all()

    return render(request,"places/gallery.html",{'articles':articles})

def gallery_byplaces(request,pk):
    articles=get_object_or_404(Article,pk=pk)
    gallery=Gallery.objects.all().filter(articles=articles)
    return render(request,"places/gallery_byplaces.html",{'gallery':gallery,'articles':articles})
