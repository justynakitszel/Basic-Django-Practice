# Generated by Django 3.0.3 on 2020-03-23 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='phone_number',
            field=models.IntegerField(default=9),
        ),
        migrations.AddField(
            model_name='snippet',
            name='surname',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
