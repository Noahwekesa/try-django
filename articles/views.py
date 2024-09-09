from django.shortcuts import render

from .models import Article


def articles_list_view(request):
    obj_list = Article.objects.all()
    context = {"obj_list": obj_list}

    return render(request, "articles/list.html", context)
