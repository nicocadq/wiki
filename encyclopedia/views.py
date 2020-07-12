from django.shortcuts import render, redirect, reverse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    f = util.get_entry(title)
    if f is not None:
        return render(request, "encyclopedia/entry.html", {
            "title": title.capitalize(),
            "content": f,
        })
    return redirect(reverse(not_found))

def not_found(request):
    return render(request, "encyclopedia/not_found.html")