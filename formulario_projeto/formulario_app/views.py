from django.shortcuts import render, redirect
from .forms import RespostaForm

def formulario_view(request):
    if request.method == 'POST':
        form = RespostaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'formulario_app/sucesso.html')
    else:
        form = RespostaForm()
    return render(request, 'formulario_app/formulario.html', {'form': form})
