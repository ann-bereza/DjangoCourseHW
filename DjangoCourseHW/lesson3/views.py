from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# Завдання 1 та 5
def tasks(request):
    lets_do_it = [{'priority': 100, 'task': 'Скласти перелік справ'}, {'priority': 150, 'task': 'Вивчати Django'},
                  {'priority': 1, 'task': 'Подумати про сенс життя'}]
    sorted_todo = reversed(sorted(lets_do_it, key=lambda x: x['priority']))
    return render(request, 'lesson3/tasks.html', context={'lets_do_it': sorted_todo})


# Завдання 2
def main(request):
    return render(request, 'lesson3/star_wars_main.html')


def page(request):
    name = request.path.split("/")[2]
    return render(request, f'lesson3/{name}.html')


# Завдання 3
def send_file(request):
    with open('lesson3/file.txt', 'rb') as file:
        file_data = file.read()
    response = HttpResponse(file_data, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="file.txt"'
    response.status_code = 227
    return response


# Завдання 4
def file_response(request):
    with open('lesson3/file.txt', 'r') as file:
        content = file.read()
    response = HttpResponse(content, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="file.txt"'
    return response


def json_response(request):
    data = {'name': 'John', 'age': 30}
    response = JsonResponse(data)
    return response


def html_response(request):
    context = {'title': 'Welcome!', 'message': 'Hello, world!'}
    return render(request, 'lesson3/template.html', context)


def text_response(request):
    response = HttpResponse('Hello, world!', content_type='text/plain')
    return response


# Завдання 6
def dune(request):
    people = [{'name': 'Шаддам IV', 'surname': 'Корріно'}, {'name': 'Пол', 'surname': 'Атрід'},
              {'name': 'Френк', 'surname': 'Герберт'}]
    context = {'people': people}
    return render(request, 'lesson3/dune.html', context)


# Завдання 7
def existential(request):
    latest_question_list = [
        {'id': 1, 'question_text': 'У чому сенс життя?'}, {'id': 2, 'question_text': 'Що первинне: дух чи матерія?'},
        {'id': 3, 'question_text': 'Чи існує свобода волі?'}]
    context = {'questions': latest_question_list}
    return render(request, 'lesson3/existential.html', context)


def question(request, question_id):
    return HttpResponse(f"<h1>This is a page for question id {question_id}</h1>")
