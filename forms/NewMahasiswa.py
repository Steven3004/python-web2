from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired


class NewMahasiswa(FlaskForm):
    name = StringField("Nama", validators=[InputRequired()])
    npm = StringField("Npm", validators=[InputRequired()])
    profile_picture= FileField(
        "Profile Picture",
        validators=[
            FileRequired(),
            FileAllowed(["png","jpg"], "File Wajib jpg atau png"),
        ],
    )