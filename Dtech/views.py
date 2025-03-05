from django.shortcuts import render
from django.views.generic import ListView
from .models import subject

# Create your views here.


class classview(ListView):
    model = subject
    template_name = "task_view.html"


def search_subject(request):
    query = request.GET.get('q', '')  # รับคำค้นหาจาก URL
    subjects = []
    
    if query:
        # ค้นหาผลลัพธ์ตามคำค้นหาจากทั้ง name และ code
        subjects = subject.objects.filter(name__icontains=query) | subject.objects.filter(code__icontains=query)
    
    return render(request, 'search_subject.html', {'subjects': subjects, 'query': query})
