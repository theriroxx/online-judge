# views.py in problems app
from django.shortcuts import render, redirect, get_object_or_404
from .models import Problem, CodeSubmission
from .forms import ProblemForm, TestCaseFormSet
from submit.forms import CodeSubmissionForm
from submit.views import run_code  # Import the run_code function
from django.contrib.auth.decorators import login_required

def problem_list(request):
    problems = Problem.objects.all()
    return render(request, 'problems/problem_list.html', {'problems': problems})

def create_problem(request):
    if request.method == 'POST':
        form = ProblemForm(request.POST)
        formset = TestCaseFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            problem = form.save()
            test_cases = formset.save(commit=False)
            for test_case in test_cases:
                test_case.problem = problem
                test_case.save()
            return redirect('problem_list')
    else:
        form = ProblemForm()
        formset = TestCaseFormSet()
    return render(request, 'problems/problem_form.html', {'form': form, 'formset': formset})

def edit_problem(request, problem_id):
    problem = get_object_or_404(Problem, id=problem_id)
    if request.method == 'POST':
        form = ProblemForm(request.POST, instance=problem)
        formset = TestCaseFormSet(request.POST, instance=problem)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('problem_list')
    else:
        form = ProblemForm(instance=problem)
        formset = TestCaseFormSet(instance=problem)
    return render(request, 'problems/problem_form.html', {'form': form, 'formset': formset, 'problem': problem})

def problem_detail(request, problem_id):
    problem = get_object_or_404(Problem, id=problem_id)
    test_cases = problem.test_cases.all()
    return render(request, 'problems/problem_detail.html', {'problem': problem, 'test_cases': test_cases})


@login_required(login_url='/auth/login/')
def submit_code(request, problem_id):
    problem = get_object_or_404(Problem, id=problem_id)
    if request.method == 'POST':
        form = CodeSubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.problem = problem
            submission.save()
            output = run_code(submission.lang, submission.code, submission.input)
            submission.output = output
            submission.save()
            return render(request, "problems/result.html", {'submission': submission, 'problem': problem})
    else:
        form = CodeSubmissionForm()

    return render(request, 'problems/submit_code.html', {'form': form, 'problem': problem})
