from flask import Blueprint, Flask, render_template, request, redirect
from models.gym import Gym
from models.customer import Customer
from models.activities import Activity
import repositories.customer_repository as customer_repository
import repositories.gym_repository as gym_repository
import repositories.activity_repository as activity_repository
import pdb

activity_blueprint = Blueprint("activities", __name__)


@activity_blueprint.route("/create", methods=['POST'])
def create_activity():
    gym_id = request.form['gym']
    activity_type = request.form['activity_type']
    duration = request.form['duration']
    difficulty = request.form['difficulty']
    gym = gym_repository.select(gym_id)
    activity = Activity(gym, activity_type, duration, difficulty)
    activity_repository.save(activity)
    return redirect("/all-activities")


@activity_blueprint.route("/activities/new")
def new():
    all_gyms = gym_repository.select_all()
    return render_template("/activities/new.html", all_gyms=all_gyms)


@activity_blueprint.route("/all-activities")
def show_activities():
    activities = activity_repository.select_all()
    return render_template("activities/index.html", activities=activities)


@activity_blueprint.route("/activities/<id>/edit")
def edit_activity(id):
    activity = activity_repository.select(id)
    all_gyms = gym_repository.select_all()
    return render_template("activities/edit.html", activity=activity, all_gyms=all_gyms)


@activity_blueprint.route('/activities/<id>/delete', methods=['POST'])
def delete_activity(id):
    activity_repository.delete(id)
    return redirect("/all-activities")


@activity_blueprint.route("/activities/<id>", methods=['POST'])
def update_activity(id):
    activity_type = request.form['activity_type']
    duration = request.form['duration']
    difficulty = request.form['difficulty']
    gym_id = request.form['gym']
    gym = gym_repository.select(gym_id)
    activity = Activity(gym, activity_type, duration, difficulty, id)
    activity_repository.update(activity)
    return redirect("/all-activities")