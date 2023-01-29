# Generated by Django 4.1.5 on 2023-01-29 10:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(blank=True, max_length=200, null=True)),
                ('brand_code', models.CharField(blank=True, max_length=120, null=True)),
                ('logo', models.ImageField(blank=True, default='/placeholder.png', null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_number', models.CharField(editable=False, max_length=50, primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=150, null=True)),
                ('last_name', models.CharField(blank=True, max_length=150, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_terminated', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Terminated', 'Terminated')], max_length=20)),
                ('added_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Customer_added_by', to=settings.AUTH_USER_MODEL)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Customer_brand', to='shop.brand')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Customer_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
