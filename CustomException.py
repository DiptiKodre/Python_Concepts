class InvalidAgeError(Exception):
    """Custom exception for invalid age input."""

    def __init__(self, message="Age must be a positive integer"):
        self.message = message
        super().__init__(self.message)


def verify_age(age):
    if not isinstance(age, int) or age < 18:
        raise InvalidAgeError()
    return "Welcome!"


try:
    print(verify_age(-5))
except InvalidAgeError as e:
    print("Error:", e)
