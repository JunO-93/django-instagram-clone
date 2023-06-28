from django.shortcuts import render
from rest_framework.views import APIView
from .settings import BASE_DIR

class Sub(APIView):
    def get(self, request):
        print("get으로 호출")
        return render(request, 'junstagram/main.html')
    
    def post(self, request):
        print("post으로 호출")
        return render(request, 'junstagram/main.html')
