# Generated by Django 3.0.3 on 2020-08-30 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('keshe', '0003_booktype'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='b_type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='keshe.BookType'),
        ),
    ]