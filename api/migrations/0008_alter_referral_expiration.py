# Generated by Django 4.2.2 on 2024-03-12 22:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_referral_expiration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referral',
            name='expiration',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Срок годности'),
        ),
    ]