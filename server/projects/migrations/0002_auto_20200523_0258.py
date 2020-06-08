# Generated by Django 3.0.6 on 2020-05-23 06:58

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='technologies',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Python', 'Python'), ('Django', 'Django'), ('React with hooks', 'React with hooks'), ('React with classes', 'React with classes'), ('React Router', 'React Router'), ('JavaScript', 'JavaScript'), ('Node', 'Node'), ('Express', 'Express'), ('MongoDB', 'MongoDB'), ('Mongoose', 'Mongoose'), ('Angular', 'Angular'), ('Postgres', 'Postgres'), ('Bootstrap', 'Bootstrap'), ('Heroku', 'Heroku'), ('Amazon Web Services', 'Amazon Web Services'), ('Digital Ocean', 'Digital Ocean'), ('Jinja', 'Jinja'), ('Styled Components', 'Styled Components'), ('CSS 3', 'CSS 3'), ('Material UI', 'Material UI'), ('Semantic UI', 'Semantic UI'), ('Materialize', 'Materialize'), ('Sass', 'Sass'), ('Less', 'Less'), ('HTML 5', 'HTML 5'), ('Axios', 'Axios'), ('None', 'None')], default='None', max_length=265),
        ),
    ]