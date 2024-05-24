from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mascotas(request):
    return HttpResponse("""
                        <h2>Esta es mi mascota</h2>
                        <p>mi perro<p>
                        <img src="https://img.freepik.com/fotos-premium/cachorro-joven-sonriendo-camara_1043470-52499.jpg" alt="thor">
                        """)