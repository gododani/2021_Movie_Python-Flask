from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from movies import app, db
from movies.forms import RegisterForm, LoginForm, UpdateAddGenreForm, UpdateAddPeopleForm, UpdateUserForm, UpdateAddMovieForm, UpdateAddActorForm
from movies.models import Movies, Users, Actors, MovieActors, Writers, Producers, Studios, Genres, MovieGenres
import os


# ----- HOME ----- #
@app.route('/')
@app.route('/home')
def home_page():
    return render_template("home.html")


# ----- MOVIES ----- #
@app.route('/movies')
@login_required
def movies_page():
    movies = Movies.query.all()
    return render_template("movies.html", movies=movies)


@app.route('/delete_movie/<int:id>')
@login_required
def delete_movie(id):
    movie_to_delete = Movies.query.get(id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    flash(f'Movie succesfully deleted!', category='success')
    return redirect('/movies')


@app.route('/update_movie/<int:id>&<string:name>', methods=['GET', 'POST'])
@login_required
def update_movie(id, name):
    form = UpdateAddMovieForm()
    movie_to_update = Movies.query.get(id)
    if request.method == "POST":
        movie_to_update.name = request.form['name']
        movie_to_update.length = request.form['length']
        movie_to_update.certificate = request.form['certificate']
        movie_to_update.release_date = request.form['release_date']
        movie_to_update.writer_id = request.form['writer_id']
        movie_to_update.producer_id = request.form['producer_id']
        movie_to_update.studio_id = request.form['studio_id']
        try:
            db.session.commit()
            flash(f'{name} successfully updated ', category='success')
            return redirect('/movies')
        except:
            db.session.rollback()
            flash(f'Error while updating { movie_to_update.name }!', category='danger')
            return render_template('/updates/movies_update.html', form=form, movie_to_update=movie_to_update, name=name)
    else:
        return render_template('/updates/movies_update.html', form=form, movie_to_update=movie_to_update, name=name)


@app.route('/add_movie', methods=['GET', 'POST'])
def add_movie():
    form = UpdateAddMovieForm()
    create_movie = Movies(name=form.name.data, length=form.length.data,
                          certificate=form.certificate.data, release_date=form.release_date.data,
                          writer_id=form.writer_id.data,
                          producer_id=form.producer_id.data, studio_id=form.studio_id.data)
    if form.validate_on_submit():
        try:
            img = request.files['logo']
            img.save(os.path.join(app.config['UPLOAD_FOLDER'], img.filename))
            print(111111111)
            create_movie.logo = "../static/images/" + img.filename
            print(222222222)
            db.session.add(create_movie)
            print(333333333)
            db.session.commit()
            print("GYŐZELEM")
            flash(f'{create_movie.name} succesfully created!', category='success')
            return redirect(url_for('movies_page'))
        except:
            db.session.rollback()
            flash(f'Error while adding {create_movie.name}!', category='danger')
            return render_template('/adds/movies_add.html', form=form, create_movie=create_movie)
    else:
        return render_template('/adds/movies_add.html', form=form, create_movie=create_movie)


# ----- USERS ----- #
@app.route('/users')
@login_required
def users_page():
    users = Users.query.all()
    return render_template("users.html", users=users)


@app.route('/delete_user/<int:id>')
@login_required
def delete_user(id):
    user_to_delete = Users.query.get(id)
    db.session.delete(user_to_delete)
    db.session.commit()
    flash(f'User succesfully deleted!', category='success')
    return redirect('/users')


@app.route('/update_user/<int:id>&<string:username>&<string:email>', methods=['GET', 'POST'])
@login_required
def update_user(id, username, email):
    form = UpdateUserForm()
    user_to_update = Users.query.get(id)
    if request.method == "POST":
        if request.form['password1'] == request.form['password2']:
            try:
                user_to_update.username = request.form['username']
                user_to_update.email = request.form['email']
                user_to_update.password = request.form['password1']
                db.session.commit()
                flash(f'{username} successfully updated to { user_to_update.username }', category='success')
                flash(f'{email} successfully updated to { user_to_update.email }', category='success')
                flash(f'Password successfully changed', category='success')
                return redirect('/users')
            except:
                db.session.rollback()
                flash(f'Error while updating { user_to_update.username } and password!', category='danger')
                return render_template('/updates/users_update.html', form=form, user_to_update=user_to_update, username=username, email=email)
        else:
            flash(f'Passwords are not matching!', category='danger')
            return render_template('/updates/users_update.html', form=form, user_to_update=user_to_update, username=username, email=email)
    else:
        return render_template('/updates/users_update.html', form=form, user_to_update=user_to_update, username=username, email=email)


# ----- ACTORS ----- #
@app.route('/actors')
@login_required
def actors_page():
    actors = Actors.query.all()
    return render_template("actors.html", actors=actors)


@app.route('/delete_actor/<int:id>')
@login_required
def delete_actor(id):
    actor_to_delete = Actors.query.get(id)
    db.session.delete(actor_to_delete)
    db.session.commit()
    flash(f'Actor succesfully deleted!', category='success')
    return redirect('/actors')


@app.route('/update_actor/<int:id>&<string:name>&<string:origin>&<string:birth_date>', methods=['GET', 'POST'])
@login_required
def update_actor(id, name, origin, birth_date):
    form = UpdateAddActorForm()
    actor_to_update = Actors.query.get(id)
    if request.method == "POST":
        actor_to_update.name = request.form['name']
        actor_to_update.origin = request.form['origin']
        actor_to_update.birth_date = request.form['birth_date']
        try:
            db.session.commit()
            flash(f'Successfully updated {name} to { actor_to_update.name }', category='success')
            flash(f'Successfully updated {origin} to { actor_to_update.origin }', category='success')
            flash(f'Successfully updated {birth_date} to { actor_to_update.birth_date }', category='success')
            return redirect('/actors')
        except:
            db.session.rollback()
            flash(f'Error while updating { actor_to_update.name }, { actor_to_update.origin } and { actor_to_update.birth_date }!', category='danger')
            return render_template('/updates/actors_update.html', form=form, actor_to_update=actor_to_update, name=name, origin=origin, birth_date=birth_date)
    else:
        return render_template('/updates/actors_update.html', form=form, actor_to_update=actor_to_update, name=name, origin=origin, birth_date=birth_date)


@app.route('/add_actor', methods=['GET', 'POST'])
def add_actor():
    form = UpdateAddActorForm()
    create_actor = Actors(name=form.name.data, origin=form.origin.data, birth_date=form.birth_date.data)
    if form.validate_on_submit():
        try:
            db.session.add(create_actor)
            db.session.commit()
            flash(f'{create_actor.name} succesfully created!', category='success')
            return redirect(url_for('actors_page'))
        except:
            db.session.rollback()
            flash(f'Error while adding {create_actor.name}!', category='danger')
            return render_template('/adds/actors_add.html', form=form, create_actor=create_actor)
    else:
        return render_template('/adds/actors_add.html', form=form, create_actor=create_actor)


# ----- MOVIE - ACTOR ----- #
@app.route('/movie_actors')
@login_required
def movie_actors_page():
    movie_actors = MovieActors.query.all()
    return render_template("movie_actors.html", movie_actors=movie_actors)


# ----- WRITERS ----- #
@app.route('/writers')
@login_required
def writers_page():
    writers = Writers.query.all()
    return render_template("writers.html", writers=writers)


@app.route('/delete_writer/<int:id>')
@login_required
def delete_writer(id):
    writer_to_delete = Writers.query.get(id)
    db.session.delete(writer_to_delete)
    db.session.commit()
    flash(f'Writer succesfully deleted!', category='success')
    return redirect('/writers')


@app.route('/update_writer/<int:id>&<string:name>&<string:origin>', methods=['GET', 'POST'])
@login_required
def update_writer(id, name, origin):
    form = UpdateAddPeopleForm()
    writer_to_update = Writers.query.get(id)
    if request.method == "POST":
        writer_to_update.name = request.form['name']
        writer_to_update.origin = request.form['origin']
        try:
            db.session.commit()
            flash(f'{name} successfully updated to { writer_to_update.name }', category='success')
            flash(f'{origin} successfully updated to { writer_to_update.origin }', category='success')
            return redirect('/writers')
        except:
            db.session.rollback()
            flash(f'Error while updating { writer_to_update.name } and { writer_to_update.origin }!', category='danger')
            return render_template('/updates/writers_update.html', form=form, writer_to_update=writer_to_update, name=name, origin=origin)
    else:
        return render_template('/updates/writers_update.html', form=form, writer_to_update=writer_to_update, name=name, origin=origin)


@app.route('/add_writer', methods=['GET', 'POST'])
def add_writer():
    form = UpdateAddPeopleForm()
    create_writer = Writers(name=form.name.data, origin=form.origin.data)
    if form.validate_on_submit():
        try:
            db.session.add(create_writer)
            db.session.commit()
            flash(f'{create_writer.name} succesfully created!', category='success')
            return redirect(url_for('writers_page'))
        except:
            db.session.rollback()
            flash(f'Error while adding {create_writer.name}!', category='danger')
            return render_template('/adds/writers_add.html', form=form, create_writer=create_writer)
    else:
        return render_template('/adds/writers_add.html', form=form, create_writer=create_writer)


# ----- PRODUCERS ----- #
@app.route('/producers')
@login_required
def producers_page():
    producers = Producers.query.all()
    return render_template("producers.html", producers=producers)


@app.route('/delete_producer/<int:id>')
@login_required
def delete_producer(id):
    producer_to_delete = Producers.query.get(id)
    db.session.delete(producer_to_delete)
    db.session.commit()
    flash(f'Producer succesfully deleted!', category='success')
    return redirect('/producers')


@app.route('/update_producer/<int:id>&<string:name>&<string:origin>', methods=['GET', 'POST'])
@login_required
def update_producer(id, name, origin):
    form = UpdateAddPeopleForm()
    producer_to_update = Producers.query.get(id)
    if request.method == "POST":
        producer_to_update.name = request.form['name']
        producer_to_update.origin = request.form['origin']
        try:
            db.session.commit()
            flash(f'Successfully updated {name} to { producer_to_update.name }', category='success')
            flash(f'Successfully updated {origin} to { producer_to_update.origin }', category='success')
            return redirect('/producers')
        except:
            db.session.rollback()
            flash(f'Error while updating { producer_to_update.name } and { producer_to_update.origin }!', category='danger')
            return render_template('/updates/producers_update.html', form=form, producer_to_update=producer_to_update, name=name, origin=origin)
    else:
        return render_template('/updates/producers_update.html', form=form, producer_to_update=producer_to_update, name=name, origin=origin)


@app.route('/add_producer', methods=['GET', 'POST'])
def add_producer():
    form = UpdateAddPeopleForm()
    create_producer = Producers(name=form.name.data, origin=form.origin.data)
    if form.validate_on_submit():
        try:
            db.session.add(create_producer)
            db.session.commit()
            flash(f'{create_producer.name} succesfully created!', category='success')
            return redirect(url_for('producers_page'))
        except:
            db.session.rollback()
            flash(f'Error while adding {create_producer.name}!', category='danger')
            return render_template('/adds/producers_add.html', form=form, create_producer=create_producer)
    else:
        return render_template('/adds/producers_add.html', form=form, create_producer=create_producer)


# ----- STUDIOS ----- #
@app.route('/studios')
@login_required
def studios_page():
    studios = Studios.query.all()
    return render_template("studios.html", studios=studios)


@app.route('/delete_studio/<int:id>')
@login_required
def delete_studio(id):
    studio_to_delete = Studios.query.get(id)
    db.session.delete(studio_to_delete)
    db.session.commit()
    flash(f'Studio succesfully deleted!', category='success')
    return redirect('/studios')


@app.route('/update_studio/<int:id>&<string:name>&<string:origin>', methods=['GET', 'POST'])
@login_required
def update_studio(id, name, origin):
    form = UpdateAddPeopleForm()
    studio_to_update = Studios.query.get(id)
    if request.method == "POST":
        studio_to_update.name = request.form['name']
        studio_to_update.origin = request.form['origin']
        try:
            db.session.commit()
            flash(f'Successfully updated {name} to { studio_to_update.name }', category='success')
            flash(f'Successfully updated {origin} to { studio_to_update.origin }', category='success')
            return redirect('/studios')
        except:
            db.session.rollback()
            flash(f'Error while updating { studio_to_update.name } and { studio_to_update.origin }', category='danger')
            return render_template('/updates/studios_update.html', form=form, studio_to_update=studio_to_update, name=name, origin=origin)
    else:
        return render_template('/updates/studios_update.html', form=form, studio_to_update=studio_to_update, name=name, origin=origin)


@app.route('/add_studio', methods=['GET', 'POST'])
def add_studio():
    form = UpdateAddPeopleForm()
    create_studio = Studios(name=form.name.data, origin=form.origin.data)
    if form.validate_on_submit():
        try:
            db.session.add(create_studio)
            db.session.commit()
            flash(f'{create_studio.name} succesfully created!', category='success')
            return redirect(url_for('studios_page'))
        except:
            db.session.rollback()
            flash(f'Error while adding {create_studio.name}!', category='danger')
            return render_template('/adds/studios_add.html', form=form, create_studio=create_studio)
    else:
        return render_template('/adds/studios_add.html', form=form, create_studio=create_studio)


# ----- GENRES ----- #
@app.route('/genres')
@login_required
def genres_page():
    genres = Genres.query.all()
    return render_template("genres.html", genres=genres)


@app.route('/delete_genre/<int:id>')
@login_required
def delete_genre(id):
    genre_to_delete = Genres.query.get(id)
    db.session.delete(genre_to_delete)
    db.session.commit()
    flash(f'Genre succesfully deleted!', category='success')
    return redirect('/genres')


@app.route('/update_genre/<int:id>/<string:name>', methods=['GET', 'POST'])
@login_required
def update_genre(id, name):
    form = UpdateAddGenreForm()
    genre_to_update = Genres.query.get(id)
    if request.method == "POST":
        genre_to_update.name = request.form['name']
        try:
            db.session.commit()
            flash(f'{name} successfully updated to { genre_to_update.name }!', category='success')
            return redirect('/genres')
        except:
            db.session.rollback()
            flash(f'Error while updating { genre_to_update.name }!', category='danger')
            return render_template('/updates/genres_update.html', form=form, genre_to_update=genre_to_update)
    else:
        return render_template('/updates/genres_update.html', form=form, genre_to_update=genre_to_update)


@app.route('/add_genre', methods=['GET', 'POST'])
def add_genre():
    form = UpdateAddGenreForm()
    create_genre = Genres(name=form.name.data)
    if form.validate_on_submit():
        try:
            db.session.add(create_genre)
            db.session.commit()
            flash(f'{create_genre.name} succesfully created!', category='success')
            return redirect(url_for('genres_page'))
        except:
            db.session.rollback()
            flash(f'Error while adding {create_genre.name}!', category='danger')
            return render_template('/adds/genres_add.html', form=form, create_genre=create_genre)
    else:
        return render_template('/adds/genres_add.html', form=form, create_genre=create_genre)


# ----- MOVIE - GENRE ----- #
@app.route('/movie_genres')
@login_required
def movie_genres_page():
    movie_genres = MovieGenres.query.all()
    return render_template("movie_genres.html", movie_genres=movie_genres)


# ----- REGISTER ----- #
@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        create_user = Users(username=form.username.data, email=form.email.data, password=form.password1.data)
        db.session.add(create_user)
        db.session.commit()
        login_user(create_user)
        flash(f'Account created succesfully! You have been logged in as { create_user.username }!', category='success')
        return redirect(url_for('movies_page'))
    # Ha van error a validáció után, akkor belefut az if-be
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error with creating your account: {err_msg}', category='danger')
    return render_template('register.html', form=form)


# ----- LOGIN ----- #
@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = Users.query.filter_by(username=form.username.data).first()
        if attempted_user:
            if attempted_user.check_password(attempted_password=form.password.data):
                login_user(attempted_user)
                flash(f'Login succesful! You are logged in as: {attempted_user.username}', category='success')
                return redirect(url_for('home_page'))
            else:
                flash(f'Username and password are not matching! Please try again!', category='danger')
                return redirect(url_for('login_page'))
        else:
            flash(f'Username does not exist!', category='danger')
            return redirect(url_for('login_page'))
    return render_template('login.html', form=form)


# ----- LOGOUT ----- #
@app.route('/logout')
def logout_page():
    logout_user()
    flash(f'You have been succesfully logged out!', category='info')
    return redirect(url_for('home_page'))