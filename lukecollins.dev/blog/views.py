from django.shortcuts import render, get_object_or_404
from .models import blog_preview

def all_blogs(request):
    blog_previews = blog_preview.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'blog_previews':blog_previews})

def detail(request, blog_id):
    blog = get_object_or_404(blog_preview, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})
