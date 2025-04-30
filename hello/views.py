from django.http import HttpResponse
from django.shortcuts import render


def hello_view(request):
    name = None
    if request.method == "POST":
        name = request.POST.get("name")
        if name:
            NameEntry.objects.create(name=name)
            return redirect('/')
            
    names = NameEntry.objects.order_by('-submitted_at')
    return render(request, "hello.html", {"name": name})
