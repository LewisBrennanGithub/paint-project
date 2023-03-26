from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.paint import Paint
import repositories.paint_repository as paint_repository

paints_blueprint = Blueprint("paints", __name__)

@paints_blueprint.route("/paints")
def main():
    paints = paint_repository.list_paints_limited() 
    return render_template("paints/index.html", paints = paints)

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
    value = request.form['value']
    new_paint = Paint(name, description, value)
    paint_repository.save_new_paint(new_paint)
    return redirect('/paints')

@paints_blueprint.route("/paints/<id>/delete", methods=['POST'])
def delete_paint(id):
    paint_repository.delete(id)
    return redirect('/paints')

# EDIT
# GET '/books/<id>/edit'
@paints_blueprint.route("/paints/<id>/edit", methods=['GET'])
def edit_paint_page(id):
    paint = paint_repository.select(id)
    return render_template('paints/edit.html', paint=paint, id=id)

# UPDATE
# PUT '/books/<id>'
@paints_blueprint.route("/paints/<id>/edit", methods=['POST'])
def update_paint(id):
    name = request.form['name']
    description = request.form['description']
    value = request.form['value']
    offset_value = request.form['offset_value']
    paint = Paint(name, description, value, offset_value, id)
    paint_repository.update_existing_paint(paint)
    return redirect('/paints')
