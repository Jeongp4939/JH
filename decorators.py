
def decorator(func):
    def decorated(input_text):
        print('함수 시작!')
        func(input_text)
        print('함수 끝!')
    return decorated

@decorator
def hello_world(input_text):
    print(input_text)

hello_world('Hello World!')

def decorator2(func):
    def decorated(width, height):
        if width < 0 or height < 0:
            print('Error')
        else:
            func(width, height)
    return decorated

@decorator2
def rectangle(width, height):
    print(width * height)
@decorator2
def triangle(width, height):
    print(width * height * (1/2))

rectangle(-1, 2)
triangle(2, 3)
#
#
# class User:
#     def __init(self, auth):
#         self.is_authenticated = auth
#
# user = User(auth = False)
#
# rectangle(user, 10, 10)
# triangle(user, 10, 10)