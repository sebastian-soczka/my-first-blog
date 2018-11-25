from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.
# def post_list(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[0:3]
#     return render(request, 'blog/post_list.html', {'posts': posts})

def main(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[0:3]
    dictionary = {
        'posts': posts,
    }
    return render(request, 'blog/main.html', dictionary)

def all_posts(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    dictionary = {
        'posts': posts,
    }
    return render(request, 'blog/all_posts.html', dictionary)

def single_post(request, post_num):
    post= Post.objects.get(id=post_num)
    dictionary = {
        'post': post,
    }
    return render(request, 'blog/single_post.html', dictionary)

def posts_by_book(request, book_title):
    if book_title == 'poczatek':
        book_title = 1
    if book_title == 'mrok_pod_ziemia':
        book_title = 2
    posts = Post.objects.filter(book=book_title).order_by('-published_date')
    dictionary = {
        'posts': posts,
    }
    return render(request, 'blog/all_posts.html', dictionary)