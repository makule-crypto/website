from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author'     : 'makule',
        'title'      : 'blog post 1',
        'content'    : 'first post content',
        'date_posted': 'march 17 2021'
    },
    {
        'author'     : 'goody',
        'title'      : 'blog post 2',
        'content'    : 'second post content',
        'date_posted': 'march 18 2021'
    }
]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

 
def about(request):
    return render(request, 'blog/about.html')