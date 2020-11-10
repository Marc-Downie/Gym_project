from db.run_sql import run_sql
from models.gym import Gym
from models.customer import Customer
import repositories.customer_repository as customer_repository

def save(customer):
    sql = "INSERT INTO gyms (name) VALUES (%s) RETURNING *"
    values = [customer.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    customer.id = id
    return customer


def select_all():
    gyms = []

    sql = "SELECT * FROM gyms"
    results = run_sql(sql)

    for row in results:
        gym = Gym(row["name"], row["id"])
        gyms.append(gym)
    return gyms


def select(id):
    sql = "SELECT * FROM gyms WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    gym = Gym(result["name"], result["id"])
    return gym


def delete_all():
    sql = "DELETE  FROM gyms"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM gyms WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(customer):
    sql = "UPDATE gyms SET (name) = (%s) WHERE id = %s"
    values = [customer.name, customer.id]
    run_sql(sql, values)