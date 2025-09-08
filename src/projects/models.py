from django.db import models
from accounts.models import CustomUser


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateField(blank=True, null=True)
    type = models.CharField(max_length=50, choices=[
        ('web', 'موقع ويب'),
        ('mobile', 'تطبيق موبايل'),
        ('desktop', 'تطبيق سطح المكتب'),
        ('vedio', 'فيديو تقديمي'),
        ('other', 'أخرى')
    ])
    state = models.CharField(max_length=50, choices=[
        ('pending', 'قيد المراجعة'),
        ('inprogress', 'قيد التنفيذ'),
        ('completed', 'مكتمل'),
    ], default='pending')
    ppt_presentation = models.BooleanField(default=False, verbose_name='هل تم تقديم عرض تقديمي؟')
    tech_card = models.BooleanField(default=False, verbose_name='هل تم تقديم بطاقة تقنية؟')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return self.title