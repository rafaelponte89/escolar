# Generated by Django 3.2.6 on 2021-11-07 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_trajeto', '0003_auto_20211107_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='tipo_transporte',
            field=models.ForeignKey(db_column='tipo_transporte_id', on_delete=django.db.models.deletion.CASCADE, to='app_trajeto.tipo_transporte'),
        ),
    ]
