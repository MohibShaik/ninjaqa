# Generated by Django 2.2.2 on 2019-06-25 04:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('configuration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(max_length=256)),
                ('report_name', models.CharField(max_length=200)),
                ('report_file', models.CharField(max_length=200)),
                ('environment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuration.Environment')),
                ('run_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
