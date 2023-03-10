# Generated by Django 4.1 on 2023-02-05 02:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.CharField(max_length=8)),
                ('name', models.CharField(max_length=50)),
                ('mail', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='date published')),
                ('document_p', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.person')),
            ],
        ),
    ]
