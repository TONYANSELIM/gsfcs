# Generated by Django 5.0.6 on 2024-06-11 12:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DistrictName', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('FacilityID', models.AutoField(primary_key=True, serialize=False)),
                ('FacilityName', models.CharField(max_length=100)),
                ('FacilityImage', models.ImageField(upload_to='facilities/')),
                ('FacilityCategory', models.CharField(choices=[('Classes', 'Classes'), ('Offices', 'Offices'), ('Laboratory', 'Laboratory'), ('Library', 'Library'), ('Toilets', 'Toilets'), ('Water', 'Water'), ('Sports', 'Sports')], default='Classes', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Maintanance',
            fields=[
                ('MaintananceID', models.AutoField(primary_key=True, serialize=False)),
                ('MaintananceDescription', models.TextField()),
                ('MaintanancePicture', models.ImageField(upload_to='maintenances/')),
                ('category', models.CharField(choices=[('Emergency', 'Emergency'), ('Preventive', 'Preventive'), ('Predictive', 'Predictive')], max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('PaymentID', models.AutoField(primary_key=True, serialize=False)),
                ('Amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='SFacility',
            fields=[
                ('FacilityID', models.AutoField(primary_key=True, serialize=False)),
                ('FacilityName', models.CharField(max_length=100)),
                ('FacilityImage', models.ImageField(upload_to='facilities/')),
                ('FacilityCategory', models.CharField(choices=[('Classes', 'Classes'), ('Offices', 'Offices'), ('Laboratory', 'Laboratory'), ('Library', 'Library'), ('Toilets', 'Toilets'), ('Water', 'Water'), ('Sports', 'Sports')], default='Classes', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DSchool',
            fields=[
                ('DSchoolID', models.AutoField(primary_key=True, serialize=False)),
                ('DSchoolName', models.CharField(max_length=100, unique=True)),
                ('Ward', models.CharField(max_length=100, unique=True)),
                ('Street', models.CharField(max_length=100, unique=True)),
                ('DistrictName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.district', to_field='DistrictName')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=50)),
                ('image', models.ImageField(default='avatar.jpg', upload_to='profile_images')),
                ('staff', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RoleName', models.CharField(max_length=100, unique=True)),
                ('DistrictName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.district', to_field='DistrictName')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SchoolAdminID', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('AdminMname', models.CharField(blank=True, max_length=50, null=True)),
                ('AdminPhoneNumber', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Content', models.TextField()),
                ('Picture', models.ImageField(blank=True, null=True, upload_to='announcement_pictures')),
                ('SchoolAdminID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.schooladmin')),
            ],
        ),
    ]
