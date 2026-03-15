import asyncio
from celery import shared_task


from research.ai_agent import _call_agent_async

# from research.models import ResearchReport 

# @shared_task
# def run_research_agent(report_id):
#     report = ResearchReport.objects.get(id=report_id)
#     report.status = ResearchReport.Status.RUNNING
#     report.save()

#     state = run_agent(report)

#     report.final_report = state
#     report.status = ResearchReport.Status.COMPLETED
#     report.save()


@shared_task
def call_agent(thesis: str):
    return asyncio.run(_call_agent_async(thesis))