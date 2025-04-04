from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    article = '''
    <h2>Welcome</h2>
    Hello, Django
    '''
    return HttpResponse(HTMLTemplate(article))

def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article))

@csrf_exempt
def create(request):
    print('request.method', request.method)
    article = '''
    <form action="/create/" method="post">
        <p><input type="text" name="title" placeholder="title"></p>
        <p><textarea name="body" placeholder="body"></textarea></p>
        <p><input type="submit"></p>
    </form>
    '''
    return HttpResponse(HTMLTemplate(article))

