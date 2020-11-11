from flask import Blueprint, Flask, render_template, request, redirect
from models.gym import Gym
from models.customer import Customer
from models.activities import Activity
import repositories.customer_repository as customer_repository
import repositories.gym_repository as gym_repository
import repositories.activity_repository as activity_repository


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
    return render_template("/activities")

@activity_blueprint.route("/activities/new")
def new():
    all_activities = activity_repository.select_all()
    return render_template("/activities/new.html")



@activity_blueprint.route("/all-activities")
def show_activities():
    activities = activity_repository.select_all()
    return render_template("activities/index.html", activities=activities)
