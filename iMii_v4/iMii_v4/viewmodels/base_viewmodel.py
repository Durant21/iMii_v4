class ViewModelBase:
    def __init__(self):
        self.errors = []
        self.error_status = 0

    @property
    def error_msg(self):
        msg = 'There are errors with your request: \n' + \
              '\n'.join(self.errors)

        return msg