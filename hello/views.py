from django.shortcuts import render, redirect
from .models import NameEntry

def hello_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        if name:
            NameEntry.objects.create(name=name)
            return redirect('/hello/')  # redirect to prevent duplicate submission

    names = NameEntry.objects.order_by('-submitted_at')
    return render(request, "hello.html", {"names": names})
