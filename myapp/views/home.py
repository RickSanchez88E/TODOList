from django.shortcuts import *
from myapp.models import home_todolist_model
from myapp.forms import home_todolist


def home(request):
        if request.method == 'POST':
            form = home_todolist.home_todolistForm(request.POST)
            if form.is_valid():
                form.save()  # 将表单数据保存到数据库
                return redirect('home')  # 重定向到当前页面以刷新表格显示
        else:
            form = home_todolist.home_todolistForm()

        tasks = home_todolist_model.objects.all()
        return render(request, 'home.html', {'tasks': tasks, 'form': form})

def delete_task(request, task_id):
        task = home_todolist_model.objects.get(id=task_id)
        task.delete()
        return HttpResponseRedirect(reverse('home'))


def edit_task(request, task_id):
    task = get_object_or_404(home_todolist_model, id=task_id)
    if request.method == 'POST':
        form = home_todolist.home_todolistForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = home_todolist.home_todolistForm(instance=task)
    return render(request, 'home.html', {'form': form})

