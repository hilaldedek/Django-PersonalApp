# Generated by Django 4.2.1 on 2023-05-29 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personel', '0002_alter_personel_department_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personel',
            name='department_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='personel', to='personel.department'),
        ),
    ]
