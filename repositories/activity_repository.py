from db.run_sql import run_sql
from models.gym import Gym
from models.customer import Customer
from models.activities import Activity
from repositories import gym_repository



def save(activity):
    sql = "INSERT INTO activities (gym_id, activity, duration, difficulty) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [activity.gym.id, activity.activity_type, activity.duration, activity.difficulty]
    results = run_sql(sql, values)
    id = results[0]['id']
    activity.id = id
    return activity


def select_all():
    activities = []

    sql = "SELECT * FROM activities"
    results = run_sql(sql)

    for row in results:
        gym = gym_repository.select(row['gym_id'])
        activity = Activity(gym, row['activity'], row['duration'], row['difficulty'], row['id'])
        activities.append(activity)
    return activities


def delete(id):
    sql = "DELETE  FROM activities WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE  FROM activities"
    run_sql(sql)

def update(activity):
    sql = "UPDATE activities SET (gym_id, activity, duration, difficulty) = (%s, %s, %s, %s) WHERE id = %s"
    values = [activity.gym.id, activity.activity_type, activity.duration, activity.difficulty, activity.id]
    run_sql(sql, values)

def select(id):
    activity = None
    sql = "SELECT * FROM activities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    gym = gym_repository.select(result['gym_id'])
    activity = Activity(gym, result["activity"], result["duration"], result["difficulty"], result["id"])
    return activity
