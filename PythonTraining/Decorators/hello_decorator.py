def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


@decorator
def say_whee():
    print("Whee!")

print(say_whee()) # Check Code
