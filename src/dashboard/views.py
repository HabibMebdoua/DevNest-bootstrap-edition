from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from projects.models import Project
from projects.filters import ProjectFilter

## Client Part

## Link telegram account



   
    


@login_required
def client_dashboard(request):
    projects = Project.objects.filter(owner=request.user)

    ##Filter Part
    project_filter = ProjectFilter(request.GET, queryset=projects)
    projects = project_filter.qs

    context = {
        'projects': projects,
        'project_filter': project_filter,
    }
    return render(request, 'dashboard/client_dashboard.html',context)


@login_required
def client_edit_project(request , project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        project.title = request.POST.get('title')
        project.description = request.POST.get('description')
        project.type = request.POST.get('type')

        ppt_presentation = request.POST.get('include_ppt') == 'on'
        tech_card = request.POST.get('include_datasheet') == 'on'

        project.ppt_presentation = ppt_presentation
        project.tech_card = tech_card

        project.save()
        messages.success(request, 'تم تحديث المشروع بنجاح')
        return redirect('client_dashboard')

    context = {
        'project':project
    }
    return render(request , 'dashboard/client_dashboard.html' , context)

@login_required
def client_delete_project(request, project_id):
    project = Project.objects.get(id=project_id, owner=request.user)
    if project.state != 'pending':
        messages.error(request, 'لا يمكنك حذف مشروع في حالة قيد التنفيذ أو مكتمل.')
        return redirect('client_dashboard')
    else:
        project.delete()
        messages.success(request , 'تم حذف المشروع بنجاح')
    return redirect('client_dashboard')
    

## Admin Part
@login_required
def admin_dashboard(request):
    projects = Project.objects.all()
    project_filter = ProjectFilter(request.GET, queryset=projects)
    projects = project_filter.qs

    # Data
    projects_inprogress = projects.filter(state='inprogress').count()
    projects_completed = projects.filter(state='completed').count()

    context = {
        'projects': projects,
        'project_filter': project_filter,

        'projects_inprogress': projects_inprogress,
        'projects_completed': projects_completed,
    }
    return render(request, 'dashboard/admin_dashboard.html', context)


@login_required
def admin_edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        project.state = request.POST.get('state')
        project.delivery_date = request.POST.get('delivery_date')
        project.save()
        messages.success(request, 'تم تحديث المشروع بنجاح')

        
        if project.state == 'pending':
            state = 'قيد الانتظار'
        elif project.state == 'inprogress':
            state = 'قيد التطوير'
        else:
            state = 'تم الإنتهاء من التطوير'

        if project.owner.chat_id:
            message = (
            f"📢 *تحديث جديد لمشروعك!*\n\n"
            f"📌 *عنوان المشروع:* {project.title}\n"
            f"📊 *الحالة الجديدة:* {state}\n"
            f"📅 *تاريخ التسليم المتوقع:* {project.delivery_date}\n\n"
            f"يرجى التحقق من لوحة التحكم لمتابعة التفاصيل."
            )
            # send_telegram_message(message , project.owner.chat_id)

            messages.success(request, 'تم إعلام المالك بنجاح')
        else:
            messages.warning(request , 'المالك لم يربط حسابه ب Telagram')
        return redirect('admin_dashboard')
    context = {
        'project': project,
    }
    return render(request, 'dashboard/admin_edit_project.html', context)

def admin_delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if project.state != 'pending':
        messages.error(request, 'لا يمكنك حذف مشروع في حالة قيد التنفيذ أو مكتمل.')
        return redirect('admin_dashboard')
    else:
        project.delete()
        messages.success(request, 'تم حذف المشروع بنجاح')
    return redirect('admin_dashboard')