from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10, null=True)
    dob = models.DateField()
    gender = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=100, null=True)
    empid = models.CharField(max_length=10, null=True)
    department = models.CharField(max_length=20, null=True)
    designation = models.CharField(max_length=20, null=True)
    jdate = models.DateField()

    def __str__(self):
        return self.user.username


class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    is_present = models.BooleanField(default=True)
    marked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['employee', 'date'],
                name='unique_daily_attendance'
            )
        ]

    def __str__(self):
        return f"{self.employee.user.username} - {self.date}"


class LeaveRequest(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )

    LEAVE_TYPE_CHOICES = (
        ('Sick', 'Sick Leave'),
        ('Casual', 'Casual Leave'),
        ('Paid', 'Paid Leave'),
        ('Unpaid', 'Unpaid Leave'),
    )

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='leaves')
    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPE_CHOICES)
    
    start_date = models.DateField()
    end_date = models.DateField()
    
    reason = models.TextField()
    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    
    applied_on = models.DateTimeField(default=timezone.now)

    def clean(self):
        from django.core.exceptions import ValidationError

        if self.end_date < self.start_date:
            raise ValidationError("End date cannot be before start date")

    @property
    def total_days(self):
        return (self.end_date - self.start_date).days + 1

    def __str__(self):
        return f"{self.employee} - {self.leave_type} ({self.status})"