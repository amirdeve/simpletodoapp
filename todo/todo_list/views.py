from django.shortcuts import render, redirect
from .models import list
from .forms import ListForm
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        form=ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items=list.objects.all
            messages.success(request, ('Items has been added to list!'))
            return render(request, 'home.html', {'all_items':all_items})

    else:
        all_items=list.objects.all
        return render(request, 'home.html', {'all_items':all_items})
