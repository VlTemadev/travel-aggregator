# Generated by Django 3.1 on 2022-10-29 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Описание')),
            ],
        ),
    ]