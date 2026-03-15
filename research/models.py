from django.db import models
from accounts.models import Profile

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class ResearchReport(BaseModel):
    class Status(models.TextChoices):
        PENDING = "PD", "Pending"
        RUNNING = "RU", "Running"
        COMPLETED = "CP", "Completed"
        FAILED = "FD", "Failed"
    
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    thesis = models.TextField()
    status = models.CharField(choices=Status.choices, max_length=2, default=Status.PENDING)
    final_report = models.JSONField(null=True, blank=True)
    confidence_score = models.FloatField(null=True, blank=True)

class ReportState(BaseModel):
    report = models.OneToOneField(ResearchReport, on_delete=models.CASCADE)
    state_data = models.JSONField(default=dict)
    tool_history = models.JSONField(default=dict)
    iteration_count = models.IntegerField(default=0)

class ToolLog(BaseModel):
    report = models.ForeignKey(ResearchReport, on_delete=models.CASCADE)
    tool_name = models.CharField(max_length=20)
    input_payload = models.JSONField()
    output_payload = models.JSONField()
    execution_time = models.TimeField()