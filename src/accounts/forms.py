from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # موديل المستخدم المخصص

base_class = 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm'

class SignInForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')
        labels = {
            'username': 'الاسم الكامل',
            'email': 'البريد الإلكتروني',
            'phone_number': 'رقم الهاتف',
            'password1': 'كلمة المرور',
            'password2': 'تأكيد كلمة المرور',
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'class': base_class,
                'placeholder': 'الاسم الكامل'
            }),
            'email': forms.EmailInput(attrs={
                'class': base_class,
                'placeholder': 'البريد الإلكتروني'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': base_class,
                'placeholder': 'رقم الهاتف'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # تعريب حقول كلمة المرور
        self.fields['password1'].label = 'كلمة المرور'
        self.fields['password1'].help_text = 'يجب أن تحتوي على 8 أحرف على الأقل ولا يمكن أن تكون شائعة أو مشابهة لمعلوماتك الشخصية.'

        self.fields['password2'].label = 'تأكيد كلمة المرور'
        self.fields['password2'].help_text = 'أعد إدخال كلمة المرور للتأكيد.'

        self.fields['username'].help_text = 'الاسم الكامل للمستخدم، يجب أن يكون فريدًا.'

        self.fields['password1'].widget.attrs.update({
            'class': base_class,
            'placeholder': 'كلمة المرور'
        })
        self.fields['password2'].widget.attrs.update({
            'class': base_class,
            'placeholder': 'تأكيد كلمة المرور'
        })
