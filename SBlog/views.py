# Create your views here.
# coding=utf-8
from SBlog.models import Post
from django.template import loader,Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.utils.http import urlquote
from django.contrib.auth import authenticate,login

def home(request):
    posts = Post.objects.all()
    t = loader.get_template('home.html')
    c = Context({ 'posts':posts})
    return HttpResponse(t.render(c))

##def login_usr(request):
##    state = u'如果输入了正确的密码，我就会开门的说～'
##    username = password=''
##    if request.POST:
##        username = request.POST.get('username')
##        password = request.POST.get('password')
##
##        user = authenticate(username=username,password=password)
##        if user is not None:
##            if user.is_active:
##                login(request,user)
##                state = u'ご主人様、いらっしゃい~~~'
##            else:
##                state = u'是谁啊？不认识你哦？'
##        else:
##            state = u"输入就不对嘛，你是谁，不明人士(笑)?"
##    return render_to_response('login.html',{'state':state,'username':username})

def show_blog(request,slug):
    try:
        post = Post.objects.get(slug=slug)
    except:
        raise Http404

    post.count_hit += 1
    post.save()

    return render_to_response('page.html',{
        'page':post
        })
    
##    return HttpResponse("Hello World")


def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject',''):
            errors.append('Enter a subject.')
        if not request.POST.get('message',''):
            errors.append('Enter a valid e-mail addreess.')
        if not errors:
            send_mail(
                    request.POST['subject'],
                    request.POST['message'],
                    request.POST.get('email','axdiaoqi220@gmail.com'),
                    )
            return HttpResponseRedirect('/contact/thanks/')
        return render_to_response('contact_form.html',{'errors':errors})
