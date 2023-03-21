from django import forms
from course.models import AddCourseModel
from .models import courseApplication

class courseForm(forms.Form):
    Discussions_Sections = forms.ChoiceField(choices= courseApplication.Course_Choices)

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(courseForm, self).form_valid(form)
