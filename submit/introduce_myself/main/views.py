from django.shortcuts import render

# Create your views here.
def mainpage(request):
    return render(request, 'main/mainpage.html')

def About_me(request):
    return render(request, 'main/About_me.html')

def notion(request):
    return render(request, 'main/notion.html')

def talking(request):
    return render(request, 'main/talking.html')