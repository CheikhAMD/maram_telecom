from django.db import models


class RepairRequest(models.Model):
    STATUS_CHOICES = [
        ('قيد المعالجة', 'قيد المعالجة'),
        ('تم الرد', 'تم الرد'),
        ('تم الإصلاح', 'تم الإصلاح'),
    ]

    user_name = models.CharField(max_length=100)
    phone_model = models.CharField(max_length=100)
    issue_description = models.TextField()
    contact_info = models.CharField(max_length=100)
    reply = models.TextField(blank=True, null=True)
    appointment_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='قيد المعالجة')
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f"{self.user_name} - {self.phone_model}"

