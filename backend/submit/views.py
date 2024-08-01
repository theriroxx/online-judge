from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from submit.forms import CodeSubmissionForm
from django.contrib.auth.decorators import login_required
import os
import uuid
import subprocess
from pathlib import Path

# def submit(request):
#     if request.method == 'POST':
#         form = CodeSubmissionForm(request.POST)
#         if form.is_valid():
#             submission = form.save()
#             code = request.POST.get('code')
#             lang = request.POST.get('lang')
#             input = request.POST.get('input')
#             submission.input = submission.input.replace('\r', '')
#             submission.code = submission.code.replace('\r', '')
#             output = run_code(
#                 submission.lang, submission.code, submission.input
#             )
#             submission.output = output
#             submission.save()
#             return render(request, "result.html", {'submission': submission})
#     else:
#         form = CodeSubmissionForm()
        
#     return render(request, 'index.html', {'form': form})


def run_code(lang, code, input):
    base_path = Path(settings.BASE_DIR)
    directories = {'codes', 'inputs', 'outputs'}

    input = input.replace('\r', '')
    code = code.replace('\r', '')
    for directory in directories:
        dir_path = base_path / directory
        if not dir_path.exists():
            dir_path.mkdir(parents=True, exist_ok=True)

    codes_dir = base_path / "codes"
    input_dir = base_path / "inputs"
    output_dir = base_path / "outputs"

    unique = str(uuid.uuid4())

    code_file_name = unique + "." + lang
    input_file_name = unique + ".txt"
    output_file_name = unique + ".txt"

    code_file_path = codes_dir / code_file_name
    input_file_path = input_dir / input_file_name
    output_file_path = output_dir / output_file_name

    with open(code_file_path, "w") as code_file:
        code_file.write(code)

    with open(input_file_path, "w") as input_file:
        input_file.write(input)

    if lang == "cpp":
        exe_path = codes_dir / unique
        compile_result = subprocess.run(
            ["clang++", str(code_file_path), "-o", str(exe_path)]
        )
        if compile_result.returncode == 0:
            with open(input_file_path, "r") as input_file:
                with open(output_file_path, "w") as output_file:
                    subprocess.run(
                        [str(exe_path)],
                        stdin=input_file,
                        stdout=output_file,
                    )
    elif lang == "py":
        with open(input_file_path, "r") as input_file:
            with open(output_file_path, "w") as output_file:
                subprocess.run(
                    ["python", str(code_file_path)],
                    stdin=input_file,
                    stdout=output_file,
                )

    with open(output_file_path, "r") as output_file:
        output_data = output_file.read()

    return output_data