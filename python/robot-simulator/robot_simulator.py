# Globals for the directions
# Change the values as you see fit
EAST =180 
NORTH =90
WEST =0
SOUTH =270

class Robot:
    ADVANCE={EAST:'self.x+=1',NORTH:'self.y+=1',WEST:'self.x-=1',SOUTH:'self.y-=1'} 

    def __init__(self, direction=NORTH, x=0, y=0):
        self.direction=direction
        self.x=x
        self.y=y

    def move(self,instructions):
        for ins in instructions:
            if ins=='R':
                self.direction=(self.direction+90)%360
            elif ins=="L":
                self.direction=(self.direction-90)%360
            elif ins=='A':
                temp=Robot.ADVANCE.get(self.direction)
                exec(temp)
    @property
    def coordinates(self,):
        '''
        return {x,y}
        '''
        return (self.x,self.y)



