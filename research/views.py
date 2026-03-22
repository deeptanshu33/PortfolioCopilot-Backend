import uuid
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from research.models import ResearchReport
from research.serializers import ResearchInputSerializer
from rest_framework.permissions import IsAuthenticated
from research.tasks import call_agent


class GenerateReportView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        serializer = ResearchInputSerializer
        user = request.user
        data = request.data
        thesis = data.get('thesis')
        if not serializer.is_valid(data):
            return Response({"message": "invalid data"}, status=status.HTTP_400_BAD_REQUEST)
        ## generate a random id for the web socker connection
        ws_id = str(uuid.uuid4())
        report = ResearchReport.objects.create(
            user = user, 
            thesis = thesis,
            status = ResearchReport.Status.PENDING
        )
        task = call_agent.delay(thesis, ws_id, report)

        return Response({
            "task_id": task.id,
            "ws_id": ws_id
        }, status=status.HTTP_200_OK)