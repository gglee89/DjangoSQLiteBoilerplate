from django.shortcuts import render
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.http import HttpResponse, Http404

# External Modules
from .tasks import run_script
from .forms import InstaloaderForm

def index(request):
    return render(request, 'core/index.html')

def instaloader(request):
    # usuario = form.cleaned_data['user']
    # password = form.cleaned_data['password']
    # shortCode = form.cleaned_data['shortCode']
    
    USERNAME = 'gustavogiwoolee'
    PASSWORD = 'Gust@vo123Inst@gr@M'
    SHORTCODE = 'B8T_oFwlSY4pmVElZUuPNHTvq1fzlk7-XpP-oU0'
    
    result = run_script.delay(USERNAME, PASSWORD, SHORTCODE)
    messages.success(self.request, 'We are fetching your posts! Wait a moment and refresh this page.')
    
    return HttpResponse('Worker processing: ' + result.ready())