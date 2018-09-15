class Add:

    def __init__(self, debug=False, update=False, **kwargs):
        self.debug = debug
        self.update = update

    def run(self):
        print(f'running add... update: {self.update}, debug: {self.debug}')
