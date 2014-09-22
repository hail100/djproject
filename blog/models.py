from django.db import models
from django.contrib import admin
from django import forms

class AppForm(forms.Form):
    apps = forms.ChoiceField(choices=[('bb','bb'),('aa','aa')])

# Create your models here.
class BlogsPost(models.Model):
    title = models.CharField(max_length=150)
    body  = models.TextField()
    timestamp = models.DateTimeField()

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp')
    
admin.site.register(BlogsPost,BlogPostAdmin)
