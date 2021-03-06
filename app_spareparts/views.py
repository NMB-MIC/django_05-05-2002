from django.shortcuts import render
from app_spareparts.models import Sparepart
from django.http import HttpResponseRedirect
from django.urls import reverse
from app_spareparts.forms import SparepartModelForm ,RestockModelForm
from django.db.models import Q 

# Create your views here.
def spareparts(request):
    search = request.GET.get('search')
    if search:
        all_parts = Sparepart.objects.filter(Q(part_number__icontains=search) | Q(name__icontains=search) | Q(maker__icontains=search))
    else:
        all_parts = Sparepart.objects.all()
    spareparts = {'spareparts':all_parts}
    return render(request,'app_spareparts/spareparts.html',context=spareparts)

def deposit(request,sparepart_id):
    one_part = Sparepart.objects.get(id=sparepart_id) 
    if request.method == 'POST':
        form = RestockModelForm(request.POST)  
        one_part.qty = int(one_part.qty) + int(form['qty'].value())
        one_part.save()
        return HttpResponseRedirect(reverse('spareparts'))
    else:
        form = SparepartModelForm() 

    spareparts = {'sparepart':one_part,'form':form}
    return render(request,'app_spareparts/deposit.html',context=spareparts)

def withdraw(request,sparepart_id):
    one_part = Sparepart.objects.get(id=sparepart_id)
    if request.method == 'POST':
        form = RestockModelForm(request.POST)  
        one_part.qty = int(one_part.qty) - int(form['qty'].value())
        one_part.save()
        return HttpResponseRedirect(reverse('spareparts'))
    else:
        form = SparepartModelForm() 

    spareparts = {'sparepart':one_part,'form':form}
    return render(request,'app_spareparts/withdraw.html',context=spareparts)

def new_sparepart(request):
    if request.method == 'POST':
        form = SparepartModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('spareparts'))
    else:
        form = SparepartModelForm()
    context = {'form':form}  
    return render(request,'app_spareparts/new_sparepart.html',context)

def delete(request,sparepart_id):
    one_part = Sparepart.objects.get(id=sparepart_id)
    one_part.delete()
    return HttpResponseRedirect(reverse('spareparts'))


