# Generated by Django 3.2.10 on 2022-08-20 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_auto_20220819_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controller',
            name='blurController',
            field=models.ImageField(default='blur-image.jpeg', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='embeddedlinux',
            name='blurEmbeddedLinux',
            field=models.ImageField(default='blur-image.jpeg', null=True, upload_to=''),
        ),
    ]