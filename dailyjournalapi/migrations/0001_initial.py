# Generated by Django 3.2.8 on 2021-10-07 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='JournalEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concept', models.CharField(max_length=100)),
                ('entry', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('mood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dailyjournalapi.mood')),
            ],
        ),
    ]
