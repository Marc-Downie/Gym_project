from db.run_sql import run_sql
from models.gym import Gym
from models.customer import Customer
from repositories import gym_repository



def save(customer):
    sql = "INSERT INTO customers (name, membership, gym_id) VALUES (%s, %s, %s) RETURNING *"
    values = [customer.name, customer.membership, customer.gym.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    customer.id = id
    return customer



def select_all():
    customers = []

    sql = "SELECT * FROM customers"
    results = run_sql(sql)

    for row in results:
        gym = gym_repository.select(row['gym_id'])
        customer = Customer(row['name'], row['membership'], gym, row['id'])
        customers.append(customer)
    return customers


def select(id):
    customer = None
    sql = "SELECT * FROM customers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    customer = Customer(result["name"], result["id"])
    return customer


def delete_all():
    sql = "DELETE  FROM customers"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM customers WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(customer):
    sql = "UPDATE customers SET (name, membership, gym_id) = (%s, %s, %s) WHERE id = %s"
    values = [customer.name, customer.membership, customer.id]
    run_sql(sql, values)