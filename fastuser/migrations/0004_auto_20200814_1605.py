# Generated by Django 2.1.11 on 2020-08-14 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fastuser', '0003_merge_20200813_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='creator',
            field=models.CharField(max_length=20, null=True, verbose_name='创建人'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='updater',
            field=models.CharField(max_length=20, null=True, verbose_name='更新人'),
        ),
        migrations.AddField(
            model_name='usertoken',
            name='creator',
            field=models.CharField(max_length=20, null=True, verbose_name='创建人'),
        ),
        migrations.AddField(
            model_name='usertoken',
            name='updater',
            field=models.CharField(max_length=20, null=True, verbose_name='更新人'),
        ),
    ]
