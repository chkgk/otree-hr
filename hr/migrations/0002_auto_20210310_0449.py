# Generated by Django 3.1.7 on 2021-03-09 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='aws_access_key_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='aws_secret_access_key',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='rest_key',
            field=models.CharField(max_length=255, verbose_name='OTREE_REST_KEY'),
        ),
        migrations.AlterField(
            model_name='site',
            name='url',
            field=models.CharField(help_text='For example, http://localhost:8000 or https://myapp.herokuapp.com', max_length=255, verbose_name='URL'),
        ),
    ]
