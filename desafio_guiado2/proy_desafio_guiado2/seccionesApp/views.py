from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("""
                        <h1>Esta es la seccion Home<h1>
                        <p>Bienvenido al desafio guiado 2!!<p>
                        <img src="https://www.telemundo.com/sites/nbcutelemundo/files/images/article/cover/2015/06/24/perro_saltando_.jpg" alt="copito" style="max-width: 400px;">
                        """)
    
def about(request):
    return HttpResponse("""
                        <h1>Esta es la seccion About<h1>
                        <p>El desafio consiste en crear una aplicación web donde tenga la vista Home, About y Contact.<p>
                        <img src="https://media.istockphoto.com/id/178622320/es/foto/perro-mirando-hacia-arriba-y-se%C3%B1alando.jpg?s=612x612&w=0&k=20&c=DCk4_Adg5fkPsOduxPOnsFfDpwBNn3laSp_zvykcqpo=" alt="thor" style="max-width: 400px;">
                        """)
    
def contact(request):
    return HttpResponse("""
                        <h1>Esta es la seccion Contact<h1>
                        <p>Por favor completa el siguiente formulario..<p>
                        <form>
                        <div class="mb-3">
                            <label for="exampleInputnombrecompleto" class="form-label">Nombre Completo</label>
                            <br>
                            <input type="name" class="form-control" id="exampleInputnombrecompleto" aria-describedby="emailHelp">
                            
                        </div>
                        <div class="mb-3">
                            <label for="exampleInputProfesion" class="form-label">Profesion</label>
                            <br>
                            <input type="profesion" class="form-control" id="exampleInputProfesion">
                        </div>
                        <br>
                        <button type="submit" class="btn btn-primary">Submit</button>
                        </form>
                        <img src="https://media.istockphoto.com/id/1389862392/es/foto/mano-de-mujer-acariciando-a-un-gato-de-jengibre-sobre-fondo-blanco-aislado.jpg?s=612x612&w=0&k=20&c=jDM2adnA-aY9rRTep1Eb0OmldaWuusdb8FE80hOw4Uk=" alt="cat" style="max-width: 400px;">
                        """)