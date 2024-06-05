
from .models import Curso,disciplina,projeto
from django.shortcuts import render, get_object_or_404, redirect
from .forms import DisciplinaForm, ProjetoForm

def criar_projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('curso:projetos_view')
    else:
        form = ProjetoForm()
    return render(request, 'curso/criar_projeto.html', {'form': form})



def editar_projeto(request, pk):
    projeto_instance = get_object_or_404(projeto, pk=pk)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto_instance)
        if form.is_valid():
            form.save()
            return redirect('curso:projetos_view')
    else:
        form = ProjetoForm(instance=projeto_instance)
    return render(request, 'curso/editar_projeto.html', {'form': form})

def remover_projeto(request, pk):
    projeto_instance = get_object_or_404(projeto, pk=pk)
    if request.method == 'POST':
        projeto_instance.delete()
        return redirect('curso:projetos_view')
    return render(request, 'curso/remover_projeto.html', {'projeto': projeto_instance})


def criar_disciplina(request):
    if request.method == 'POST':
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('curso/todasDisciplinas.html')
    else:
        form = DisciplinaForm()
    return render(request, 'curso/criar_disciplina.html', {'form': form})



def editar_disciplina(request, pk):
    disciplina_instance = get_object_or_404(disciplina, pk=pk)
    if request.method == 'POST':
        form = DisciplinaForm(request.POST, instance=disciplina_instance)
        if form.is_valid():
            form.save()
            return redirect('curso:todasDisciplinas_view')
    else:
        form = DisciplinaForm(instance=disciplina_instance)
    return render(request, 'curso/editar_disciplina.html', {'form': form})

def remover_disciplina(request, pk):
    disciplina_instance = get_object_or_404(disciplina, pk=pk)
    if request.method == 'POST':
        disciplina_instance.delete()
        return redirect('curso/todasDisciplinas.html')
    return render(request, 'curso/remover_disciplina.html', {'disciplina': disciplina_instance})


def intro_view(request):
    # Query all Curso objects
    cursos = Curso.objects.all()

    # Pass cursos to the template
    context = {
        'cursos': cursos
    }

    # Render the template with the provided context
    return render(request, 'curso/intro.html', context)


def todasDisciplinas_view(request):
    disciplinas = disciplina.objects.all().order_by('ects')
    return render(request, 'curso/todasDisciplinas.html', {'disciplinas': disciplinas})


def disciplina_details(request, disciplina_id):
    disciplinas = get_object_or_404(disciplina, pk=disciplina_id)
    return render(request, 'curso/disciplina_details.html', {'disciplina': disciplinas})

def disciplina_view(request, disciplina_id):
    context = {
        'disciplina': disciplina.objects.get(id=disciplina_id),
    }
    return render(request, "curso/disciplina.html", context)


def project_details(request, project_id):
    project = get_object_or_404(projeto, pk=project_id)
    return render(request, 'curso/project_details.html', {'project': project})

def projetos_view(request):
    projetos = projeto.objects.all().order_by('ano')
    return render(request, 'curso/projetos.html', {'projetos': projetos})

def disciplina_detail_view(request, disciplina_id):
    disciplinas = get_object_or_404(disciplina, pk=disciplina_id)
    return render(request, 'disciplina_detail.html', {'disciplina': disciplinas})