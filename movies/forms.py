from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, PasswordField, SubmitField, FileField
from wtforms.validators import Length, Email, EqualTo, DataRequired, ValidationError
from movies.models import Users

# ----- REGISTER ----- #
class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = Users.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Try a different username')

    def validate_email(self, email_to_check):
        email = Users.query.filter_by(email=email_to_check.data).first()
        if email:
            raise ValidationError('This email already exists! Try a different email address')

    username = StringField(label='Username:', validators=[Length(min=4, max=20), DataRequired()])
    email = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')


# ----- LOGIN ----- #
class LoginForm(FlaskForm):
    username = StringField(label='Username:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')


# ----- GENRE UPDATE & ADD ----- #
class UpdateAddGenreForm(FlaskForm):
    name = StringField(label='Name:', validators=[Length(min=4, max=20), DataRequired()])
    submit = SubmitField(label='Save')


# ----- STUDIO, WRITER, Producer, Studio UPDATE & ADD ----- #
class UpdateAddPeopleForm(FlaskForm):
    name = StringField(label='Name:', validators=[Length(min=4, max=40), DataRequired()])
    origin = StringField(label='Origin:', validators=[Length(min=4, max=20), DataRequired()])
    submit = SubmitField(label='Save')


# ----- USER UPDATE ----- #
class UpdateUserForm(FlaskForm):
    username = StringField(label='Username:', validators=[Length(min=4, max=20), DataRequired()])
    email = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Save')


# ----- MOVIE UPDATE & ADD ----- #
class UpdateAddMovieForm(FlaskForm):
    name = StringField(label='Name:', validators=[Length(min=4, max=40), DataRequired()])
    logo = FileField(label='Logo:', name='logo', validators=[DataRequired()])
    length = IntegerField(label='Length:', validators=[DataRequired()])
    certificate = IntegerField(label='Certificate:', validators=[DataRequired()])
    release_date = DateField(label='Release Date', validators=[DataRequired()])
    writer_id = IntegerField(label='Writer:', validators=[DataRequired()])
    producer_id = IntegerField(label='Producer:', validators=[DataRequired()])
    studio_id = IntegerField(label='Studio:', validators=[DataRequired()])
    submit = SubmitField(label='Save')


# ----- ACTOR UPDATE & ADD ----- #
class UpdateAddActorForm(FlaskForm):
    name = StringField(label='Name:', validators=[Length(min=4, max=40), DataRequired()])
    origin = StringField(label='Origin:', validators=[Length(min=4, max=20), DataRequired()])
    birth_date = DateField(label='Birth Date:', validators=[DataRequired()])
    submit = SubmitField(label='Save')
