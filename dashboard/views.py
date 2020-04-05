from django.shortcuts import render

def index(request):
    
    template = "dashboard/index.html"
    context = {
        
    }
    return render(request, template, context)