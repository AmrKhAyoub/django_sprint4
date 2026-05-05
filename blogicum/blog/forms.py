from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # استبعاد الحقول التي لا يدخلها المستخدم يدوياً
        exclude = ('author',)
        # إضافة تنسيقات Widgets لجعل شكل الحقول أفضل (اختياري حسب القوالب)
        widgets = {
            'pub_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
