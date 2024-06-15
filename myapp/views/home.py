from django.shortcuts import *
from myapp.models import home_todolist_model
from myapp.forms import home_todolist


def home(request):

        # tasks = home_todolist_model.objects.all()
        # form = home_todolist.home_todolistForm()
        #
        # if request.method == 'POST':
        #     form = home_todolist.home_todolistForm(request.POST)
        #     if form.is_valid():
        #         form.save()
        #         return redirect('home')  # 重定向到当前页面以刷新表格显示
        # return render(request, 'home.html', {'tasks': tasks, 'form': form})

        # views.py

        if request.method == 'POST':
            form = home_todolist.home_todolistForm(request.POST)
            if form.is_valid():
                form.save()  # 将表单数据保存到数据库
                return redirect('home')  # 重定向到当前页面以刷新表格显示
        else:
            form = home_todolist.home_todolistForm()

        tasks = home_todolist_model.objects.all()
        return render(request, 'home.html', {'tasks': tasks, 'form': form})

