from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt

nextId = 4
topics = [
    {'id': 1, 'title': 'routing', 'body': 'Routing is ..'},
    {'id': 2, 'title': 'view', 'body': 'View is ..'},
    {'id': 3, 'title': 'Model', 'body': 'Model is ..'}
]

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
        </ul>
    </body>
    </html>
    '''

urlpatterns = [
    path('', views.index, name='index'),  # 블로그 홈 페이지로 연결
]
from django.urls import path
from . import views  # 같은 폴더의 views.py를 불러옴

urlpatterns = [
    path("create/", views.create, name="create"),  # 여기 등록!
]

from django.urls import path
from . import views  # 같은 앱 내의 views 가져오기

urlpatterns = [
    path("create/", views.create, name="create"),  # create 뷰 연결
]

topics = [
    {'id': 1, 'title': 'routing', 'body': 'Routing is ..'},
    {'id': 2, 'title': 'view', 'body': 'View is ..'},
    {'id': 3, 'title': 'Model', 'body': 'Model is ..'}
]

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
