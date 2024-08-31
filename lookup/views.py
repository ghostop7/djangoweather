from django.shortcuts import render
#this is my views.py file
def home (request):
	return render (request,'home.html',{})

def about(request):
    return render(request, 'about.html', {})