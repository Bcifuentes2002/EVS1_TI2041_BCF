from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def vista2 (request):
    html = """
            <html>
            <h2>hola mundo</h2>
            <br>
            <p>Texto normal y ...
            <font size="5" color="#0000ff"> Texto distinto. </font></p>
            </html>
            
            """
    return HttpResponse(html)