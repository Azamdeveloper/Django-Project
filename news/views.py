from django.shortcuts import render
from news.models import Course, Teacher
from news.forms import ApplicationForm

# Create your views here.

def home_page(request):
    kurslar = Course.objects.all()
    teachers = Teacher.objects.all()
    print(kurslar)
    return render(request, 'home_list.html', {'courses':kurslar, 'teachers':teachers})


def about_detail(request, pk):
    kurs = Course.objects.get(pk=pk)
    form = ApplicationForm(request.POST or None)
    is_success = False
    if request.method == 'POST' and form.is_valid():
        instance = form.save(commit=False)
        is_success=True
        instance.course = Course
        instance.save()
        form =ApplicationForm()    
    return render(request, 'about_detail.html',
    {'course': kurs, 'form': form, 'is_success': is_success})













