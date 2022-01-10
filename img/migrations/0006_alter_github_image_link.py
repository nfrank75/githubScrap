# Generated by Django 3.2.5 on 2022-01-05 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('img', '0005_alter_github_image_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='github',
            name='image_link',
            field=models.CharField(blank=True, db_index=True, max_length=150, unique=True, verbose_name='Image Link'),
        ),
    ]
