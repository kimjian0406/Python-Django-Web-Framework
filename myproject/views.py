from django.shortcuts import render, HttpResponse,redirect
form django .views.decorators.csrf import csrf_exempt
form django .shortcuts import redirect


nextid = 4
topics = [
    {'id': 1, 'title': 'routing', 'body': 'Routing is ..'},
    {'id': 2, 'title': 'view', 'body': 'View is ..'},
    {'id': 3, 'title': 'model', 'body': 'Model is ..'}
]

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
elft requsest.method == 'POST' :
     title = request.POST['title']
     body = request.POST['body']
     newTopic = {"title": title, "body": body}
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
    global nextId
    if request.method == 'GET':
        article = '''
        <form action="/create/" method="post">
            <p><input type="text" name="title" placeholder="title"></p>
            <p><textarea name="body" placeholder="body"></textarea></p>
            <p><input type="submit"></p>
        </form>
        '''
        return HttpResponse(HTMLTemplate(article))
    elif request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        newTopic = {"id": nextId, "title": title, "body": body}
        topics.append(newTopic)
        nextId = nextId + 1
        return HttpResponse(HTMLTemplate('AAA'))
@csrf_exempt
def create(request):
    global nextId
    if request.method == 'GET':
        article = '''
        <form action="/create/" method="post">
            <p><input type="text" name="title" placeholder="title"></p>
            <p><textarea name="body" placeholder="body"></textarea></p>
            <p><input type="submit"></p>
        </form>
        '''
        return HttpResponse(HTMLTemplate(article))
    elif request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        newTopic = {"id": nextId, "title": title, "body": body}
        topics.append(newTopic)
        url = '/read/' + str(nextId)
        nextId = nextId + 1
        return redirect(url)
@csrf_exempt
def create(request):
    global nextId
    if request.method == 'GET':
        article = '''
        <form action="/create/" method="post">
            <p><input type="text" name="title" placeholder="title"></p>
            <p><textarea name="body" placeholder="body"></textarea></p>
            <p><input type="submit"></p>
        </form>
        '''
        return HttpResponse(HTMLTemplate(article))
    elif request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        newTopic = {"id": nextId, "title": title, "body": body}
        topics.append(newTopic)
        url = '/read/' + str(nextId)
        nextId = nextId + 1
        return redirect(url)
@csrf_exempt
def create(request):
    global nextId
    if request.method == 'GET':
        article = '''
        <form action="/create/" method="post">
            <p><input type="text" name="title" placeholder="title"></p>
            <p><textarea name="body" placeholder="body"></textarea></p>
            <p><input type="submit"></p>
        </form>
        '''
        return HttpResponse(HTMLTemplate(article))
    elif request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        newTopic = {"id": nextId, "title": title, "body": body}
        topics.append(newTopic)
        url = '/read/' + str(nextId)
        nextId = nextId + 1
        return redirect(url)


from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt

# 데이터 저장
nextId = 4
topics = [
    {'id': 1, 'title': 'routing', 'body': 'Routing is ..'},
    {'id': 2, 'title': 'view', 'body': 'View is ..'},
    {'id': 3, 'title': 'Model', 'body': 'Model is ..'}
]


# HTML 템플릿 함수
def HTMLTemplate(articleTag):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'

    return f'''
    <html>
    <body>
        <h1><a href="/">Django</a></h1>
        <ul>
            {ol}
        </ul>
        {articleTag}
        <ul>
            <li><a href="/create/">create</a></li>
            <li>
                <form action="/delete/" method="post">
                    <input type="submit" value="delete">
                </form>
            </li>
        </ul>
    </body>
    </html>
    '''


# 읽기 (Read) 기능
def read(request, id):
    global topics
    article = next((topic for topic in topics if topic["id"] == int(id)), None)
    if article is None:
        return HttpResponse("Not Found", status=404)

    articleTag = f'<h2>{article["title"]}</h2>{article["body"]}'
    return HttpResponse(HTMLTemplate(articleTag))


# 생성 (Create) 기능
@csrf_exempt
def create(request):
    global nextId, topics
    if request.method == 'POST':
        title = request.POST.get('title', '')
        body = request.POST.get('body', '')
        topics.append({'id': nextId, 'title': title, 'body': body})
        nextId += 1
        return redirect('/')

    articleTag = '''
    <form action="/create/" method="post">
        <p><input type="text" name="title" placeholder="Title"></p>
        <p><textarea name="body" placeholder="Body"></textarea></p>
        <p><input type="submit" value="Create"></p>
    </form>
    '''
    return HttpResponse(HTMLTemplate(articleTag))


# 삭제 (Delete) 기능
@csrf_exempt
def delete(request):
    global topics
    if request.method == 'POST':
        topics.clear()  # 모든 데이터 삭제 (영상 코드가 특정 ID를 삭제하는지 불명확)
    return redirect('/')

