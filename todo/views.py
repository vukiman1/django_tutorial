from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .form import TodoForm
from .models import Todo


def home(request):
    return render(request, "home.html", {"title": "Home"})


def index(request):
    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Công việc đã được thêm thành công!")
            return redirect("todo:index")
    form = TodoForm()

    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, "todo/index.html", page)


def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "Item removed!")
    return redirect("todo:index")


def lottery(request):
    return render(request, "lottery.html", {"title": "Lottery"})
