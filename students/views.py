from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Student


def student_list(request):
    students = Student.objects.all()
    q = request.GET.get("q", "").strip()
    section = request.GET.get("section", "")
    if q:
        students = students.filter(
            Q(first_name__icontains=q) | Q(last_name__icontains=q) | Q(student_id__icontains=q)
        )
    if section:
        students = students.filter(section=section)
    sections = Student.objects.order_by("section").values_list("section", flat=True).distinct()
    return render(request, "students/list.html", {
        "students": students, "q": q, "section": section, "sections": sections,
        "total": Student.objects.count(),
    })


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, "students/detail.html", {"student": student})