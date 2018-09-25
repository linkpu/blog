from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request, 'foreground/index.html')

def gallery(request):

    return render(request, 'foreground/share.html')

def diary(request):

    return render(request, 'foreground/list.html')

def about(request):

    return render(request, 'foreground/about.html')

def message(request):

    return render(request, 'foreground/gbook.html')

def info(request):

    return render(request, 'foreground/info.html')

def infopic(request):

    return render(request, 'foreground/infopic.html')


def test(request):

    return render(request, 'foreground/test.html')