# Generated by Django 4.2.2 on 2024-03-12 21:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_referral_expiration_alter_referral_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referral',
            name='expiration',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 12, 21, 58, 53), verbose_name='Срок годности'),
        ),
    ]