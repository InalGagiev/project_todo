# Generated by Django 4.1.4 on 2023-03-23 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0002_todoitem_todo_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
