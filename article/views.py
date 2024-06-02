from django.db.models import Q
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse

from article.forms import ArticleForm, CommentForm
from article.models import Article, Comment


# Create your views here.

def index(request):
    context = {"isim": "Baran",
               "yas": 25,
               "numbers": [1, 2, 3, 4, 5, 6, 7, 8],
               "coffees": {"latte": 25, "americano": 30, "çay": 15, "filtre kahve": 35}
               }
    return render(request, "index.html", context)


def index2(request):
    return render(request, "index2.html")


def detail(request, id):
    article = get_object_or_404(Article, id=id)
    comments = article.comments.all()
    form = CommentForm()
    # article = Article.objects.filter(id=id).first()
    context = {
        "article": article,
        "comments":comments,
        "form": form,
    }
    return render(request, "detail.html", context)


def about(request):
    return render(request, "about.html")


def frontend_test(request):
    users = User.objects.all()
    return render(request, "frontend.html", context={"users": users})


@login_required(login_url="user:login")
def dashboard(request):
    articles = Article.objects.all()
    context = {
        "articles": articles
    }
    return render(request, "dashboard.html", context)


@login_required
def add_article(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        # author = form.cleaned_data.get("author")
        # title = form.cleaned_data.get("title")
        #
        # article = Article()
        # article.author = author
        # article.title = title
        # article.save()
        article = form.save(commit=False)  ##veritabanına gerçek bi save işlemi yapmamış oluyoruz.
        article.author = request.user
        article.save()

        messages.success(request, "Makaleniz başarıyla kaydedildi.")
        return redirect("article:dashboard")

    context = {
        "form": form
    }
    return render(request, "add_article.html", context)


@user_passes_test(lambda u: u.is_superuser)
def update_article(request, id):
    article = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()  # commit = True

        messages.success(request, "Makale başarıyla güncellendi.")
        return redirect("article:dashboard")
    return render(request, "update.html", {"form": form})


def delete_article(request, id):
    article = get_object_or_404(Article, id=id)
    article.delete()

    messages.success(request, "Makale başarıyla silindi.")
    return redirect("article:dashboard")


def articles(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(Q(title__icontains=keyword) | Q(content__contains=keyword))
        return render(request, "articles.html", {"articles": articles})
    articles = Article.objects.all()

    return render(request, "articles.html", {"articles": articles})


def add_comment(request, id):
    article = get_object_or_404(Article, id=id)
    form = CommentForm(request.POST or None)
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")
        new_comment = Comment()
        new_comment.comment_author = comment_author
        new_comment.comment_content = comment_content
        new_comment.article = article
        new_comment.save()
    # if form.is_valid():
    #     new_comment = form.save(commit=False)
    #     new_comment.comment_author = request.user
    #     new_comment.save()

    return redirect(reverse("article:detail", kwargs={"id": id}))