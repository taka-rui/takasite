class Human:
    class_name = "Human"

    def __init__(self):
        self.name = "大泉"

    def show(self):
        print(self.name)

class Hoge:
    class_call_count = 0

    def __init__(self):
        Hoge.class_call_count += 1

Hoge()
print(Hoge.class_call_count)

Hoge()
print(Hoge.class_call_count)

Hoge()
print(Hoge.class_call_count)