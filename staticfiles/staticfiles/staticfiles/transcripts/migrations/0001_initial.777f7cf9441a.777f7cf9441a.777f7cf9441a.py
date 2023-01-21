# Generated by Django 4.1.5 on 2023-01-17 15:41

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_from', models.DateField(blank=True, null=True)),
                ('year_to', models.DateField(blank=True, null=True)),
                ('institution_name', models.CharField(blank=True, max_length=100, null=True)),
                ('award', models.CharField(blank=True, max_length=100, null=True)),
                ('copy_of_document', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Hobbies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobby_name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Hobbie',
            },
        ),
        migrations.CreateModel(
            name='LanguagesSpoken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_name', models.CharField(max_length=50)),
                ('level_of_proficiency', models.CharField(choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Fairly Good', 'Fairly Good'), ('Poor', 'Poor')], max_length=250)),
            ],
            options={
                'verbose_name': 'Language',
            },
        ),
        migrations.CreateModel(
            name='LeadershipSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_from', models.DateField(blank=True, null=True)),
                ('year_to', models.DateField(blank=True, null=True)),
                ('institution_name', models.CharField(blank=True, max_length=100, null=True)),
                ('post', models.CharField(blank=True, max_length=100, null=True)),
                ('certificate', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Objective',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objective_statement', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Objective',
            },
        ),
        migrations.CreateModel(
            name='OtherDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_name', models.CharField(blank=True, max_length=100, null=True)),
                ('issued_by', models.CharField(blank=True, max_length=100, null=True)),
                ('copy_of_document', models.FileField(blank=True, null=True, upload_to='')),
                ('NIN_or_Identifier_Number', models.CharField(blank=True, max_length=150)),
                ('expires_on', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Other Doc',
            },
        ),
        migrations.CreateModel(
            name='References',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_refere', models.CharField(max_length=50)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(max_length=254)),
                ('institution_name', models.CharField(max_length=50)),
                ('working_as', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Reference',
            },
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills_name', models.CharField(max_length=150)),
                ('level_of_proficiency', models.CharField(choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Fairly Good', 'Fairly Good'), ('Poor', 'Poor')], max_length=250)),
            ],
            options={
                'verbose_name': 'Skill',
            },
        ),
        migrations.CreateModel(
            name='WorkingExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_from', models.DateField(blank=True, null=True)),
                ('year_to', models.DateField(blank=True, null=True)),
                ('institution_name', models.CharField(blank=True, max_length=100, null=True)),
                ('post', models.CharField(blank=True, max_length=100, null=True)),
                ('certificate', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
