# Generated by Django 3.2.8 on 2021-10-22 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_audit', '0002_auditlog_post_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='auditlog',
            name='host_name',
            field=models.CharField(
                default='', max_length=200, verbose_name='HostName'),
        ),
    ]