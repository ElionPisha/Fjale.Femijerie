# Generated by Django 3.0.6 on 2020-05-20 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FjaleVideo', '0008_dramatizimedrama'),
    ]

    operations = [
        migrations.CreateModel(
            name='Krijimeabetare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.TextField(max_length=200)),
                ('lecture_name', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100)),
                ('names', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=300)),
            ],
        ),
    ]