from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from .models import Curso
from .forms import CursoForm 




def curso(request):
    cursos=Curso.objects.all()
    return render(request,"inicio/cursos.html",{'cursos':cursos})

def eliminarCurso(request, id, confirmacion='inicio/confirmarEliminacion.html'):
    curso = get_object_or_404(Curso, id=id)
    if request.method == 'POST':
        curso.delete()
        cursos = Curso.objects.all()
        return render(request, "inicio/cursos.html", {'cursos': cursos})
    return render(request, confirmacion, {'object': curso})


def registrar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES)  # Incluye request.FILES para la imagen
        if form.is_valid():
            form.save()
            return curso(request)
    else:
        form = CursoForm()
    
    return render(request, 'inicio/registrar_curso.html', {'form': form})

def consultarCursoIndividual(request, id):
    curso=Curso.objects.get(id=id)
    return render(request,"inicio/formEditarCurso.html",{'curso':curso})

def editarCurso(request, id):
    curso = get_object_or_404(Curso, id=id)
    form = CursoForm(request.POST, instance=curso)

    if form.is_valid():
        form.save() 
        cursos=Curso.objects.all()
        return render(request,"inicio/cursos.html",{'cursos':cursos})
    else:
        return render(request,"inicio/formEditarCurso.html",{'curso':curso})