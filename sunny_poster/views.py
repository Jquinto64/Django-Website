from django.shortcuts import render
from sunny_poster.models import Section

# Create your views here.
def section_index(request):
    sections = Section.objects.all()
    context = {
        "Sections": sections,
    }
    return render(request, "section_index.html", context)

def section_detail(request, pk):
    sections = Section.objects.all()
    section = Section.objects.get(pk=pk)
    context = {
        "Sections": sections,
        "Section": section,
    }
    if pk == 1:
        return render(request, "section_detail.html", context)
    elif pk == 2:
        return render(request, "section_detail.html", context)
    elif pk == 3:
        return render(request, "section_detail.html", context)
    elif pk == 4:
        return render(request, "methods.html", context)
    elif pk == 5:
        return render(request, "results.html", context)
    elif pk == 6:
        return render(request, "section_detail.html", context)
    elif pk == 7:
        return render(request, "section_detail.html", context)
    elif pk == 8:
        return render(request, "acknowledgements.html", context)