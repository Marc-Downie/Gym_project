from flask import Blueprint, Flask, render_template, request, redirect
from models.gym import Gym
from models.customer import Customer
import repositories.customer_repository as customer_repository
import repositories.gym_repository as gym_repository



customer_blueprint = Blueprint("customers", __name__)

@customer_blueprint.route("/customers")
def show_customers():
    customers = customer_repository.select_all()
    return render_template("customers/index.html", customers=customers)


@customer_blueprint.route("/sign-up", methods=['POST'])
def create_customer():
    name = request.form['name']
    membership = request.form['membership']
    gym = request.form['gym']
    customer = Customer(name, membership, gym)
    customer_repository.save(customer)
    return redirect("/customers")

@customer_blueprint.route("/customers/new")
def new():
    return render_template("customers/new.html")