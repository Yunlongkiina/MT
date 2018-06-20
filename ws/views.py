# Create your views here.
# URL : menu view: kitchen template: food
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from ws.models import News

def index(request):
    return render(request, "ws/index.html", {})


def search_form(request):
    return render(request, "ws/search_form.html", {})


def news_visual(request):
    return render(request, "ws/News_Visual.html", {})


def cv(request):
    return render(request, "ws/cv.html",{})


def search(request):
    if 'publisher' in request.GET and request.GET['publisher']:
        publisher = request.GET['publisher']
        news = News.objects.filter(name__icontains=publisher)
        return render(request, "ws/search_result.html", {'news': news, 'query': publisher} )
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)


def post_detail(request, pk):
    post = get_object_or_404(News, pk=pk)
    return render(request, 'ws/post_detail.html', {'post': post})
# About


def about(request):
    return render(request, "ws/about.html", {})





