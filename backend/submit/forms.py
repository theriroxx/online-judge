from django import forms
from submit.models import CodeSubmission

Lang_choices = [
    ('py', 'Python'),
    ('cpp', 'C++'),
    ('C','c'),
]

class CodeSubmissionForm(forms.ModelForm):
    lang = forms.ChoiceField(choices=Lang_choices)

    class Meta:
        model = CodeSubmission
        fields = ['lang', 'code', 'input']
