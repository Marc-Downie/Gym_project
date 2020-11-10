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
    gym_id = request.form['gym']
    gym = gym_repository.select(gym_id)
    customer = Customer(name, membership, gym)
    customer_repository.save(customer)
    return redirect("/customers")

@customer_blueprint.route("/customers/new")
def new():
    all_gyms = gym_repository.select_all()
    return render_template("customers/new.html", all_gyms=all_gyms)


@customer_blueprint.route("/customers/<id>/edit")
def edit_customer(id):
    customer = customer_repository.select(id)
    all_gyms = gym_repository.select_all()
    return render_template("customers/edit.html", customer=customer, all_gyms=all_gyms)


@customer_blueprint.route("/customers/<id>", methods=['POST'])
def update_customer(id):
    name = request.form['name']
    membership = request.form['membership']
    gym_id = request.form['gym']
    gym = gym_repository.select(gym_id)
    customer = Customer(name, membership, gym, id)
    customer_repository.update(customer)
    return redirect("/customers")

@customer_blueprint.route("/customers/<id>/delete", methods=["POST"])
def delete_customer(id):
    customer_repository.delete(id)
    return redirect("/customers")