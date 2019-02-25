from app import app
from flask import render_template, request, redirect, url_for, flash 
from flask_wtf import FlaskForm 
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField 
from wtforms.validators import DataRequired  


class UploadForm(FlaskForm):
    pictures=FileField('pictures',validators=[FileRequired(),FileAllowed(['jpg', 'png', 'Images only!'])])