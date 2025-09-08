from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, get_user_model,logout
from django.contrib.auth import login as auth_login
from django.contrib import messages
from .forms import SignInForm



def signin(request):
    form = SignInForm
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "تم التسجيل بنجاح. يمكنك الآن تسجيل الدخول.")
            return redirect('login')
        else:
            messages.error(request, "لقد حدث خطأ في التسجيل. يرجى التحقق من البيانات المدخلة.")
    else:
        form = SignInForm()

    context = {
        'form': form,
        }
    return render(request, 'accounts/signin.html', context)




def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        User = get_user_model()
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
        except User.DoesNotExist:
            user = None

        if user is not None:
            auth_login(request, user)
            messages.success(request, "تم تسجيل الدخول بنجاح.")
            return redirect('index')
        else:
            messages.error(request, "البريد الإلكتروني أو كلمة المرور غير صحيحة.")
    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)  
    messages.success(request, "تم تسجيل الخروج بنجاح.")
    return redirect('index')
