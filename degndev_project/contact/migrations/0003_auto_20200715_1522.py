# Generated by Django 2.2.13 on 2020-07-15 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20200715_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='package',
            field=models.CharField(choices=[('website', 'Website'), ('app', 'App Development'), ('graphic', 'Graphics Design')], default='PACKAGES', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='plan',
            field=models.CharField(choices=[('gold', 'Gold'), ('diamond', 'Diamond'), ('platinum', 'Platinum')], default='PLANS', max_length=20, null=True),
        ),
    ]