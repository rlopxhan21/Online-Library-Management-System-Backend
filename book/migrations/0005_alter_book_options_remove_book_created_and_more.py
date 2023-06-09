# Generated by Django 4.1.7 on 2023-04-01 10:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0004_book_patrons'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={},
        ),
        migrations.RemoveField(
            model_name='book',
            name='created',
        ),
        migrations.AddField(
            model_name='book',
            name='booked_till',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('A', 'AVAILABLE'), ('B', 'BORROWED'), ('R', 'RESERVED')], default='A', max_length=2),
        ),
        migrations.AddField(
            model_name='book',
            name='updated',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='patrons',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='borrowed_collection', to=settings.AUTH_USER_MODEL),
        ),
    ]
