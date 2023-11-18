import pygame,PyEngine
#sf=stockfish.Stockfish('stockfish_15.1_win_x64_avx2\\stockfish_15.1_win_x64_avx2\\stockfish-windows-2022-x86-64-avx2.exe')

screen=pygame.display.set_mode((600,600))
x,y=200,200
board=pygame.image.load('chessboard0.png').convert()
testPiece=pygame.image.load('player.png').convert()
screen.blit(board,(0,0))
screen.blit(testPiece,(x,y))
pygame.display.update()
pieces=[]
pieceUp=False
class piece:
    def __init__(self,type,positionId,team,x,y) -> None:
        self.type=type
        self.positionId=positionId
        self.team=team
        self.x=x
        self.y=y
        if self.type=='pawn':
            if self.team=='white':
                self.image=pygame.image.load('Assets\\TheRealPawn.png').convert()
            else:
                self.image=pygame.image.load('Assets\\PawnBlack.png').convert()
        if self.type=='knight':
            if self.team=='white':
                self.image=pygame.image.load('Assets\\Kight.png').convert()
            else:
                self.image=pygame.image.load('Assets\\KightBlack.png').convert()
        if self.type=='bishop':
            if self.team=='white':
                self.image=pygame.image.load('Assets\\Bishop.png').convert()
            else:
                self.image=pygame.image.load('Assets\\BishopBlack.png').convert()
        if self.type=='rook':
            if self.team=='white':
                self.image=pygame.image.load('Assets\\rook.png').convert()
            else:
                self.image=pygame.image.load('Assets\\rookBlack.png').convert()
        if self.type=='queen':
            if self.team=='white':
                self.image=pygame.image.load('Assets\\Queen.png').convert()
            else:
                self.image=pygame.image.load('Assets\\QueenBLACK.png').convert()
        if self.type=='king':
            if self.team=='white':
                self.image=pygame.image.load('Assets\\King.png').convert()
            else:
                self.image=pygame.image.load('Assets\\KingBLACK.png').convert()
        self.image.set_colorkey((255,255,255))
        screen.blit(self.image,(x,y))
        pygame.display.update()
        pieces.append(self)
    def move(self):
        self.mousex,self.mousey=pygame.mouse.get_pos()
        self.x,self.y=self.mousex-16,self.mousey-16
        screen.blit(self.image,(self.x,self.y))
    def dontMove(self):
        screen.blit(self.image,(customRound(self.x)+16,customRound(self.y)+12))
    def listen(self):
        global left
        if left:  
            PyEngine.checkHover(self.x-5,self.x+59,self.y-5,self.y+54,self.move,self.dontMove)
        else:
            self.x,self.y=customRound(self.x),customRound(self.y)
            screen.blit(self.image,(customRound(self.x)+16,customRound(self.y)+12))        
def customRound(x, base=75):
    return base * round(x/base)
def listenAll():
    global pieces
    for i in pieces:
        i.listen()

aPawn=piece('pawn',0,'white',0,450)
bPawn=piece('pawn',0,'white',75,450)
cPawn=piece('pawn',0,'white',150,450)
dPawn=piece('pawn',0,'white',225,450)
ePawn=piece('pawn',0,'white',300,450)
fPawn=piece('pawn',0,'white',375,450)
gPawn=piece('pawn',0,'white',450,450)
hPawn=piece('pawn',0,'white',525,450)
leftRook=piece('rook',0,'white',0,525)
rightRook=piece('rook',0,'white',525,525)
leftHorse=piece('knight',0,'white',75,525)
rightHorse=piece('knight',0,'white',450,525)
leftBishop=piece('bishop',0,'white',150,525)
rightBishop=piece('bishop',0,'white',375,525)
wQueen=piece('queen',0,'white',225,525)
wKing=piece('king',0,'white',300,525)

aPawnB=piece('pawn',0,'black',0,75)
bPawnB=piece('pawn',0,'black',75,75)
cPawnB=piece('pawn',0,'black',150,75)
dPawnB=piece('pawn',0,'black',225,75)
ePawnB=piece('pawn',0,'black',300,75)
fPawnB=piece('pawn',0,'black',375,75)
gPawnB=piece('pawn',0,'black',450,75)
hPawnB=piece('pawn',0,'black',525,75)
leftRookB=piece('rook',0,'black',0,0)
rightRookB=piece('rook',0,'black',525,0)
leftHorseB=piece('knight',0,'black',75,0)
rightHorseB=piece('knight',0,'black',450,0)
leftBishopB=piece('bishop',0,'black',150,0)
rightBishopB=piece('bishop',0,'black',375,0)
QueenB=piece('queen',0,'black',225,0)
KingB=piece('king',0,'black',300,0)
screen.blit(board,(0,0))
left=0
listenAll()
while True:    
    
    left=pygame.mouse.get_pressed()[0]
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            screen.blit(board,(0,0))
            listenAll()