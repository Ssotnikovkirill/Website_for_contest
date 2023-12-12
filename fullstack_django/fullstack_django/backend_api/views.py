from django.shortcuts import *
from rest_framework.views import APIView
from .models import SitePost
from .serializer import SitePostSerializer
from rest_framework.response import Response
# Create your views here.

class SitePostView(APIView):
    def get(self, request):
        output = [
            {
                "title": output.title,
                "description": output.description
            } for output in SitePost.objects.all()
        ]
        return Response(output)
    
    def post(self, request):
        serializer = SitePostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self, request):
        output = SitePost.objects.all().delete()
        return Response()
