# coding:utf-8
from django.db import models
from django.contrib import admin

class Tag(models.Model):
    '''标签'''
    name = models.CharField(max_length=100,unique=True,verbose_name=u'标签名')
    count_tag = models.IntegerField(default=0,editable=False,verbose_name=u'相关文章数')

    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return u'/tags/%s/' % self.name


class Post(models.Model):
    '''文章'''
    title = models.CharField(max_length=200,verbose_name=u'标题')
    author = models.CharField(max_length=100,verbose_name=u'作者')
    slug = models.SlugField(max_length=100,verbose_name=u'Slug',help_text = u'本文的短标题，将出现在文章的url中')
    archive = models.CharField(max_length=100,verbose_name=u'归档标签',help_text = u'用于给文章分类，比如博客，心情什么的')
    count_hit = models.IntegerField(default=0,editable=False,verbose_name=u'点击数')
    content = models.TextField(verbose_name=u'内容')
    abstract = models.TextField(verbose_name=u'摘要')
    timestamp = models.DateTimeField(u'编辑时间',auto_now=True)
    allow_comment = models.BooleanField(default = True,verbose_name='允许评论')
    ## Tags 多对多的关系
    ##tags = models.ManyToManyField(Tag,blank=True,verbose_name='标签')
    ##taglist = []

    def __unicode__(self):
        return u'%s' % self.title

    def get_absolute_url(self):
        return u'/articles/%s' % self.slug

    #def save(self,*args,**kwargs):
        ##taglist = ','.join([i['name'] for i in self.tags.all().values()]).split(',')
        
        #taglist = [i['name'] for i in self.tags.all().values()]
    #    print self.tags.all().value()

    #    super(Post,self).save()

        ##for i in taglist:
        ##    p, created = Tag.objects.get_or_create(name=i)
        ##    self.tags.add(p)
        ##self.taglist = []

    class Meta:
        ordering = ['-id']
        verbose_name_plural = verbose_name = u'文章' 
        

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp')
    search_fields = ('title',)


admin.site.register(Tag)
admin.site.register(Post,PostAdmin)
