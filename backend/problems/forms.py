from django import forms
from .models import Problem, TestCase

class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['title', 'description', 'input', 'output', 'constraints']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'input': forms.Textarea(attrs={'rows': 4}),
            'output': forms.Textarea(attrs={'rows': 4}),
            'constraints': forms.Textarea(attrs={'rows': 4}),
        }

class TestCaseForm(forms.ModelForm):
    class Meta:
        model = TestCase
        fields = ['input_data', 'expected_output']
        widgets = {
            'input_data': forms.Textarea(attrs={'rows': 2}),
            'expected_output': forms.Textarea(attrs={'rows': 2}),
        }

TestCaseFormSet = forms.inlineformset_factory(
    Problem, TestCase, form=TestCaseForm, extra=1, can_delete=True
)
