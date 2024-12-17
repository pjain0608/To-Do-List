from django.shortcuts import render, get_object_or_404, redirect
from .models import Task, History

def home(request):
    edit = False
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        a = Task.objects.create(title=title, description=description)
        return redirect('home')
    return render(request, 'home.html',{'edit':edit})


def history(request):
    htable = History.objects.all()
    context = {
        'htable' : htable
    }
    return render(request,'history.html',context)

def delete(request,ak):
    print('Hello')
    htable = History.objects.get(id = ak)
    htable.delete()
    return redirect('history')

def display(request,ab):
    data3 = Task.objects.get(id = ab)
    if request.method == 'POST':
        b = History.objects.create(htitle = data3.title, hdescription = data3.description)
        data3.delete()
        return redirect('task_list')
    context = {
        'data3' : data3
    }
    return render(request, 'display.html', context)

def task_list(request):
    # data1 = Task.objects.all()
    # context = {
    #     'data1' : data1
    # }
    # return render(request, 'task_list.html',context)
    query = request.GET.get('search', '')  
    if query:
        data1 = Task.objects.filter(title__icontains=query)  
    else:
        data1 = Task.objects.all()  # Get all tasks if no query
    return render(request, 'task_list.html', {'data1': data1, 'is_task_list': True})

def edit(request,pk):
    edit = True
    data4 = Task.objects.get(id = pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        data4.title = title
        data4.description = description
        data4.save()
        return redirect('task_list')

    context = {
        'data4' : data4,
        'edit' : edit
    }
    return render(request, 'edit.html',context)

def contact(request):
    return render(request, 'contact.html')