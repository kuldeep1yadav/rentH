# Generated by Django 3.2.25 on 2024-04-21 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='user',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_client',
            field=models.BooleanField(default=False, verbose_name='Is client'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_owner',
            field=models.BooleanField(default=False, verbose_name='Is owner'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='Owner',
        ),
    ]