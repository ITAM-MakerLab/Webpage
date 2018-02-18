from django.shortcuts import render, get_object_or_404
from .models import BlogEntry


def blogIndex(request):
    recent_blogs = BlogEntry.objects.order_by("entryDateTime").reverse()
    blog_context = {"blogs_list": recent_blogs}
    return render(request, "blog/blogIndex.html", blog_context)


def blogEntry(request, blogEntry_id):
    selected_entry = get_object_or_404(BlogEntry, pk=blogEntry_id)
    entry_context = {"selected_entry": selected_entry}
    return render(request, "blog/blogEntryDetail.html", entry_context)