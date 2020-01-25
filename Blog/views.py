from django.contrib.auth.models import User
from .models import Post
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import Profile


@login_required
def home(request):
    current_user_id = request.user.id
    user = User.objects.get(id=current_user_id)
    # profile = User.objects.get(id=current_user_id)
    context = {
        'posts': Post.objects.all(),
        'user': user,

    }
    print(context)
    print(Post)

    return render(request, 'Blog/base.html', context)


def post_list_view(request):
    author = request.user
    title = request.POST.get('title')
    content = request.POST.get('post')
    Post.objects.create(author=author, title=title, content=content)
    return redirect('home')


def post_delete_view(request, pk):
    current_post = Post.objects.get(id=pk)
    post_author = current_post.author

    if post_author == request.user:
        current_post.delete()

    return redirect('home')


def post_update_view(request, pk):
    current_post = Post.objects.get(id=pk)
    post_author = current_post.author

    if request.method == 'POST':
        if post_author == request.user:
            title = request.POST.get('title')
            content = request.POST.get('post')
            current_post.title = title
            current_post.content = content
            current_post.save()
            return redirect('home')

