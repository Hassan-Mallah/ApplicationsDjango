# Generated by Django 3.0.4 on 2020-03-27 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_auto_20200327_1205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='alias',
            new_name='application_name',
        ),
        migrations.RemoveField(
            model_name='application',
            name='name',
        ),
        migrations.AddField(
            model_name='application',
            name='key',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
