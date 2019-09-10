# Generated by Django 2.2.2 on 2019-08-20 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API_TESTING', '0011_auto_20190820_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='environment',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API_TESTING.project'),
        ),
        migrations.AlterField(
            model_name='query_params',
            name='environment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API_TESTING.environment'),
        ),
    ]
