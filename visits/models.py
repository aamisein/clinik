from django.db import models
from jdatetime import datetime  # استفاده از jdatetime برای تاریخ شمسی
from django_jalali.db import models as jmodels
import jdatetime


class Service(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Visit(models.Model):
    first_name = models.CharField(max_length=100 ,verbose_name='نام')
    last_name = models.CharField(max_length=100 , verbose_name='نام خانوادگی')
    phone = models.CharField(max_length=11 ,verbose_name='شماره همراه')

    service = models.ForeignKey(Service, on_delete=models.CASCADE ,verbose_name=' خدمات')
    current_visit_date = jmodels.jDateField(verbose_name='تاریخ ویزیت')
    next_visit_date = jmodels.jDateField(verbose_name='تاریخ ویزیت بعدی', null=True, blank=True)
    SMS_sent = models.BooleanField(verbose_name='پیامک داده شده', default=False )

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.service.name}"

    # تبدیل تاریخ میلادی به شمسی
    # def get_current_visit_date_jalali(self):
    #     return datetime.fromgregorian(date=self.current_visit_date).strftime('%Y/%m/%d')

    # def get_next_visit_date_jalali(self):
    #     if self.next_visit_date:
    #         return datetime.fromgregorian(date=self.next_visit_date).strftime('%Y/%m/%d')
    #     return None



