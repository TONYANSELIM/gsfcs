from django.contrib import admin
from .models import District, Role, DSchool, SFacility, Maintanance, SchoolAdmin, Announcement, Payment, Profile

admin.site.site_header = 'GSFCS Dashboard'



class DistrictAdmin(admin.ModelAdmin):
    list_display = ('DistrictName',)
    search_fields = ('DistrictName',)

class RoleAdmin(admin.ModelAdmin):
    list_display = ('RoleName',)
    search_fields = ('RoleName',)

class DSchoolAdmin(admin.ModelAdmin):
    list_display = ('DSchoolName', 'Ward', 'Street')
    search_fields = ('DSchoolName', 'Ward', 'Street')
    list_filter = ('DSchoolName',)

class SFacilityAdmin(admin.ModelAdmin):
    list_display = ('FacilityName', 'FacilityCategory',)
    search_fields = ('FacilityName', 'FacilityCategory',)
    list_filter = ('FacilityCategory',)

class MaintananceAdmin(admin.ModelAdmin):
    list_display = ('MaintananceID', 'MaintananceDescription', 'category',)
    search_fields = ('MaintananceID', 'MaintananceDescription', 'category',)
    list_filter = ('category',)

class SchoolAdminAdmin(admin.ModelAdmin):
    list_display = ('SchoolAdminID', 'AdminMname', 'AdminPhoneNumber',)
    search_fields = ('AdminFname', 'AdminMname', 'AdminLname', 'AdminEmail', 'AdminPhoneNumber',)

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('Title', 'SchoolAdminID',)
    search_fields = ('Title', 'SchoolAdminID',)
    list_filter = ('SchoolAdminID',)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('PaymentID', 'Amount',)
    search_fields = ('PaymentID', 'Amount',)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('staff', 'address', 'phone',)
    search_fields = ('staff__username', 'address', 'phone',)

# Register your models here.
admin.site.register(District, DistrictAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(DSchool, DSchoolAdmin)
admin.site.register(SFacility, SFacilityAdmin)
admin.site.register(Maintanance, MaintananceAdmin)
admin.site.register(SchoolAdmin, SchoolAdminAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Profile, ProfileAdmin)
