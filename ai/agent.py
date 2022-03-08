from asyncio import proactor_events


class Agent():
    def __init__(self, program=None,search=None):
        self.program = program 
        self.search = search

    
    def update_state(self, state, action):
        pass

