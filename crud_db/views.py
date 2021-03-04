from django.shortcuts import render, HttpResponseRedirect
from .forms import UserForm
from .models import User_Info

def home(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            add = User_Info(name=form.cleaned_data['name'], email=form.cleaned_data['email'])
            add.save()
            form = UserForm()
    else:
        form = UserForm()
    data = User_Info.objects.all()
    return render(request, 'crud_db/home.html', {'form':form, 'data':data})

def edit(request, id):
    if request.method == "POST":
        key = User_Info.objects.get(pk=id)
        form = UserForm(request.POST, instance=key)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        key = User_Info.objects.get(pk=id)
        edit_form = UserForm(instance=key)
        data = User_Info.objects.all()
    return render(request, 'crud_db/home.html', {'edit_form':edit_form, 'data':data})

def delete(request, id):
    if request.method == "POST":
        key = User_Info.objects.get(pk=id)
        key.delete()
        return HttpResponseRedirect('/')