from django.db import models
from django.contrib import admin
from SBlog.models import Post
#from django.contrib.admin.sites import AdminSite
from epiceditor.widgets import AdminEpicEditorWidget

class PostAdmin(admin.ModelAdmin):
    search_fields = ('title','archive')
    list_display = ('title','author','archive','timestamp')

#class MyAdminSite(AdminSite):
#    login_template = 'login.html'
    formfield_overrides = {
            models.TextField:{'widget':AdminEpicEditorWidget},
            }


#AdminSite.login_template = 'login.html'
admin.site.register(Post,PostAdmin)
