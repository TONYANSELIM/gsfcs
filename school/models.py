from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

FACILITY_CATEGORY = (
    ('F1class', 'F1class'),
    ('f2class', 'f2class'),
    ('f3class', 'f3class'),
    ('f4class', 'f4class'),
    ('Offices', 'Offices'),
    ('Laboratory', 'Laboratory'),
    ('Library', 'Library'),
    ('Toilets', 'Toilets'),
    ('Water', 'Water'),
    ('Sports', 'Sports'),
    ('Others', 'Others'),
)
MAINTENANCE_CATEGORY = (
    ('Emergency', 'Emergency'),
    ('Preventive', 'Preventive'),
    ('Predictive', 'Predictive'),
)

class District(models.Model):
    DistrictName = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.DistrictName

class Role(models.Model):
    RoleName = models.CharField(max_length=100, unique=True)
    DistrictName = models.ForeignKey(District, to_field='DistrictName', on_delete=models.CASCADE)

    def __str__(self):
        return self.RoleName



class DSchool(models.Model):
    DSchoolID = models.AutoField(primary_key=True)
    DSchoolName = models.CharField(max_length=100, unique=True)
    Ward = models.CharField(max_length=100, unique=True)
    Street = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.DSchoolName

class SFacility(models.Model):
    FacilityID = models.AutoField(primary_key=True)
    FacilityName = models.CharField(max_length=100)
    FacilityImage = models.ImageField(upload_to='facilities/')
    FacilityCategory = models.CharField(max_length=100, choices=FACILITY_CATEGORY, default='F1class')
    school = models.ForeignKey(DSchool, on_delete=models.CASCADE, related_name='facilities', default=1) 
    def generate_facility_number(self):
        return f"{self.school.DSchoolName}/{self.FacilityName}/{self.get_FacilityCategory_display()}/{self.FacilityID}"

    def __str__(self):
        return f"{self.FacilityName} - Category: {self.get_FacilityCategory_display()}"

class SchoolAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    SchoolAdminID = models.CharField(max_length=100, unique=True, null=True, blank=True)
    AdminMname = models.CharField(max_length=50, null=True, blank=True)
    AdminSname = models.CharField(max_length=50, null=True, blank=True)
    AdminPhoneNumber = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.AdminMname if self.AdminMname else 'Unnamed Admin'

class Announcement(models.Model):
    Title = models.CharField(max_length=200)
    Content = models.TextField()
    SchoolAdminID = models.ForeignKey('SchoolAdmin', on_delete=models.CASCADE)
    Picture = models.ImageField(upload_to='announcement_pictures', null=True, blank=True)
    TimePosted = models.DateTimeField(default=timezone.now)
    DSchoolID = models.ForeignKey('DSchool', on_delete=models.CASCADE, default=1)
    Email = models.EmailField(blank=True, null=True)
    Comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.Title

class Maintanance(models.Model):
    MaintananceID = models.AutoField(primary_key=True)
    MaintananceDescription = models.TextField()
    MaintanancePicture = models.ImageField(upload_to='maintenances/')
    category = models.CharField(max_length=50, choices=MAINTENANCE_CATEGORY, null=True)
    facility = models.ForeignKey('SFacility', on_delete=models.CASCADE, related_name='maintenances', default=1)
    confirmed = models.BooleanField(default=False)
    receipt = models.FileField(upload_to='maintenance_receipts/', null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
 

    def __str__(self):
        return f'Maintenance {self.MaintananceID}'


class Payment(models.Model):
    PaymentID = models.AutoField(primary_key=True)
    Amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Payment {self.PaymentID} - {self.Amount}'
    
class Profile(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    image = models.ImageField(default='avatar.jpg', upload_to='profile_images')

    def __str__(self):
        return f'{self.staff.username} - Profile'





    
