# Generated by Django 4.2.2 on 2024-03-25 02:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_referral_expiration_alter_user_referral_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referral',
            name='expiration',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 25, 2, 15, 31), verbose_name='Срок годности до'),
        ),
    ]