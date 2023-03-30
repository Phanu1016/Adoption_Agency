from flask import Flask, flash, request, redirect, render_template, session
from models import connect_database, database, Pet
from forms import AddPetForm, EditPetForm

#  SET UP
app = Flask(__name__)

DATABASE_NAME = 'pets'

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql:///{DATABASE_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config["SECRET_KEY"] = "Phanu!"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

connect_database(app)


@app.route('/')
def index_page():
    """ Home page shows all the pets in adoption center """
    return render_template('index.html', pets=Pet.query.all())


@app.route('/add', methods=["GET", "POST"])
def add_pet_page():
    """ Add new pet page to adoption center, shows add pet form (handles both get and post)"""
    form = AddPetForm()
    if form.validate_on_submit():
        example_pet = Pet(name=form.name.data, species=form.species.data, photo_url=form.photo_url.data if form.photo_url.data != '' else "https://i.ibb.co/qRpVdbn/noimage.png", age=form.age.data if form.age.data != None else 0, notes=form.notes.data)
        database.session.add(example_pet)
        database.session.commit()
        return redirect('/')
    else:
        return render_template('add.html', form=form)

@app.route('/<int:pet_id>')
def view_pet_page(pet_id):
    """ Pet profile """
    return render_template('pet.html', pet=Pet.query.get_or_404(pet_id))

@app.route('/<int:pet_id>/edit', methods=["GET", "POST"])
def edit_pet_page(pet_id):
    """ Edit the specified id pet (handles both get and post) """
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        database.session.add(pet)
        database.session.commit()
        return redirect('/')
    else:
        return render_template('edit_pet.html', form=form, pet=pet)


