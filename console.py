import pdb
from models.gym import Gym
from models.customer import Customer
from models.activities import Activity

import repositories.gym_repository as gym_repository
import repositories.customer_repository as customer_repository
import repositories.activity_repository as activity_repository

activity_repository.delete_all()
customer_repository.delete_all()
gym_repository.delete_all()


gym_1 = Gym('Chromerias Gym')
gym_repository.save(gym_1)

gym_2 = Gym('MAXIMUM Gym')
gym_repository.save(gym_2)

activity_1 = Activity(gym_1, 'Running', 60, 'INTENSE')
activity_repository.save(activity_1)

customer_1 = Customer('Kip Gyle', 'Premium', gym_1)
customer_repository.save(customer_1)

customer_2 = Customer('Gavin Gyle', 'Standard', gym_1)
customer_repository.save(customer_2)

customer_3 = Customer('Karris White', 'Standard', gym_2)
customer_repository.save(customer_3)

customer_4 = Customer('Kylar Stern', 'Standard', gym_2)
customer_repository.save(customer_4)




pdb.set_trace()