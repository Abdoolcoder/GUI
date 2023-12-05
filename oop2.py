class Abdul():
    def __init__(self,name,age):
        if age > 18:
            self._name = name
            self._age = age

    def run(self):
        print('i am ' + str(self._age) + ' old')

player1 = Abdul('daddy',30)
player1.run = '50'

dam = player1.run()
