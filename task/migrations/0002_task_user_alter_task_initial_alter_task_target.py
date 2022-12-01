# Generated by Django 4.1.3 on 2022-12-01 14:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='initial',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='task',
            name='target',
            field=models.IntegerField(default=1),
        ),
    ]