from django.shortcuts import render

# Create your views here.

def index(request):
    #homepage for pizzas
    return render(request, 'pizzas/index.html')