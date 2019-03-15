"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from app.forms import ProfileForm
from app.models import UserProfile


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


@app.route("/profile", methods=["GET", "POST"])
def profile():
    form = ProfileForm()
    if request.method == "POST":
        if form.validate_on_submit() == True:
            
            #Gets the user input from the form
            fname = form.firstname.data
            lname = form.lastname.data
            gender = form.gender.data
            email = form.email.data
            location = form.location.data
            bio = form.bio.data
            filename = assignPath(form.photo.data)
            
            #create user object and add to database
            user = UserProfile(fname,lname,gender,email,location,bio, filename)
            db.session.add(user)
            db.session.commit()

            # remember to flash a message to the user
            flash('User information submitted successfully.', 'success')
        else:
            flash('User information not submitted', 'danger')
        return redirect(url_for("profiles"))  # they should be redirected to a secure-page route instead
    return render_template("profile.html", form=form)


#Save the uploaded photo to a folder
def assignPath(upload):
    filename = secure_filename(upload.filename)
    upload.save(os.path.join(
                app.config['UPLOAD_FOLDER'], filename
    ))
    return filename 


# def get_uploaded_image(upload):
#     photo = " "
#     # valid_images = [".jpg",".png",".jpeg"]
#     for subdir, dirs, files in os.walk(app.config['UPLOAD_FOLDER']):
#         files = [f for f in files if not f[0] == '.']
#         for file in files:
#             f = os.path.splitext(os.path.basename(subdir))[0]
#             if str(upload) in file:
#                 photo = os.path.join(f, file)
#                 print(photo)
#     return photo


@app.route("/profiles")
def profiles():
    user_profiles = db.session.query(UserProfile).all()
    return render_template("profiles.html", users=user_profiles)
    
# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session
# @login_manager.user_loader
# def load_user(id):
#     return UserProfile.query.get(int(id))

###
# The functions below should be applicable to all Flask apps.
###


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
