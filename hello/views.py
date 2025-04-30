from django.http import HttpResponse
from django.shortcuts import render


def hello_view(request):
    name = None
    if request.method == "POST":
        name = request.POST.get("name")
    return render(request, "hello.html", {"name": name})
