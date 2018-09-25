from django.core.files import File
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
from users.models import Articles


def login(request):
    if request.method == 'POST':
        return render(request, 'backstage/index.html')
    return render(request, 'backstage/login.html')


def index(request):

    return render(request, 'backstage/index.html')

def article(request):
    with open('static/mdeia/articles/1.txt', 'r') as file:
        text = file.read()

    print(text)
    return render(request, 'backstage/article.html')

def notice(request):

    return render(request, 'backstage/notice.html')

def comment(request):

    return render(request, 'backstage/comment.html')

def category(request):

    return render(request, 'backstage/category.html')

def flink(request):

    return render(request, 'backstage/flink.html')

def manage_user(request):

    return render(request, 'backstage/manage-user.html')

def loginlog(request):

    return render(request, 'backstage/loginlog.html')

def setting(request):

    return render(request, 'backstage/setting.html')

def readset(request):

    return render(request, 'backstage/readset.html')

def add_article(request):
    if request.method == 'GET':
        return render(request, 'backstage/add-article.html')

    if request.method == 'POST':
        data = request.POST
        artic = Articles()
        artic.a_author = 'admin'
        artic.a_title = data['title']
        artic.a_keyWord = data['keywords']
        artic.a_describe = data['describe']
        artic.a_column = data['category']
        artic.a_label = data['tags']
        artic.a_picture = request.FILES.get('titlepic', None)
        # if not picture:
        #     return HttpResponse("No files")
        # with open("static/mdeia/"+picture.name, 'wb+') as file:
        #     for chunk in picture.chunks():
        #         file.write(chunk)
        cont = data['content']
        with open('static/mdeia/articles/'+data['title']+'.txt','w') as file:
            for c in cont[3:-4]:
                file.write(c)
        artic.save()
        return render(request, 'backstage/article.html')