from django.shortcuts import render, redirect
from . models import Student

def page2(request):
    return render(request, 'addStudent.html')

def addStudent(request):
    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        birthDate = request.POST['birthDate']
        course = request.POST['course']
        enrollmentDate = request.POST['enrollmentDate']

        newStudent = Student(FirstName = firstName, LastName = lastName, Email = email, DateOfBirth = birthDate, Course = course, EnrollmentDate = enrollmentDate)
        newStudent.save()

        return redirect('/')
    return render(request, 'addStudent.html')

def viewStudents(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'students' : students})

def editStudent(request, studentID):
    student = Student.objects.get(id=studentID)

    if request.method == "POST":
        student.FirstName = request.POST['firstName']
        student.LastName = request.POST['lastName']
        student.Email = request.POST['email']
        student.DateOfBirth = request.POST['birthDate']
        student.Course = request.POST['course']
        student.EnrollmentDate = request.POST['enrollmentDate']

        student.save()
        return redirect('/')
    
    return render(request, 'editStudent.html', {'student' : student})

def deleteStudent(request, studentID):
    student = Student.objects.get(id=studentID)
    student.delete()
    return redirect('/')

def confirmDelete(request, studentID):
    student = Student.objects.get(id=studentID)
    
    return render(request, 'confirmDelete.html', {'student' : student})