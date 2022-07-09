from django.shortcuts import render,redirect
from django.http import HttpResponse
from pollapplication.models import Register,Poll
from django.conf.urls.static import static
from .forms import CreatePollForm 
from .models import Poll

def first(request):
	msg="registerd successfully"
	return render(request,'template/register.html', {"msg":msg})

def home(request):
    polls = Poll.objects.all()

    context = {}
    return render(request, 'template/home.html', context)

def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
    else:
        form = CreatePollForm()

    context = {'form' : form}
    return render(request, 'template/create.html', context)

def results(request,poll_id):
    context = {}
    return render(request, 'template/results.html', context)

def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    context = {
        'poll' : poll
    }
    return render(request, 'template/vote.html', context)
def register(request):
	context = {}
	return render(request,'template/register.html',context)
def registercode(request):
	if request.method=="POST":
		a=request.POST['t1']
		b=request.POST['t2']
		c=request.POST['t3']
		d=request.POST['t4']
		data=Register(name=a,email=b,password=c,phoneno=d)
		data.save()
		msg="registerd successfully"
		return render(request,'template/msg.html',{"msg":msg})
	else:
		return render(request,'template/register.html')
def login(request):
	context = {}
	return render(request,'template/login.html',context)
def logincode(request):
	if request.method=="POST":
		a=request.POST['t1']
		b=request.POST['t2']
		if a=="mb@gmail.com" and b=="madhu12345":
			request.session['admin']=a
			return redirect("/admin/")
		else:
			user=Register.objects.filter(email=a,password=b).count()
			if(user==0):
				msg="Not match"
				return render(request,"template/msg.html",{"msg":msg})
			else:
				request.session['user']=a
				return redirect("/login/")
	else:
		return redirect("/login/")


# Create your views here.
