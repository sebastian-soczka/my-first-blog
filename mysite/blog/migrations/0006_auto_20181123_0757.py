# Generated by Django 2.1.3 on 2018-11-23 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_chapter_nr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='volume_nr',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]