from tempfile import template
from django.http import HttpResponse
from django.template import loader
#from matplotlib.style import context

from .models import Bb, Rubric

def index(request):
    template = loader.get_template('bboard/index.html')
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    return HttpResponse(template.render(context, request))

def by_rubric(request, rubric_id):
    template = loader.get_template('bboard/by_rubric.html')
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics,
                'current_rubrics': current_rubric}
    return HttpResponse(template.render(context, request))

'''
    s = 'Список объявлений\r\n\r\n\r\n'
    for bb in Bb.objects.order_by('-published'):
        s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
    return HttpResponse(s, content_type='text/plain; charset=utf-8')
'''
