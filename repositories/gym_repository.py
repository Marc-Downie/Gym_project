from db.run_sql import run_sql
from models.gym import Gym
from models.customer import Customer
# import repositories.customer_repository as customer_repository

def save(customer):
    sql = "INSERT INTO gyms (name) VALUES (%s) RETURNING *"
    values = [customer.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    task.id = id
    return customer


def select_all():
    customers = []

    sql = "SELECT * FROM gym"
    results = run_sql(sql)

    for row in results:
        customer = Customer(row['name'], row['membership'], row['id'])
        # gym = Gym(row['name'], customers)
        customers.append(customer)
    return customer


def select(id):
    customer = None
    sql = "SELECT * FROM gym WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    customer = Customer(result["name"], result["id"])
    return customer


def delete_all():
    sql = "DELETE  FROM gym"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM gym WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(customer):
    sql = "UPDATE gym SET (name) = (%s) WHERE id = %s"
    values = [customer.name, customer.id]
    run_sql(sql, values)