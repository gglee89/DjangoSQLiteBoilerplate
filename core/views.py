from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

# External Modules
from .tasks import run_script

def index(request):
    # output = ', '.join([p.question_text for q in latest_question_list])    
    # return HttpResponse(template.render(context, request))
    return render(request, 'core/index.html', context);

def instaloader(request):
    USERNAME = 'gustavogiwoolee'
    PASSWORD = 'Gust@vo123Inst@gr@M'
    SHORTCODE = 'B8T_oFwlSY4pmVElZUuPNHTvq1fzlk7-XpP-oU0'

    result = run_script.delay(USERNAME, PASSWORD, SHORTCODE)
    return HttpResponse('Worker processing: ' + result.ready())