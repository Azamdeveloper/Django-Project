# Generated by Django 4.1.4 on 2023-01-05 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_application'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='Course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='news.course'),
        ),
        migrations.AddField(
            model_name='application',
            name='client_last_name',
            field=models.CharField(max_length=255, null=True, verbose_name='Familiya'),
        ),
    ]
