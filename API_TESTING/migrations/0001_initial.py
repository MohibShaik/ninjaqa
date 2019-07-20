# Generated by Django 2.2.2 on 2019-07-19 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('environment', models.CharField(choices=[['local', 'Local'], ['dev', 'Development'], ['qa', 'QA'], ['stage', 'Staging'], ['prod', 'Production']], max_length=10)),
                ('base_url', models.URLField(max_length=256)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API_TESTING.Project')),
            ],
        ),
    ]
