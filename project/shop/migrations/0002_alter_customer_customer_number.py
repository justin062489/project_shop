# Generated by Django 4.1.5 on 2023-01-29 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_number',
            field=models.IntegerField(editable=False, max_length=50, primary_key=True, serialize=False),
        ),
    ]