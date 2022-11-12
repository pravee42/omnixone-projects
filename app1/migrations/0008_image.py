# Generated by Django 3.2.10 on 2022-07-14 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app1', '0007_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, null=True)),
                ('image', models.ImageField(null=True, upload_to='images')),
                ('description', models.TextField(null=True)),
            ],
        ),
    ]