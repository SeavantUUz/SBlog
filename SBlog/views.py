# Create your views here.
from SBlog.models import Post
from django.template import loader,Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.db.models import Q
from django.core.mail import send_mail
from django.utils.http import urlquote


def home(request):
    posts = Post.objects.all()
    t = loader.get_template('home.html')
    c = Context({ 'posts':posts})
    return HttpResponse(t.render(c))

def search(request):
    query = request.GET.get('q','')
    if query:
        qset = (
                Q(title__icontains=query) |
                Q(abstract__icontains=query)
                )
        results = Post.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("search.html",{
        "results":results,
        "query":query
        })

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
