# Generated by Django 3.1.5 on 2021-03-16 13:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payment', '0002_auto_20210215_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='stripepayment',
            name='edit_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stripepayment',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_payment', to=settings.AUTH_USER_MODEL),
        ),
    ]
