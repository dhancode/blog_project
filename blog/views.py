from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost

def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/index.html', {'posts': posts})

def blog_create(request):
    if request.method == 'POST':
        BlogPost.objects.create(
            title=request.POST['title'],
            author=request.POST['author'],
            content=request.POST['content'],
            image=request.FILES.get('image')
        )
        return redirect('blog_list')
    return render(request, 'blog/form.html')

def blog_detail(request, id):
    post = get_object_or_404(BlogPost, id=id)
    return render(request, 'blog/detail.html', {'post': post})

def blog_update(request, id):
    post = get_object_or_404(BlogPost, id=id)
    if request.method == 'POST':
        post.title = request.POST['title']
        post.author = request.POST['author']
        post.content = request.POST['content']
        if request.FILES.get('image'):
            post.image = request.FILES.get('image')
        post.save()
        return redirect('blog_list')
    return render(request, 'blog/form.html', {'post': post})

def blog_delete(request, id):
    post = get_object_or_404(BlogPost, id=id)
    post.delete()
    return redirect('blog_list')
