from django.shortcuts import render

def principal(request):

    return render(request, "inicio/principal.html")

def contacto(request):
    return render(request, "inicio/contacto.html")


def registro(request):
    return render(request, "inicio/registro.html")

def cursos(request):
    return render(request, "inicio/cursos.html")