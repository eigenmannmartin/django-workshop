# Generated by Django 3.2.5 on 2021-07-08 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='description',
        ),
        migrations.AddField(
            model_name='collection',
            name='name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]