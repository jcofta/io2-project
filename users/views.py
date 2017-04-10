from django.shortcuts import get_object_or_404,render

from .models import Question
from django.http import Http404

from django.http import HttpResponse

#

# def login(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'eleague/index.html', context)
