from django.shortcuts import render

# Create your views here.
def homepageView(request):
    return render(request, 'homepage.html')

def basic_bootstrap(request):
    return render(request, 'partials\base.html', {})