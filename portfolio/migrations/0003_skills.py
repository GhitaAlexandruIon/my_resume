# Generated by Django 3.0.3 on 2020-06-23 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_technology_facts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('percent', models.CharField(max_length=3)),
                ('text', models.TextField(max_length=50)),
            ],
        ),
    ]
