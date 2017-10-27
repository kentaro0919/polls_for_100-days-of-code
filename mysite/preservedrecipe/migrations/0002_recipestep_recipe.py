# Generated by Django 2.0b1 on 2017-10-27 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('preservedrecipe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipestep',
            name='recipe',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='preservedrecipe.Recipe'),
            preserve_default=False,
        ),
    ]
