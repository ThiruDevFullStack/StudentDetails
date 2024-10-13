from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from django.utils.datastructures import MultiValueDictKeyError

from .models import StudentDetails


# Create your views here.
def indexPage(request):
    # if request.method=='POST':
    #     rollno=request.POST['rollno']
    #     reg_no=request.POST['register_no']
    #     name=request.POST['fullname']
    #     dob=request.POST['birthdate']
    #     gender=request.POST['gender']
    #     father=request.POST['father_name']
    #     mother=request.POST['mother_name']
    #     email=request.POST['email']
    #     phone=request.POST['phone']
    #     address=request.POST['address']
    #     student=StudentDetails(roll_no=rollno,reg_no=reg_no,full_name=name,birth_date=dob,gender=gender,father_name=father,mother_name=mother,email=email,phone_no=phone,address=address)
    #     student.save()
    #     return HttpResponse("<h2>Successfully inserted !</h2>")
    # else:
    #     return HttpResponse("<h2>Please enter all datas</h2>")
    return render(request,'MyApp/index.html')

def addData(request):
    try:
        if request.method == 'POST':
            rollno = request.POST['rollno']
            reg_no = request.POST['register_no']
            name = request.POST['fullname']
            dob = request.POST['birthdate']
            gender = request.POST['gender']
            father = request.POST['father_name']
            mother = request.POST['mother_name']
            email = request.POST['email']
            phone = request.POST['phone']
            address = request.POST['address']
            student = StudentDetails(roll_no=rollno, reg_no=reg_no, full_name=name, birth_date=dob, gender=gender,
                                     father_name=father, mother_name=mother, email=email, phone_no=phone,
                                     address=address)
            student.save()
            return HttpResponse("""
                 <script>
                     alert("Successfully Added !");
                     window.location.href = 'http://127.0.0.1:8000/'; 
                 </script>
            """)
    except MultiValueDictKeyError as e:
        return HttpResponse("""
        <script>
        alert("Please Enter All Datas !");
        window.history.back()
        </script>
        """)


def viewData(request):
    # student=StudentDetails.objects.all()

    srch = request.GET.get("search")

    if srch:
        student = StudentDetails.objects.filter(
            Q(roll_no__icontains=srch) | Q(reg_no__icontains=srch) | Q(full_name__icontains=srch) | Q(
                email__icontains=srch))
        msg=""
        if not student.exists():
            msg=messages.error(request,"No data for your search")
    else:
        student = StudentDetails.objects.all()
        msg=messages.error(request,"Please enter value and search")
    return render(request,'MyApp/viewData.html',context={"student":student,"msg":msg})

def updateData(request):
    # student=StudentDetails.objects.all()

    srch = request.GET.get("search")

    if srch:
        student = StudentDetails.objects.filter(
            Q(roll_no__icontains=srch) | Q(reg_no__icontains=srch) | Q(full_name__icontains=srch) | Q(
                email__icontains=srch))
        msg = ""
        if not student.exists():
            msg = messages.error(request, "No data for your search")
    else:
        student = StudentDetails.objects.all()
        msg = messages.error(request, "Please enter value and search")
    return render(request,'MyApp/updateData.html',context={"student":student,"msg":msg})

def updateStudent(request,id):

    student = StudentDetails.objects.get(id=id)
    if request.method == "POST":
        data=request.POST
        rollno = data.get('rollno')
        reg_no = data.get('register_no')
        name = data.get('fullname')
        birthdate = data.get('birthdate')
        gender = data.get('gender')
        father = data.get('father_name')
        mother = data.get('mother_name')
        email = data.get('email')
        phone = data.get('phone')
        address = data.get('address')

        if rollno and reg_no and name and birthdate and gender and father and mother and email and phone and address:
            student.roll_no=rollno
            student.reg_no=reg_no
            student.full_name=name
            student.birth_date=birthdate
            student.gender=gender
            student.father_name=father
            student.mother_name=mother
            student.email=email
            student.phone_no=phone
            student.address=address

            student.save()
            return HttpResponse("""
                            <script>
                                alert("Successfully Updated !");
                                window.location.href = 'http://127.0.0.1:8000/update'; 
                            </script>
                       """)

        else:
            msg = messages.error(request, "Please enter all values")
            return render(request, 'MyApp/updateStudent.html', context={"student": student, "msg": msg})




    return render(request,'MyApp/updateStudent.html',context={"student":student})


def deleteData(request):
    srch = request.GET.get("search")

    if srch:
        student = StudentDetails.objects.filter(
            Q(roll_no__icontains=srch) | Q(reg_no__icontains=srch) | Q(full_name__icontains=srch) | Q(
                email__icontains=srch))
        msg = ""
        if not student.exists():
            msg = messages.error(request, "No data for your search")
    else:
        student = StudentDetails.objects.all()
        msg = messages.error(request, "Please enter value and search")
    return render(request, 'MyApp/deleteData.html', context={"student": student, "msg": msg})

def deleteStudent(request,id):
    student = StudentDetails.objects.get(id=id)
    name=student.full_name
    if request.method=="POST":
        student.delete()
        return HttpResponse("""
                        <script>
                            alert("Successfully Deleted !");
                            window.location.href = 'http://127.0.0.1:8000/delete'; 
                        </script>
                   """)

    return render(request, 'MyApp/deleteStudent.html',context={"name":name})

