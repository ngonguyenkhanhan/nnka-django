# Generated by Django 3.2.5 on 2021-08-04 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_lv5', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='portfolio',
            new_name='portfolio_site',
        ),
    ]