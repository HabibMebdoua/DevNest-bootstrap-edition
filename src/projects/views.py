from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required
from .forms import OrderProjectForm
from django.contrib import messages



@login_required
def order_project(request):
    form = OrderProjectForm()
    if request.method == 'POST':
        form = OrderProjectForm(request.POST)
        if form.is_valid():

            # Getting data from the form
            data = form.cleaned_data
            project_title = data.get('title')
            project_desc = data.get('description')
            project_type = data.get('type')
            project_owner = request.user

           
           

            order = form.save(commit=False)
            order.owner = request.user
            order.save()
            messages.success(request, ' تم إرسال طلب المشروع بنجاح! قم بتفقد لوحة التحكم')
            return redirect('index')
        else:
            messages.error(request, 'حدث خطأ أثناء إرسال طلب المشروع. يرجى المحاولة مرة أخرى.')

    context = {
        'form': form
    }
    return render(request, 'projects/order_project.html', context)