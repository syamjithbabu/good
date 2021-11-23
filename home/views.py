from django.shortcuts import render

# Create your views here.

def Grand(request):
    return render(request, 'dream.html')

def Free(request):
    return render(request, 'form.html')    
