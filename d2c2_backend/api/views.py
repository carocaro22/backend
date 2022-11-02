from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import QuestionSerializer
from .models import Question

def index(request):
    return HttpResponse("Hello, world. You're at the main index.")

# Create your views here.
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('id')
    serializer_class = QuestionSerializer