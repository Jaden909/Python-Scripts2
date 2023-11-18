import pygame,random
screen=pygame.display.set_mode((600,600))

population=99
healthy=population
infected=1
dead=0
people=[]
clock=pygame.time.Clock()
#start=time.time()
pygame.font.init()
#print(time.time()-start)
font=pygame.font.SysFont('comic sans',20)
healthyPeople=font.render(f'Healthy: {healthy}',True,'black')
infectedPeople=font.render(f'Infected: {infected}',True,'black')
deadPeople=font.render(f'Dead: {dead}',True,'black')
class Person:
    def __init__(self,infected,x,y,id,immunity):
        self.infected=infected
        self.x=x
        self.y=y
        self.id=id
        self.immunity=immunity
        self.dead=False
        self.dest=(random.choice(range(568)),random.choice(range(568)))
        if infected:
            self.image=pygame.image.load('sick.png')
        else:     
            self.image=pygame.image.load('healthy1.png')
    def show(self):
        screen.blit(self.image,(self.x,self.y))
    def move(self):
        
        if self.x<self.dest[0]:
            self.x+=1
        if self.x>self.dest[0]:
            self.x-=1
        if self.y<self.dest[1]:
            self.y+=1
        if self.y>self.dest[1]:
            self.y-=1 
        if self.x==self.dest[0] and self.y==self.dest[1]:
            self.dest=(random.choice(range(568)),random.choice(range(568)))
        if self.x>568:
            self.x=568
        if self.x<0:
            self.x=0
        if self.y>568:
            self.y=568
        if self.y<0:
            self.y=0   
        #for i in range(random.choice(range(50))):
        #    self.x+=random.choice(range(-1,2))
        #    self.y+=random.choice(range(-1,2))
            
        if self.infected and not self.dead:
            centerX=self.x+16
            centerY=self.y+16
            for person in people:
                personCenterX=person.x+16
                personCenterY=person.y+16
                if personCenterX>centerX and personCenterX<centerX+32:
                    if personCenterY>centerY and personCenterY<centerY+32:
                        sickness.physicalContact(person)
            sickness.fatality(self)
    def infect(self):
        global healthy,infected
        self.infected=True
        self.image=pygame.image.load('sick.png')
        healthy-=1
        infected+=1
    def die(self):
        global dead,infected
        self.dead=True
        dead+=1
        infected-=1
        for person in people:
            if person.id==self.id:
                people.pop(people.index(person))
class Virus:
    'transmissionRate: x% chance of infection, mortalityRate: 0.x% chance of death, airbourne: can infect in a radius around infected'
    def __init__(self,transmissionRate:int,mortalityRate:int,airbourne:bool,mutationRate):
        self.transmissionRate=transmissionRate
        self.mortalityRate=mortalityRate
        self.airbourne=airbourne
        self.mutationRate=mutationRate
        
    def physicalContact(self,target):
        roll=random.choice(range(0,101))
        #print(roll)
        if roll<self.transmissionRate-target.immunity and not target.infected:
            target.infect()
            self.mutate()
    def fatality(self,target):
        roll=random.choice(range(0,1001))
        if roll<self.mortalityRate-target.immunity:
            target.die()
    def mutate(self):
        roll=random.choice(range(0,1001))
        if roll<self.mutationRate:
            stat=random.choice(range(0,3))
            if stat==0:
                self.transmissionRate+=random.choice(range(-1,2))
            if stat==1:
                self.mortalityRate+=random.choice(range(-1,2))
            if stat==2:
                self.mutationRate+=random.choice(range(-1,2))

        
sickness=Virus(15,11,False,100)
patient0=Person(True,300,300,population+1,1)
transmission=font.render(f'Transmission Rate: {sickness.transmissionRate}',True,'black')
mortality=font.render(f'Mortality Rate: {sickness.mortalityRate}',True,'black')
mutation=font.render(f'Mutation Rate: {sickness.mutationRate}',True,'black')
for i in range(population):
    y=Person(False,random.choice(range(601)),random.choice(range(601)),i,10)
    #print(y)
    people.append(y)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    screen.fill('white')
    if not patient0.dead:
        patient0.show() 
        patient0.move() 
    #print(people) 
    for person in people:
        person.show()
        person.move()
        #sickness.physicalContact(person)
    healthyPeople=font.render(f'Healthy: {healthy}',True,'black')
    infectedPeople=font.render(f'Infected: {infected}',True,'black')
    deadPeople=font.render(f'Dead: {dead}',True,'black')
    transmission=font.render(f'Transmission Rate: {sickness.transmissionRate}',True,'black')
    mortality=font.render(f'Mortality Rate: {sickness.mortalityRate}',True,'black')
    mutation=font.render(f'Mutation Rate: {sickness.mutationRate}',True,'black')
    screen.blit(healthyPeople,(0,0))
    screen.blit(infectedPeople,(0,25))
    screen.blit(deadPeople,(0,50))
    screen.blit(transmission,(0,525))
    screen.blit(mortality,(0,550))
    screen.blit(mutation,(0,575))
    pygame.display.update()
    #clock.tick(10)