# Generated by Django 4.2.13 on 2024-06-28 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='/project_photos/default_project.png', null=True, upload_to='project_photos/')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_images', to='projects.project')),
            ],
        ),
    ]
