# Generated by Django 4.0 on 2021-12-18 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('mobileNo', models.IntegerField(verbose_name=10)),
                ('email', models.CharField(max_length=30)),
                ('age', models.IntegerField(verbose_name=2)),
                ('education', models.CharField(max_length=30)),
            ],
        ),
    ]
