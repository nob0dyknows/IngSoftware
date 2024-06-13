# Generated by Django 5.0.6 on 2024-06-03 21:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categoria', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ubishop_categoria',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.IntegerField()),
            ],
            options={
                'db_table': 'ubishop_producto',
            },
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'ubishop_reserva',
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_rol', models.CharField(max_length=50)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ubishop_rol',
            },
        ),
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ubishop_tienda',
            },
        ),
        migrations.CreateModel(
            name='DetalleReserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ubishop.producto')),
                ('reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ubishop.reserva')),
            ],
            options={
                'db_table': 'ubishop_detalle_reserva',
            },
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('tienda', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Ubishop.tienda')),
                ('latitud', models.DecimalField(decimal_places=8, max_digits=10)),
                ('longitud', models.DecimalField(decimal_places=8, max_digits=11)),
                ('direccion', models.TextField()),
            ],
            options={
                'db_table': 'ubishop_ubicacion',
            },
        ),
        migrations.AddField(
            model_name='producto',
            name='tienda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ubishop.tienda'),
        ),
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('descuento', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ubishop.producto')),
                ('tienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ubishop.tienda')),
            ],
            options={
                'db_table': 'ubishop_oferta',
            },
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ubishop.producto')),
                ('tienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ubishop.tienda')),
            ],
            options={
                'db_table': 'ubishop_inventario',
            },
        ),
        migrations.CreateModel(
            name='Convenio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_convenio_inicio', models.DateField()),
                ('fecha_convenio_fin', models.DateField()),
                ('tienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ubishop.tienda')),
            ],
            options={
                'db_table': 'ubishop_convenio',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=50)),
                ('clave', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=100)),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ubishop.rol')),
            ],
            options={
                'db_table': 'ubishop_usuario',
            },
        ),
        migrations.AddField(
            model_name='tienda',
            name='propietario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ubishop.usuario'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ubishop.usuario'),
        ),
        migrations.CreateModel(
            name='Resena',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calificacion', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('comentario', models.TextField()),
                ('fecha_opinion', models.DateField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ubishop.usuario')),
            ],
            options={
                'db_table': 'ubishop_resena',
            },
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=50)),
                ('apellido_usuario', models.CharField(max_length=50)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('ciudad', models.CharField(blank=True, max_length=50, null=True)),
                ('direccion', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ubishop.usuario')),
            ],
            options={
                'db_table': 'ubishop_perfil',
            },
        ),
        migrations.CreateModel(
            name='ProductoCategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ubishop.categoria')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ubishop.producto')),
            ],
            options={
                'db_table': 'ubishop_producto_categoria',
                'unique_together': {('producto', 'categoria')},
            },
        ),
    ]
