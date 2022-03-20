"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

import os
from app import app, db
from flask import flash, render_template, request, redirect, send_from_directory, url_for, session
from werkzeug.utils import secure_filename

from app.forms import NewProperty
from app.models import Property


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
    return render_template('about.html', name="Mary Jane")

@app.route('/properties/create', methods = ['GET', 'POST'])
def new_properties():
    """Render website's new properties page."""
    formobj = NewProperty()
    if request.method == 'GET':
        render_template('new_properties.html', form1 = formobj)
        
    if request.method == 'POST':
        if formobj.validate_on_submit():
            phObj = request.files['photo']
            otherobj = secure_filename(phObj.filename)
            phObj.save(os.path.join(app.config['UPLOAD_FOLDER'], otherobj))
            if phObj and otherobj != "":
                propty = Property(request.form['property_title'],request.form['description'], request.form['no_of_rooms'], request.form['no_of_bthrooms'], request.form['price'], request.form['property_type'], otherobj, request.form['location'])
                db.session.add(propty)
                db.session.commit()
                flash('Your property was added successfully', 'success')
                return redirect(url_for('properties'))
    return render_template('new_properties.html', form1 = formobj)


@app.route('/properties')
def properties():
    """Render website's properties page."""
    if request.method == 'GET':
        propInfo = Property.query.all() 
        return render_template('properties.html', propDetails = propInfo)


@app.route('/properties/<propertyid>')
def property_id(propertyid):
    """Render website's properties page."""
    prop_id = db.session.query(Property).filter(Property.id==propertyid).first()
    return render_template ('onepropview.html', property=prop_id)

@app.route('/uploads/<filename>')
def image(filename):
    return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), filename)



###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
