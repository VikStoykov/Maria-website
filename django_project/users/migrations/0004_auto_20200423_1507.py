# Generated by Django 3.0.4 on 2020-04-23 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200423_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.TextField(default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='profile',
            name='facebook',
            field=models.URLField(default='#'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='instagram',
            field=models.URLField(default='#'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='twitter',
            field=models.URLField(default='#'),
        ),
    ]