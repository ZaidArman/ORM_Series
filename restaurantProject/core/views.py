from django.shortcuts import render
from .forms import restuarantForm
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = restuarantForm(request.POST or None)
        if form.is_valid():
            # form.save()
            print(form.cleaned_data)
        else:
            return render(request, 'index.html', {'form': form})
    context = {'form': restuarantForm()}
    return render(request, 'index.html', context)