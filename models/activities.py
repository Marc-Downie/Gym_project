class Activity:

    def __init__(self, gym, activity_type, duration, difficulty, id=None):
        self.gym = gym
        self.activity_type = activity_type
        self.duration = duration
        self.difficulty = difficulty
        self.id = id
