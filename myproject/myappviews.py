from django.http import HttpResponse

def create(request):
    article = '''
    <form action="/create/" method="POST">
        <p><input type="text" name="title" placeholder="Title"></p>
        <p><textarea name="body" placeholder="Content"></textarea></p>
        <p><input type="submit" value="Create"></p>
    </form>
    '''
    return HttpResponse(article)

