class PlayerCharacter:
    def __init__(self, name):
        self.name = name
        
    def run(self,left,right):
        print('my name is ' +left + right + self.name)
        return 'run'


player1 = PlayerCharacter('sani')
print(player1.run('45 ','65 '))

   
