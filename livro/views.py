from datetime import date, datetime
from django.shortcuts import redirect, render
from django.http import HttpResponse
from usuarios.models import Usuario
from .models import Emprestimos, Livros, Categoria
from .forms import CadastroLivro, CategoriaLivro
from django import forms
from django.db.models import Q

def home(request):
    if request.session.get('usuario'):  
        usuario = Usuario.objects.get(id = request.session['usuario'])
        status_categoria = request.GET.get('cadastro_categoria')
        livros = Livros.objects.filter(usuario = usuario)
        total_livros = livros.count()
        form = CadastroLivro()
        form.fields['usuario'].initial = request.session['usuario']
        form.fields['categoria'].queryset = Categoria.objects.filter(usuario = usuario)     
        form_categoria = CategoriaLivro()
        usuarios = Usuario.objects.all()

        livros_emprestar = Livros.objects.filter(usuario = usuario).filter(emprestado = False)
        livros_emprestados = Livros.objects.filter(usuario = usuario).filter(emprestado = True)

        return render(request, 'home.html', {'livros': livros,
                                            'usuario_logado': request.session.get('usuario'),
                                            'form': form,
                                            'status_categoria': status_categoria,
                                            'form_categoria': form_categoria,
                                            'usuarios': usuarios,
                                            'livros_emprestar': livros_emprestar,
                                            'total_livro': total_livros,
                                            'livros_emprestados': livros_emprestados})
    else:
        return redirect('/auth/login/?status=2')