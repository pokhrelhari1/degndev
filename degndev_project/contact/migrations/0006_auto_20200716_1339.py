# Generated by Django 2.2.13 on 2020-07-16 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_auto_20200716_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='package',
            field=models.CharField(choices=[('website', 'Website'), ('app', 'App Development'), ('graphic', 'Graphics Design')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='plan',
            field=models.CharField(choices=[('gold', 'Gold'), ('diamond', 'Diamond'), ('platinum', 'Platinum')], max_length=20, null=True),
        ),
    ]