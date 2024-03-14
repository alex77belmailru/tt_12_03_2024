# Generated by Django 4.2.2 on 2024-03-12 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_referral_expiration_date_referral_expiration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referral',
            name='expiration',
            field=models.DateTimeField(auto_now=True, verbose_name='Срок годности'),
        ),
        migrations.AlterField(
            model_name='referral',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Активен'),
        ),
    ]
