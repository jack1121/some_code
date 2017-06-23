from django.http import Http404
from django.shortcuts import render,get_object_or_404
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from .models import EbTerminal,EbArea
from .forms import NameForm


def index(request):
	#a = EbTerminal.objects.all().filter(terminal_type=1).exclude(status=1).filter(branch_id=2)
	a = EbTerminal.objects.extra(where=['terminal_type=%s','status = %s'], params=['1','0'])
	context = {'terminal': a,'topic':"Terminal List"}
	return render(request,'ems/index.html',context)

def login(request):
	if request.method == 'POST':
		form = NameForm(request.POST)
		if form.is_valid():
			if form.cleaned_data['your_name']=='hj':
				return HttpResponseRedirect('/ems/')
			else:
				form = NameForm()
				context = {'name':'hj','form':form}
				return render(request,'ems/login.html',context)
	else:
		form = NameForm()
		context = {'name':'hj','form':form}
		return render(request,'ems/login.html',context)



'''
class IndexView(generic.ListView):
	model = EbTerminal
	template_name = 'ems/index.html'

class DetailView(generic.DetailView):
    model = Question
    template_name = 'ems/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'ems/results.html'
'''