from flask import Blueprint, Flask, render_template, request, redirect
from models.gym import Gym
from models.customer import Customer
import repositories.gym_repository as gym_repository

gym_blueprint = Blueprint("gym", __name__)

# @gym_blueprint.route("/customers")
# def show_customers():
#     customers = gym_repository.select_all()
#     return render_template("customers/index.html", customers=customers)