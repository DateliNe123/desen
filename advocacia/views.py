from django.shortcuts import render, get_object_or_404, redirect
from .models import Advogado, Caso
from .forms import AdvogadoForm, CasoForm

def pagina_inicial(request):
    return render(request, 'advocacia/index.html')

def lista_advogados(request):
    advogados = Advogado.objects.all()
    return render(request, 'advocacia/advogado_list.html', {'advogados': advogados})

def criar_advogado(request):
    if request.method == 'POST':
        form = AdvogadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_advogados')
    else:
        form = AdvogadoForm()
    return render(request, 'advocacia/advogado_form.html', {'form': form})

def editar_advogado(request, pk):
    advogado = get_object_or_404(Advogado, pk=pk)
    if request.method == 'POST':
        form = AdvogadoForm(request.POST, instance=advogado)
        if form.is_valid():
            form.save()
            return redirect('lista_advogados')
    else:
        form = AdvogadoForm(instance=advogado)
    return render(request, 'advocacia/advogado_form.html', {'form': form})

def excluir_advogado(request, pk):
    advogado = get_object_or_404(Advogado, pk=pk)
    if request.method == 'POST':
        advogado.delete()
        return redirect('lista_advogados')
    return render(request, 'advocacia/advogado_confirm_delete.html', {'advogado': advogado})

# Caso CRUD
def lista_casos(request):
    casos = Caso.objects.all()
    return render(request, 'advocacia/caso_list.html', {'casos': casos})

def criar_caso(request):
    if request.method == 'POST':
        form = CasoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_casos')
    else:
        form = CasoForm()
    return render(request, 'advocacia/caso_form.html', {'form': form})

def editar_caso(request, pk):
    caso = get_object_or_404(Caso, pk=pk)
    if request.method == 'POST':
        form = CasoForm(request.POST, instance=caso)
        if form.is_valid():
            form.save()
            return redirect('lista_casos')
    else:
        form = CasoForm(instance=caso)
    return render(request, 'advocacia/caso_form.html', {'form': form})

def excluir_caso(request, pk):
    caso = get_object_or_404(Caso, pk=pk)
    if request.method == 'POST':
        caso.delete()
        return redirect('lista_casos')
    return render(request, 'advocacia/caso_confirm_delete.html', {'caso': caso})
