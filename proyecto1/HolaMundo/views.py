from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hola(request):
    return HttpResponse("""
                        <h1>hola desde otro metodo<h1>
                        <p>Esto es un parrafo de Django<p>
                        """)
    
def index(request):
    return HttpResponse("""
                        Hola Mundo!!!!
                        """)