# Generated by Django 3.0.2 on 2020-02-15 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Room', '0008_auto_20200215_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='discountcode',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Room.Discount'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='reserve',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Room.Reserve'),
        ),
        migrations.AlterField(
            model_name='reserve',
            name='room',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Room.Room'),
        ),
        migrations.AlterField(
            model_name='reserve',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Room.Users'),
        ),
    ]
