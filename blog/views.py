from django.shortcuts import get_object_or_404, render
# from requests import get
from .models import Blog
# Create your views here.

def blog_list(request):

    blog = Blog.objects.all()

    context = {
        'blogs':blog
    }

    return render(request,'blog/blog.html',context)


def blog_detail(request,slug):

    blog = get_object_or_404(Blog,slug=slug)

    return render(request, 'blog/blog_detail.html', {'blog':blog})