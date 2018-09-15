class Push:

    def __init__(self, debug=False, tags=False, **kwargs):
        self.debug = debug
        self.tags = tags

    def run(self):
        print(f'Pushing... debug: {self.debug}, tags: {self.tags}')
