from django.shortcuts import render, redirect, get_object_or_404
from . models import Home
from django.contrib.auth.decorators import login_required
# from . forms import *
from . import forms
from .models import *
from . forms import CommentForm
from django.core.paginator import Paginator
import pandas as pd
import datetime


def homepage(request):
    try:
        user_id = str(request.user.id)
        user_love_to_read = request.COOKIES[user_id]
        print("user_love_to_read:::::::::::::::::::::: ", user_love_to_read)
    except:
        user_love_to_read = 'ANDROID'
        print("user_love_to_read: User Not Login")

    homeblog_list = Home.objects.all().order_by('-date')

    # Pagination
    # Show 10 Post Per Page
    paginator = Paginator(homeblog_list, 9)

    page = request.GET.get('page')
    homeblog = paginator.get_page(page)
    articles = {
        'articles': homeblog,
        'user_love_to_read': user_love_to_read,
    }
    return render(request, 'home/home.html', articles)


def android(request):
    homeblog_list = Home.objects.all().order_by('-date')
    paginator = Paginator(homeblog_list, 10)
    page = request.GET.get('page')
    homeblog = paginator.get_page(page)
    return render(request, 'home/Android.html', {'articles': homeblog})


def PC(request):
    homeblog_list = Home.objects.all().order_by('-date')
    paginator = Paginator(homeblog_list, 10)
    page = request.GET.get('page')
    homeblog = paginator.get_page(page)
    return render(request, 'home/PC.html', {'articles': homeblog})


def News(request):
    homeblog_list = Home.objects.all().order_by('-date')
    paginator = Paginator(homeblog_list, 10)
    page = request.GET.get('page')
    homeblog = paginator.get_page(page)
    return render(request, 'home/News.html', {'articles': homeblog})


def Offers(request):
    homeblog_list = Home.objects.all().order_by('-date')
    paginator = Paginator(homeblog_list, 10)
    page = request.GET.get('page')
    homeblog = paginator.get_page(page)
    return render(request, 'home/Offers.html', {'articles': homeblog})


def MachineLearning(request):
    homeblog_list = Home.objects.all().order_by('-date')
    paginator = Paginator(homeblog_list, 10)
    page = request.GET.get('page')
    homeblog = paginator.get_page(page)
    return render(request, 'home/MachineLearning.html', {'articles': homeblog})


def Others(request):
    homeblog_list = Home.objects.all().order_by('-date')
    paginator = Paginator(homeblog_list, 10)
    page = request.GET.get('page')
    homeblog = paginator.get_page(page)
    return render(request, 'home/Others.html', {'articles': homeblog})


@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.user.is_staff:
        if request.method == 'POST':
            form = forms.CreateArticle(request.POST, request.FILES)
            if form.is_valid():
                # save article to db
                instance = form.save(commit=False)
                instance.author = request.user
                instance.save()
                return redirect('home:home')
        else:
            form = forms.CreateArticle()
        return render(request, 'home/article_create.html', {'form': form})
    else:
        return render(request, 'home/not_valid_user.html')


def article_detail(request, slug):
    article = Home.objects.get(slug=slug)
    return render(request, 'home/article_detail.html', {'article': article})


@login_required(login_url="/accounts/login/")
def article_delete(request, slug):
   if request.user.is_staff:
        user = request.user
        try:
            Home.objects.get(slug=slug, author_id=user).delete()
            return render(request, 'home/article_delete.html')
        except:
            return render(request, 'home/not_valid_user.html')
   else:
        return render(request, 'home/not_valid_user.html')


@login_required(login_url="/accounts/login/")
def article_update(request, slug):
    instance = Home.objects.get(slug=slug)
    instance_new = instance
    user = request.user
    if request.user.is_staff:
        if request.method == 'GET':
            form = forms.EditPostForm(instance=instance)
            args = {'form': form}
            # The line below cause delete previous post when do not save
            return render(request, 'home/article_edit.html', args)
        else:
            form = forms.CreateArticle(request.POST, request.FILES)
            args = {'form': form}
            if form.is_valid():
                # save article to db
                print("Save to DB")
                instance_new = form.save(commit=False)
                instance_new.author = request.user
                instance_new.save()
                Home.objects.get(slug=slug, author_id=user).delete()
                return redirect('home:home')
    else:
        return render(request, 'home/not_valid_user.html')


def what_user_read(request, article):
    if request.user.is_authenticated:
        user = request.user.email
        content = article.title + article.body
        category = article.category
        date = datetime.datetime.today()

        usr = [user]
        con = [content.replace(',', ' ')]
        cat = [category]
        date_ = [date]

        data = {'user': usr, 'date': date_, 'content': con, 'category': cat}

        df = pd.DataFrame(data)

        df.to_csv('media/user_data/what_user_read.csv', mode='a', header=False, index=False)


def get_user_id(request):
    try:
        user_id = request.user.id
        return user_id
    except:
        print("User is currently not login")


def article_detail(request, slug):
    article = Home.objects.get(slug=slug)
    category = article.category

    # what user love to read logs
    what_user_read(request, article)
    user_id = get_user_id(request)

    # # comments
    comments = article.comments.filter(Active=True, Parent__isnull=True)

    # post = get_object_or_404(Blog, Slug=slug)
    # comments = post.comments.filter(Active=True, Parent__isnull=True)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid:
            Parent_obj = None
            try:
                Parent_id = int(request.POST.get('Parent_id'))
            except:
                Parent_id = None
            if Parent_id:
                Parent_obj = Comment.objects.get(id=Parent_id)
                if Parent_obj:
                    reply_comment = comment_form.save(commit=False)
                    reply_comment.Parent = Parent_obj
            new_comment = comment_form.save(commit=False)
            new_comment.Post = article
            new_comment.save()
            return redirect('home:detail', slug)
    else:
        comment_form = CommentForm()

    response = render(request, 'home/article_detail.html', {'article': article, 'comments': comments, 'comment_form': comment_form })

    # save in cookie what category user read last time
    response.set_cookie(str(user_id), category)

    return response

    # article = Home.objects.get(slug=slug)
    # category = article.category
    #
    # # what user love to read logs
    # what_user_read(request, article)
    # user_id = get_user_id(request)
    #
    # # post = get_object_or_404(Home, slug=slug)
    # # comments
    # comments = article.comments.filter(Active=True, Parent__isnull=True)
    # if request.method == 'POST':
    #     comment_form = forms.CommentForm(data=request.POST)
    #     if comment_form.is_valid():
    #         Parent_obj = None
    #         try:
    #             Parent_id = int(request.POST.get('Parent_id'))
    #         except:
    #             Parent_id = None
    #         if Parent_id:
    #             Parent_obj = Comment.objects.get(id=Parent_id)
    #             if Parent_obj:
    #                 reply_comment = comment_form.save(commit=False)
    #                 reply_comment.Parent = Parent_obj
    #         new_comment = comment_form.save(commit=False)
    #         new_comment.Post = article
    #         new_comment.save()
    #         return redirect('home:home')
    #         # return redirect('home:detail', slug)
    #     else:
    #         comment_form = forms.CommentForm()
    #
    #     # response = render(request, 'home/article_detail.html', {'article': article, 'comment': comments, 'comment_form': comment_form })
    #
    # # response = render(request, 'home/article_detail.html',
    # #                   {'article': article})
    #
    # # save in cookie what category user read last time
    # #     response.set_cookie(str(user_id), category)
    #
    # # return response
    #     return render(request, 'home/article_detail.html', {'article': article, 'comment': comments, 'comment_form': comment_form})



