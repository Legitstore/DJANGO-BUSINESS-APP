from django.shortcuts import render, redirect
from . models import *
from django.contrib import messages
from . forms import AddUserForm

# Create your views here.
def adduser(request):
    form = AddUserForm()
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Add user successfully')
            return redirect('adduser')
    context = {'form': form}
    return render(request, 'events/adduser.html', context)