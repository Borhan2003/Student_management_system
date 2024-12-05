from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Student
from .forms import StudentForm

# View for the student list
def index(request):
    return render(request, 'students/index.html', {
        'students': Student.objects.all()
    })

# View to add a new student
def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # Save the form data to create a new student
            form.save()
            return render(request, 'students/add.html', {
                'form': StudentForm(),  # Empty form for new addition
                'success': True
            })
    else:
        form = StudentForm()
    
    return render(request, 'students/add.html', {
        'form': form
    })

# View for viewing a specific student (redirecting to index for now)
def view_student(request, id):
    student = get_object_or_404(Student, pk=id)
    # For now, this just redirects to index
    return HttpResponseRedirect(reverse('index'))

def edit(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
      form.save()
      return render(request, 'students/edit.html', {
        'form': form,
        'success': True
      })
  else:
    student = Student.objects.get(pk=id)
    form = StudentForm(instance=student)
  return render(request, 'students/edit.html', {
    'form': form
  })
def delete(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    student.delete()
  return HttpResponseRedirect(reverse('index'))
