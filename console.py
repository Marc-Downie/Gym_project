import pdb
from models.gym import Gym
from models.customer import Customer

import repositories.gym_repository as gym_repository
import repositories.customer_repository as customer_repository



gym_repository.delete_all()
customer_repository.delete_all()

gym_1 = Gym('Chromerias Gym')
gym_repository.save(gym_1)

gym_2 = Gym('MAXIMUM Gym')
gym_repository.save(gym_2)


customer_1 = Customer('Kip Gyle', 'Premium')
customer_repository.save(customer_1)

customer_2 = Customer('Gavin Gyle', 'Standard')
customer_repository.save(customer_2)

customer_3 = Customer('Karris White', 'Standard')
customer_repository.save(customer_3)

customer_4 = Customer('Kylar Stern', 'Standard')
customer_repository.save(customer_4)




pdb.set_trace()