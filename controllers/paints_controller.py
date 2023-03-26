from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.paint import Paint
import repositories.paint_repository as paint_repository

paints_blueprint = Blueprint("paints", __name__)

@paints_blueprint.route("/paints")
def users():
    paints = paint_repository.list_paints_limited() 
    return render_template("paints/index.html", paints = paints)

@paints_blueprint.route("/paints/<id>")
def show(id):
    paint = paint_repository.select(id)
    return render_template("paints/show.html", paint=paint)

@paints_blueprint.route("/paints/", methods=['POST'])
def new_paint():
    name = request.form['name']
    description = request.form['description']
    value = request.form['value']
    paint = Paint(name, description, value)
    paint_repository.save(paint)
    return redirect("/paints/")