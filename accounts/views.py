from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import CustomUserForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')
    else:
        form = CustomUserForm()
    return render(request, 'index.html', {'form': form})
