from django.http import HttpResponse

def hello_view(request):
    name = None
    if request.method == "POST":
        name = request.POST.get("name")
    return render(request, "hello.html", {"name": name})
