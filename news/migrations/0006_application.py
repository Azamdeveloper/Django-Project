# Generated by Django 4.1.4 on 2022-12-27 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=200)),
                ('client_phone_number', models.CharField(max_length=50)),
            ],
        ),
    ]
