from django.db import models
from django.contrib import admin
from SBlog.models import Post
#from django.contrib.admin.sites import AdminSite
from pagedown.widgets import AdminPagedownWidget
from django import forms

##class PostForm(forms.ModelForm):
##    content = forms.TextField(widget=AdminEpicEditorWidget())
##    abstract = forms.TextField(widget=AdminEpicEditorWidget())
##
##    class Meta:
##        model = Post

class PostAdmin(admin.ModelAdmin):
    search_fields = ('title','archive')
    list_display = ('title','author','archive','timestamp')
    formfield_overrides = {
            models.TextField:{'widget':AdminPagedownWidget},
            }


##    form = PostForm

#class MyAdminSite(AdminSite):
#    login_template = 'login.html'
    #formfield_overrides = {
     #       models.TextField:{'widget':AdminEpicEditorWidget},
     #       }



#AdminSite.login_template = 'login.html'
admin.site.register(Post,PostAdmin)
