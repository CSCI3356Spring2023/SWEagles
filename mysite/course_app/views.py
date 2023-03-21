from django.shortcuts import render
from .forms import courseForm

def course_app_page(request):
    form = courseForm()
    if request.method == 'POST':
        form = courseForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = courseForm()



    return render(request, 'course_app_page.html', {'form': form})
