# Generated by Django 3.2.4 on 2021-06-29 01:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customer_e_mail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='age',
        ),
    ]
