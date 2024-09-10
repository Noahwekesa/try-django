from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import forms

from .models import Article


def articles_list_view(request):
    object_list = Article.objects.all()
    context = {"object_list": object_list}

    return render(request, "articles/list.html", context)


def article_delete_view(request):
    instance = get_object_or_404(Item)
    if request.method == "POST":
        instance.delete()
        messages.success(request, "Article deleted.")
        return redirect("article:list")
    context = {
        "instance": instance,
    }
    return render(request, "articles/delete.html", context)


@login_required
def articles_create_view(request):
    form = forms.ArticleCreateForm(request.POST or None)
    if form.is_valid():
        article_obj = form.save(commit=False)
        article_obj.save
        messages.success(request, "Aricle published.")
        # return redirect(article_obj.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, "articles/create.html", context)
