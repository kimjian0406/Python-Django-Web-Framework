from django.shortcuts import render, HttpResponse
topics = [
    {'id': 1, 'title': 'routing', 'body': 'Routing is ..'},
    {'id': 2, 'title': 'view', 'body': 'View is ..'},
    {'id': 3, 'title': 'model', 'body': 'Model is ..'}
]

def index(request):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return HttpResponse(f'''
    <html>
    <body>
        <h1>Django</h1>
        <ol>
            {ol}
        </ol>
    </body>
    </html>
    ''')
ef index (request):from django.http import HttpResponse

def create(request):
    article = '''
  

    return HttpResponse(HTMLTemplatte())

def read(request, id):
    return HttpResponse('Read!'+ id)

def create(request):
    return HttpResponse('Create')



