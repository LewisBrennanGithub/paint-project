from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.paint import Paint
import repositories.paint_repository as paint_repository

paints_blueprint = Blueprint("paints", __name__)

@paints_blueprint.route("/paints")
def top_paints():
    paints = paint_repository.list_paints_limited() 
    return render_template("paints/index.html", paints = paints)

@paints_blueprint.route("/paints")
def all_paints():
    paints = paint_repository.list_all_paints() 
    return render_template("paints/all.html", paints = paints)

@paints_blueprint.route("/paints/<id>")
def show(id):
    paint = paint_repository.select(id)
    return render_template("paints/show.html", paint=paint)

@paints_blueprint.route("/paints/new", methods=['GET'])
def new_paint():
    paint = paint_repository.select_all()
    return render_template("paints/new.html", paint = paint)

@paints_blueprint.route("/paints/new", methods=['POST'])
def create_paint():
    name = request.form['name']
    description = request.form['description']
    value = request.form['colour-picker']
    popularity = 0
    new_paint = Paint(name, description, value, popularity)
    paint_repository.save_new_paint(new_paint)
    return redirect('/paints')

@paints_blueprint.route("/paints/<id>/delete", methods=['POST'])
def delete_paint(id):
    paint_repository.delete(id)
    return redirect('/paints')

@paints_blueprint.route("/paints/<id>/edit", methods=['GET'])
def edit_paint_page(id):
    paint = paint_repository.select(id)
    return render_template('paints/edit.html', paint=paint, id=id)

@paints_blueprint.route("/paints/<int:id>/edit", methods=['POST'])
def update_paint(id):
    name = request.form['name']
    description = request.form['description']
    value = request.form['value-colour-picker']
    offset_value = request.form['offset-value-colour-picker']
    paint = paint_repository.select(id)
    paint.name = name
    paint.description = description
    paint.value = value
    paint.offset_value = offset_value
    paint_repository.update_existing_paint(paint)
    return redirect('/paints')

@paints_blueprint.route("/paints/<id>/decrement", methods=['POST'])
def decrement_paint(id):
    paint_repository.decrement_paint_popularity(id)
    return redirect('/paints')

@paints_blueprint.route("/paints/<id>/increment", methods=['POST'])
def increment_paint(id):
    paint_repository.increment_paint_popularity(id)
    return redirect('/paints')

# def paint_pop_decrement(id):
#     paint_repository.decrement_paint_popularity(id)
#     return redirect('/paints')

# @paints_blueprint.route("/paints/<id>/increment", methods=['POST'])
# def paint_pop_increment(id):
#     paint_repository.increment_paint_popularity(id)
#     return redirect('/paints')

# @paints_blueprint.route("/paints/<id>/decrement", methods=['POST'])
# def paint_pop_decrement(id):
#     paint_repository.decrement_paint_popularity(id)
#     return redirect('/paints')

# @paints_blueprint.route("/paints/<id>/increment", methods=['POST'])
# def paint_pop_increment(id):
#     paint_repository.increment_paint_popularity(id)
#     return redirect('/paints')