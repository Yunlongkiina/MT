# Generated by Django 2.0.6 on 2018-06-20 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ws', '0002_auto_20180620_1256'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('content', models.TextField()),
            ],
        ),
    ]
