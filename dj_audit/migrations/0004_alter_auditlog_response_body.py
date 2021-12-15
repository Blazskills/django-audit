# Generated by Django 3.2.8 on 2021-12-13 11:14

from django import __version__
from django.db import migrations, models

if __version__ > '2.2':
    from django.db.models import JSONField
else:
    from django.contrib.postgres.fields import JSONField


class Migration(migrations.Migration):

    dependencies = [
        ('dj_audit', '0003_alter_auditlog_http_referer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditlog',
            name='response_body',
            field=JSONField(default=dict),
        ),
    ]
