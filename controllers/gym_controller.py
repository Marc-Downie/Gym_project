from flask import Blueprint, Flask, render_template, request, redirect
from models.gym import Gym
from models.customer import Customer
from models.activities import Activity
import repositories.gym_repository as gym_repository
import repositories.customer_repository as customer_repository

gym_blueprint = Blueprint("gym", __name__)


# @gym_blueprint.route("/all-activities")
# def show_activities():
    


# (self, gym, activity_type, duration, difficulty, id=None):
# @gym_blueprint.route("/create", methods=['POST'])
# def create_activity():
#     gym_id = request.form['gym']
#     activity_type = request.form['activity_type']
#     duration = request.form['duration']
#     difficulty = request.form['difficulty']
#     gym = gym_repository.select(gym_id)
#     activity = Activity(gym, activity_type, duration, difficulty)
#     gym_repository.save(activity)
#     return render_template("/activities")




# @gym_blueprint.route("/activities/new")
# def new():
#     all_activities = gym_repository.select_all()
#     return render_template("/activities/new.html")
