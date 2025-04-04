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

