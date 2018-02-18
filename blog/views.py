from django.shortcuts import render


def blogIndex(request):
    return render(request, "blog/blog.html")