from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.paint import Paint
import repositories.paint_repository as paint_repository

paints_blueprint = Blueprint("paints", __name__)