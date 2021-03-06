# Generated by Django 2.2.6 on 2020-03-11 01:30

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=256)),
                ('username', models.CharField(max_length=256)),
                ('goal', models.IntegerField(default=20)),
                ('strike', models.IntegerField(default=0)),
                ('points', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': '"lml_player"',
            },
        ),
        migrations.CreateModel(
            name='Snapshot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player1', django.contrib.postgres.fields.jsonb.JSONField()),
                ('player2', django.contrib.postgres.fields.jsonb.JSONField()),
                ('game', django.contrib.postgres.fields.jsonb.JSONField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': '"lml_snapshot"',
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_hash', models.CharField(max_length=256)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('player1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='player1', to='learnmylanguage.Player')),
                ('player2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='player2', to='learnmylanguage.Player')),
            ],
            options={
                'db_table': '"lml_game"',
            },
        ),
    ]
