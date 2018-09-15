class Commit:

    def __init__(self, debug=False, amend=False, **kwargs):
        self.debug = debug
        self.amend = amend

    def run(self):
        print(f'Commiting... debug: {self.debug}, amend: {self.amend}')
