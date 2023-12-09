# Generated by Django 5.0 on 2023-12-09 11:23

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
            name='Designation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last Updated At')),
                ('title', models.CharField(max_length=127, verbose_name='Name')),
                ('description', models.CharField(max_length=255, verbose_name='Description')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last Updated At')),
                ('name', models.CharField(max_length=127, verbose_name='Name')),
                ('description', models.CharField(max_length=255, verbose_name='Description')),
                ('founder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Organizations', to=settings.AUTH_USER_MODEL, verbose_name='Founder')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MemberOrganization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last Updated At')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Is Admin?')),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='added_members', to=settings.AUTH_USER_MODEL, verbose_name='Added by')),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Members', to='organizations.designation', verbose_name='Designation')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='in_organizations', to=settings.AUTH_USER_MODEL, verbose_name='Member')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='organizations.organization', verbose_name='Organization')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='designation',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Designations', to='organizations.organization', verbose_name='Organization'),
        ),
    ]