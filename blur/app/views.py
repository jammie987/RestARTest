import json

from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django_celery_monitor.models import TaskState
from django.views.generic.edit import FormView

from .form import VideoForm
from .models import Video
from .tasks import estimate


class AddVideoFormView(FormView):
    template_name = 'add_video.html'
    form_class = VideoForm
    success_url = reverse_lazy('index')


class AddVideoAPIView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(AddVideoAPIView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        link = request.POST['video_link']
        estimate.delay(link)
        return HttpResponse(content='ok', status=200)


class ResultsView(TemplateView):
    template_name = 'results.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ResultsView, self).get_context_data(*args, **kwargs)
        context['results'] = Video.objects.all()
        return context
