class CustomerAlreadyExistsException(Exception):
    def __init__(self, message="Customer already exists."):
        super().__init__(message)
        self.message = message


class CustomerNotFoundException(Exception):
    def __init__(self, message="Customer not found."):
        super().__init__(message)
        self.message = message


class EntityNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class EntityAlreadyExistsException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message
