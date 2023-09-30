from django.shortcuts import render, redirect
#from http.client import HTTPResonse
from .models import Post,Comment
from blog.forms import CommentForm
from .ai_recog import identify_ifbad
from .ai_gen import generate_comments
import asyncio

# Create your views here.
def frontpage(request):
    posts=Post.objects.all()
    return render(request,"blog/frontpage.html",{"posts":posts})

def post_detail(request, slug):
    post=Post.objects.get(slug=slug)

    if request.method=="POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            generate_comments(post)
            identify_ifbad()
            return redirect("post_detail", slug=post.slug)

    else:
        form=CommentForm()

    return render(request, "blog/post_detail.html", {"post":post, "form":form})