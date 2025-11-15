from django.shortcuts import render

# Create your views here.

# Home Page 
def home(request):
    return render(request, 'main/home.html')

# About Page 
def about(request):
    return render(request, 'main/about.html')

# Portfolio Page 
def portfolio(request):
    return render(request, 'main/portfolio.html')

# Contact Page 
def contact(request):
    return render(request, 'main/contact.html')
# blog Page 
def blog(request):
    return render(request, 'main/blog.html')