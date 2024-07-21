from django.db import models

class Problem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    input = models.TextField()
    output = models.TextField()
    constraints = models.TextField()

    def __str__(self):
        return self.title

class TestCase(models.Model):
    problem = models.ForeignKey(Problem, related_name='test_cases', on_delete=models.CASCADE)
    input_data = models.TextField()
    expected_output = models.TextField()

    def __str__(self):
        return f'Test Case for {self.problem.title}'

class CodeSubmission(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name='submissions')
    lang = models.CharField(max_length=100)
    code = models.TextField()
    input = models.TextField(null=True, blank=True)
    output = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

