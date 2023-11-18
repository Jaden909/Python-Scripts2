import Computer,pygame,PyEngine,locale
windowOpen=False
window=pygame.image.load('Apps\\IDE\\media\\screen1.png')
font=pygame.font.SysFont('arial',15)
currentTyped=''
currentLine=1
line=1
lines=['']
E=''
def loop():
    global windowOpen,currentTyped,currentLine,line,lines
    line=1
    if windowOpen==True:
        Computer.screen.blit(window,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.TEXTINPUT:
                print(font.size(event.dict.get('text'))[0])
                currentTypedList=list(currentTyped)
                currentTypedList.append(event.dict.get('text'))
                currentTyped=''.join(currentTypedList)
                lines.pop(currentLine-1)
                lines.insert(currentLine-1,currentTyped)
                
            if event.type==pygame.KEYDOWN:
                keys=pygame.key.get_pressed()
                if keys[pygame.K_RETURN]:
                    #print('return')
                    #lines.append(currentTyped)
                    lines.insert(currentLine,'')
                    currentTyped=''
                    currentLine+=1
                if keys[pygame.K_BACKSPACE]:
                    currentTypedList=list(currentTyped)
                    if len(currentTypedList)>0:
                        currentTypedList.pop()
                        currentTyped=''.join(currentTypedList)
                        lines.pop(currentLine-1)
                        lines.insert(currentLine-1,currentTyped)
                if keys[pygame.K_DOWN]:
                    if currentLine<51 and len(lines)>currentLine: 
                        currentLine+=1
                    try:
                        currentTyped=lines[currentLine-1]
                    except:
                        pass
                if keys[pygame.K_UP]:
                    if currentLine>1:
                        currentLine-=1
                    try:
                        currentTyped=lines[currentLine-1]
                    except:
                        pass
                if keys[pygame.K_F5]:
                    script='\n'.join(lines)
                    #print(script)
                    try:
                        exec(compile(script,'CustomScript','exec'))
                    except NameError as error:
                        print(error)
                    except:
                        print('An unknown error occured')
                if keys[pygame.K_TAB]:
                    # doesn't stick
                    lines[currentLine-1]+='    '
        for lineTxt in lines:
            #try:
            #    g=lines[line]
            #except IndexError:
            #    lineTxt+='|'
            Computer.screen.blit(font.render(lineTxt,True,'black'),(10,line*15+50))
            line+=1
        
            tempLine=lines[currentLine-1]
            width=font.size(tempLine)
                #Read whole line for kerning
                
            #for char in tempLine:
            #    width+=font.size(char)[0]
                
            Computer.screen.blit(font.render('|',True,'black'),(width[0]+10,currentLine*15+50))
           
        exitButton.listen()
def init():
    global windowOpen,exitButton
    def closeWindow():
        global windowOpen
        windowOpen=False
        pygame.key.stop_text_input()
    if windowOpen==False:
        windowOpen=True
    windowX,windowY=0,0
    exitButton=PyEngine.GameButton(x=windowX+580,y=windowY,imageResX=60,imageResY=40,image=None,function=closeWindow,hover=True,hoverSprite=Computer.linkcursorImg,notHoverSprite=Computer.cursorImg)
    pygame.key.start_text_input()
def config():
    pass