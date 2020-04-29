from django.http import HttpResponse
from django.shortcuts import render
from .models import Question
from django.template import loader


def index(request):
    ''' # Obtenemos las 5 ultimas preguntas ordenadas por fecha de publicacion (La mas reciente antes)
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # Las concatenamos con comas
    output = ", ".join([q.question_text for q in latest_question_list])

    return HttpResponse(output)
    '''

    '''Si se hace como arriba, cada vez que se quiera cambiar la vista hay que cambiar este código python.
    Lo mejor es hacer una plantilla'''

    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }

    ''' Dos manera de devolver la respuesta, con HttpResponse o con Render.'''
    # return HttpResponse(template.render(context, request))
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    return HttpResponse("Estás viendo la pregunta " + str(question_id))


def results(request, question_id):
    return HttpResponse("Estás viendo los resultados de la pregunta: " + str(question_id))


def vote(request, question_id):
    return HttpResponse("Estás votando la pregunta " + str(question_id))
