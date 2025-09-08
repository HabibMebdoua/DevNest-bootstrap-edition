from django.shortcuts import render

def index(request):
    return render(request , 'main/index.html')

def portfolio(request):
    return render(request, 'main/portfolio.html')