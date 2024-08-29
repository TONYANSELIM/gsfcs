from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, SchoolAdmin, SFacility, Maintanance, MAINTENANCE_CATEGORY,Announcement,DSchool
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import PasswordChangeForm


class SchoolAdminForm(forms.ModelForm):
    class Meta:
        model = SchoolAdmin
        fields = '__all__'

class DSchoolForm(forms.ModelForm):
    class Meta:
        model = DSchool
        fields = ['DSchoolName', 'Ward', 'Street']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'address', 'image']
        

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class SFacilityForm(forms.ModelForm):
    class Meta:
        model = SFacility
        fields = ['FacilityName', 'FacilityImage', 'FacilityCategory', 'school']

class MaintananceForm(forms.ModelForm):
    category = forms.ChoiceField(
        choices=MAINTENANCE_CATEGORY,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    amount = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter amount'})
    )

    class Meta:
        model = Maintanance
        fields = ['MaintananceDescription', 'MaintanancePicture', 'category', 'facility', 'confirmed', 'receipt', 'amount']
        widgets = {
            'MaintananceDescription': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'MaintanancePicture': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'receipt': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'facility': forms.Select(attrs={'class': 'form-control'}),
            'confirmed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['Title', 'Content', 'Picture', 'DSchoolID', 'Email', 'Comment']

    DSchoolID = forms.ModelChoiceField(queryset=DSchool.objects.all(), empty_label="Select School")
        
class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control'})
        
        
class CommentForm(forms.Form):
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)