# Generated by Django 3.2.16 on 2024-03-01 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_follow_following'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='following',
            field=models.TextField(null=True),
        ),
    ]
