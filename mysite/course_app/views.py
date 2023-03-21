from django.shortcuts import render, redirect
from .forms import courseForm

def course_app_view(request):
    if request.method == 'POST':
        form = courseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_view_success')
    else:
        form = courseForm()
    return render(request, 'course_app_page.html', {'form': form})
