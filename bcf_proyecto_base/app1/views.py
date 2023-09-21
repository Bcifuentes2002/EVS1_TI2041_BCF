from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def vista1 (request):
    html = """
    <html>
    <head>
    <h1 style="color:red">Hola Mundo</h1>
    <header>vista1</header>
    </head>

    <p>lorem<p>
    </html>
    """
    return HttpResponse(html)



