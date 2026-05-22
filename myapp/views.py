from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.utils import timezone
from .models import *

# Create your views here.
def home(request):
    return render(request,'index.html')


def admin_home(request):
    employees = Employee.objects.all()
    total = employees.count()

    today = timezone.localdate()

    # ✅ Present
    present_records = Attendance.objects.filter(date=today).select_related('employee')
    present_ids = present_records.values_list('employee_id', flat=True)

    # ✅ Leave (approved only)
    leave_records = LeaveRequest.objects.filter(
        start_date__lte=today,
        end_date__gte=today,
        status='Approved'
    )
    leave_ids = leave_records.values_list('employee_id', flat=True)

    # ✅ Absent = not present AND not on leave
    absent_users = employees.exclude(id__in=present_ids).exclude(id__in=leave_ids)

    # ✅ Recent employees
    recent_emp = Employee.objects.all().order_by('-id')[:5]

    data = {
        'employees': employees,
        'total': total,
        'recent_emp': recent_emp,
        'present_records': present_records,
        'absent_users': absent_users,
        'leave_records': leave_records,   # ✅ add this
        'total_present': present_records.count(),
        'total_absent': absent_users.count(),
        'total_leave': leave_records.count(),
        'date': today,
    }

    return render(request, 'admin_home.html', data)
def user_login(request):
    error = ""

    if request.method == "POST":
        u = request.POST['username']
        p = request.POST.get('password')

        user = authenticate(username=u, password=p)

        if user is not None:
            login(request, user)

            # ✅ REDIRECT BASED ON ROLE
            if user.is_staff:
                return redirect('admin_home')
            else:
                return redirect('employee_home')

        else:
            error = "yes"

    return render(request, "login.html", {'error': error})

    
def add_employee(request):
    error=""
    if request.method =="POST":
        f=request.POST['first_name']
        l=request.POST['last_name']
        e=request.POST['email']
        p=request.POST.get('password')
        ph=request.POST['phone']
        dob=request.POST['dob']
        gen=request.POST['gender']
        add=request.POST['address']
        eid=request.POST['employee_id']
        dep=request.POST['department']
        post=request.POST['designation']
        jd=request.POST['join_date']
        try:
           user=User.objects.create_user(first_name=f,last_name=l,username=e,password=p)
           Employee.objects.create(user=user,mobile=ph,dob=dob,gender=gen,address=add,empid=eid,department=dep,designation=post,jdate=jd)
           error = "no"
           return redirect('admin_home')
        except:
           error="yes"
    return render(request,'add_employee.html',{'error':error})
def Logout(request):
    logout(request)
    return redirect('login')


from django.utils import timezone
def employee_home(request):
    today = timezone.localdate()

    try:
        emp = Employee.objects.get(user=request.user)
    except Employee.DoesNotExist:
        return redirect('login')

    has_marked_today = Attendance.objects.filter(employee=emp, date=today).exists()

    if request.method == 'POST':
        if not has_marked_today:
            Attendance.objects.create(employee=emp, date=today)

    return render(request, 'employee_home.html', {
        'has_marked_today': has_marked_today
    })
def leave_emp(request):
    emp = Employee.objects.get(user=request.user)
    leaves = LeaveRequest.objects.filter(employee=emp)

    return render(request, 'leave_emp.html', {'leaves': leaves})
def apply_leave(request):

    error = ""
    emp = Employee.objects.get(user=request.user)

    if request.method == "POST":
        lt = request.POST['leave_type']
        sd = request.POST['start_date']
        ed = request.POST['end_date']
        reason = request.POST['reason']

        try:
            LeaveRequest.objects.create(
                employee=emp,
                leave_type=lt,
                start_date=sd,
                end_date=ed,
                reason=reason
            )
            error = "no"
        except:
            error = "yes"

    return render(request, 'apply_leave.html', {'error': error})




