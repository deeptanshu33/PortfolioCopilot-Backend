from django.urls import path

from research.views import GenerateReportView
urlpatterns = [
    path('generate_report/', GenerateReportView.as_view(), name='generate-report'),
]