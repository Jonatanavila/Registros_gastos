from django.shortcuts import render, redirect
from .models import * #models
from .forms import GastoForm #forms


def gastos(request):
	form=GastoForm()
	if request.method == 'POST':
		tar=GastoForm(request.POST)
		if tar.is_valid():
			instancia= tar.save(commit=False)
			instancia.save()
			return redirect('/')
	return render(request,'gasto_total.html',{'form': form})

def lista(request):
    gastos = Gasto.objects.all() 
    return render(request, 'gastos.html', {'gastos': gastos})


