# Create your views here.
from django.shortcuts import render,render_to_response
from django.template import loader,Context,RequestContext
from django.http import HttpResponse
from blog.models import *

def custom_proc(request):
    '''A context processor that provides 'app', 'user' and 'ip_address'.'''
    return {
        'app': 'My app',
        'user': request.user,
        'ip_address': request.META['REMOTE_ADDR']
    }
# Create your views here.
def archive(request):
    posts = BlogsPost.objects.all()
    t = loader.get_template("archive.html")
    c = Context({'posts':posts,'progressbar':'10'})
    return HttpResponse(t.render(c))

def online(request):
    t = loader.get_template("online.html")
    #c = Context({"apps":["aa","bb","cc"]})
    form = AppForm(initial={'apps':'aa'})
    c = RequestContext(request, {"apps":["aa","bb","cc"]}, processors=[custom_proc]) 
    return HttpResponse(t.render(c))

def app(request):
    app = request.META.get('app', 'unknown')
    t = loader.get_template("online.html")
    c = Context({"apps":["app"], "version":"1.0"})
    return HttpResponse(t.render(c))

def help(request):
    t = loader.get_template("help.html")
    c = Context({'progressbar':'50'})
    return HttpResponse(t.render(c))

def jpaas(request):
    posts = BlogsPost.objects.all()
    t = loader.get_template("jpaas.html")
    c = Context({'posts':posts,'progressbar':'10'})
    return HttpResponse(t.render(c))

def deploy(request):
    if request.method == 'POST':
        print request.POST.getlist
    if request.POST.has_key("icafe"):
        print 'icafe'
    t = loader.get_template("online.html")
    c = RequestContext(request, {"apps":[request.POST['app']]}, processors=[custom_proc]) 
    return HttpResponse(t.render(c))
    
