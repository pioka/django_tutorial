# Generated by Django 2.0.7 on 2018-07-21 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='puestion_text',
            new_name='question_text',
        ),
    ]
