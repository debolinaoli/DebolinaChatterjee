# Generated by Django 4.2.7 on 2024-01-29 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField(max_length=10)),
                ('company_organization', models.CharField(max_length=50)),
                ('venue_requested', models.CharField(max_length=255)),
                ('type_event', models.CharField(max_length=255)),
                ('date_requested_first', models.DateField()),
                ('date_requested_second', models.DateField()),
                ('about_event_hosting', models.TextField()),
            ],
        ),
    ]
