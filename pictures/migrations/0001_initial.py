# Generated by Django 3.2 on 2021-04-11 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FilePathField(path='/img')),
                ('image_desc', models.CharField(max_length=100)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('contributor', models.CharField(max_length=50)),
            ],
        ),
    ]
