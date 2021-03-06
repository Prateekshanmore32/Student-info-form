# Generated by Django 4.0 on 2021-12-19 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='insti',
            field=models.CharField(default='nil', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='percentage',
            field=models.CharField(default='nil', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='qualification',
            field=models.CharField(default='nil', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='university',
            field=models.CharField(default='nil', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='yop',
            field=models.CharField(default='nil', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='mobileNo',
            field=models.IntegerField(),
        ),
    ]
