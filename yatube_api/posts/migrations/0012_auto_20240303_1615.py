# Generated by Django 3.2.16 on 2024-03-03 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_follow_posts_follow_prevent_self_follow'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_follower_followings',
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'following'), name='posts _ follow _unique_relationships'),
        ),
    ]