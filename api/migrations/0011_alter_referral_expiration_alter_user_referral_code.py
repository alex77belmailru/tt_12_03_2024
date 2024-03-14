# Generated by Django 4.2.2 on 2024-03-13 23:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_referral_options_alter_referral_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referral',
            name='expiration',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 13, 23, 26, 41), verbose_name='Срок годности до'),
        ),
        migrations.AlterField(
            model_name='user',
            name='referral_code',
            field=models.CharField(blank=True, default=None, max_length=5, null=True, verbose_name='Реферальный код'),
        ),
    ]