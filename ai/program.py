class Program():
    def __init__(self, problem = None, search = None):
        self.problem = problem
        self.search = search
        self.percept

    def __call__(self, percept):
        return self.search(self.problem, percept)

    def update_state():
        pass

    





