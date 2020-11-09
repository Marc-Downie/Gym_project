from flask import Blueprint, Flask, render_template, request, redirect
from models.customer import Customer
import repositories.customer_repository as customer_repository

gym_blueprint = Blueprint("gym", __name__)

@gym_blueprint.route("/customers")
def show_customers():
    customers = customer_repository.select_all()
    return render_template("customers/index.html", customers=customers)