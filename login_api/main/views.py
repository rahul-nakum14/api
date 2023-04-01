from django.shortcuts import render

def index_view(request):
    return render(request, 'main/index.html')
# Create your views here.
def success_view(request):
    return render(request, 'main/success.html')