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

def ver_livros(request, id):
    if request.session.get('usuario'):
        livro = Livros.objects.get(id = id)
        if request.session.get('usuario') == livro.usuario.id:
            usuario = Usuario.objects.get(id = request.session['usuario'])
            categoria_livro = Categoria.objects.filter(usuario = request.session.get('usuario'))
            emprestimos = Emprestimos.objects.filter(livro = livro)
            form = CadastroLivro()
            form.fields['usuario'].initial = request.session['usuario']
            form.fields['categoria'].queryset = Categoria.objects.filter(usuario = usuario)
            
            form_categoria = CategoriaLivro()
            usuarios = Usuario.objects.all()

            livros_emprestar = Livros.objects.filter(usuario = usuario).filter(emprestado = False)
            livros_emprestados = Livros.objects.filter(usuario = usuario).filter(emprestado = True)
            
            return render(request, 'ver_livro.html', {'livro': livro,
                                                    'categoria_livro': categoria_livro,
                                                    'emprestimos': emprestimos,
                                                    'usuario_logado': request.session.get('usuario'),
                                                    'form': form,
                                                    'id_livro': id,
                                                    'form_categoria': form_categoria,
                                                    'usuarios': usuarios,
                                                    'livros_emprestar': livros_emprestar,
                                                    'livros_emprestados': livros_emprestados})
        else:
            return HttpResponse('Esse livro não é seu')
    return redirect('/auth/login/?status=2')