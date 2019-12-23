from django.shortcuts import render, redirect
from . models import Home
from django.contrib.auth.decorators import login_required
from . import forms
from django.core.paginator import Paginator


def homepage(request):
    # return render(request, 'home/home.html')
    a = 9.8  # YouTube
    b = 343  # Instagram
    c = 50  # Twitter
    homeblog_list = Home.objects.all().order_by('-date')

    # Pagination
    # Show 10 Post Per Page
    paginator = Paginator(homeblog_list, 8)

    page = request.GET.get('page')
    homeblog = paginator.get_page(page)
    articles = {
        'articles': homeblog,
        'youtube_subscriber': a,
        'instagram_followers': b,
        'twitter_followers': c,
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
    user = request.user
    try:
        if request.user.is_staff:
            form = forms.EditPostForm(instance=instance)
            args = {'form': form}
            # The line below cause delete previous post when do not save
            return render(request, 'home/article_edit.html', args)
        else:
            return render(request, 'home/not_valid_user.html')
    except:
        return render(request, 'home/not_valid_user.html')


def article_detail(request, slug):
    article = Home.objects.get(slug=slug)
    return render(request, 'home/article_detail.html', {'article': article})
