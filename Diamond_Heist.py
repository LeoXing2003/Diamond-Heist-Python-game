from tkinter import*
from math import*
from time import*
import random

root = Tk()
screen = Canvas(root,width = 1000,height = 800,background = "white")


def initialvalues(): #Responsivle for storing all the values and variables needed
    global currentTime, xposition, yposition,xspeed,yspeed
    global xguards, yguards, guardspeed,levels
    global character,character_drawing,xmouse,ymouse
    global diamond, diamond_drawing
    global guardx1,guardy1,guardx2,guardy2,guardx3,guardy3
    global xlight1,ylight1,xlight2,ylight2,xlight3,ylight3,i,protip
    global instructions1,instructions2,instructions3
    global exitbutton,exitbuttontext
    global run,qpressed, l
    
    run = True
    xposition = 10
    yposition = 10
    xspeed = 0
    yspeed = 0
    character = 0
    character_drawing = 0
    diamond = 0
    diamond_drawing = 0
    guardx1 = 150
    guardy1 = 700
    guardx2 = 850
    guardy2 = 50
    guardx3 = 850
    guardy3 = 700
    xlight1 = 150
    levels = 0
    i = 0
    ylight1 = 200
    xlight2 = 850
    ylight2 = 550
    xlight3 = 350
    ylight3 = 700
    instructions1 = 0
    instructions2 = 0
    instructions3 = 0
    qpressed = False
    tips = ["In order to succeed at this game, you need to ensure that you do not lose!", "Colliding with the light beams will result in a game over!","Obtain the diamond to claim victory!","Do something more productive instead of playing games!","Remember to do your homework!"]
    protip = random.choice(tips)

def easy(): #When the player selects easy difficulty
    global l,buttonlight,buttonmedium,buttonhard,currentTime
    currentTime = 30
    l = 500 #Changes the length of the light beam based on the difficulty selected
    buttonlight.destroy() #Deletes the button
    buttonmedium.destroy()
    buttonhard.destroy()

def medium(): #Medium difficulty
    global l,buttonmedium,buttonlight,buttonhard,currentTime
    currentTime = 27
    l = 550 #When player choose medium or hard, the length of the light will be extended
    buttonmedium.destroy()
    buttonlight.destroy()
    buttonhard.destroy()

def hard(): #Hard difficulty
    global l,buttonmedium,buttonlight,buttonhard,currentTime
    currentTime = 25
    l = 700
    buttonmedium.destroy() #Deletes all other buttons apart from the back button
    buttonlight.destroy()
    buttonhard.destroy()

def back(): #The back button which takes the player back to the menu
    global button3,buttonlight,buttonmedium,buttonhard,buttonback 
    menu()
    button3.destroy() #Deletes all other buttons
    buttonmedium.destroy()
    buttonlight.destroy()
    buttonback.destroy()
    buttonhard.destroy()

def level():
    #the player can select their difficulty level here
    global button3,buttonlight,buttonmedium,buttonhard,buttonback
    button3.destroy() #Removes the setting button

    cover = screen.create_rectangle(0,0,1000,1000,fill = "white") #A rectangle to cover up the background

    #Button for easy difficulty
    buttonlight = Button(root,text = "Easy",font = "Arial 30",command = easy,anchor = CENTER)
    buttonlight.pack()
    buttonlight.place(x =50,y = 400,width = 250, height = 200)

    #Button for medium difficulty
    buttonmedium = Button(root,text = "Medium",font = "Arial 30",command = medium,anchor = CENTER)
    buttonmedium.pack()
    buttonmedium.place(x = 300,y = 400,width = 250,height = 200)

    #Button for hard difficulty
    buttonhard = Button(root,text = "Hard",font = "Arial 30",command = hard,anchor = CENTER)
    buttonhard.pack()
    buttonhard.place(x = 550,y = 400,width = 250,height = 200)

    #Button that takes the player back to the menu
    buttonback = Button(root,text = "back",font = "Arial 30", command = back,anchor = CENTER)
    buttonback.pack()
    buttonback.place(x = 100,y = 700,width = 200,height = 50)




    
def menu(): #Creates the buttons and title in the menu page
    global title, button1, button1text, button2, button2text,button3
    global buttonlight,buttonmedium,buttonhard

    background()
    
    
    title = screen.create_text(500,150,text = "DIAMOND HEIST",fill = "blue",font = "Helvetica 80")

    #Button if clicked on will call the run game function
    button1 = screen.create_rectangle(200, 650, 400, 750, fill="green", outline="green") 
    button1text = screen.create_text(300, 700, text="Play", font="Helvetica 30")

    #Button which if clicked on will call the instructions function
    button2 = screen.create_rectangle(650,750,850,650,fill = "blue",outline = "blue")
    button2text = screen.create_text(750,700,text  = "Instructions",font = "Helvetica 24")

    #Button allowing the player to choose the difficulty
    button3 = Button(root,text = "settings",font = "Arial 20", command = level,anchor = CENTER)
    button3.pack()
    button3.place(x = 400,y = 550,width = 250,height = 100)

    
    


def instruction():
    global instructions1,exitbutton,exitbuttontext,instructions2,instructions3,instructions4,instructions5,instructions6,instructions7,instructions8,instructions9,instructions10,button3
    cover = screen.create_rectangle(0,0,1000,1000,fill = "white") #A rectangle to cover up the background
    button3.destroy()

    #The instructions on the basics of the game
    instructions1 = screen.create_text(500,250,text = "A new priceless artifact had just been recently added to the exhibition room of the local museum",font = "caveat 20")
    sleep(0.05)
    instructions2 = screen.create_text(500,300,text = "and it was none other than the legendary and mythical blue diamond,",font = "caveat 20")
    instructions3 = screen.create_text(500,350,text = "which was prophesied to vanish without a trace just momentarily after it was unearthed",font = "caveat 20")
    instructions4 = screen.create_text(500,400,text = "As a notorious career criminal specializing in looting historical artifacts", font = "caveat 20")
    instructions5 = screen.create_text(500,450,text = "you contemplates greedily the immense luxuries and extravagance this bounty would bring you",font = "caveat 20")
    instructions6 = screen.create_text(500,500,text = "However, in order to successfully seize the diamond and escape unscathed from the highly secure museum,", font = "caveat 20")
    instructions7 = screen.create_text(500,550,text = "you will have to avoid the lethal light beams emitted by the handheld flashlights which were equipped",font = "caveat 20")
    instructions8 = screen.create_text(500,600,text = "to the three security guards stationed in the museum. This can be achieved by moving your character with arrow keys,", font = "caveat 18")
    instructions9 = screen.create_text(500,650,text = "“Let the prophecy come true, ” you said with a soft chuckle as you embark on this heist of a life time.",font = "caveat 20")
    instructions10 = screen.create_text(500,700,text = "Remember to select your difficulty from the settings first before playing!",font = "caveat 20")

    #Button in the instructions page which allows you to return to the menu
    exitbutton = screen.create_rectangle(430,900,620,750,fill = "red",outline = "red")
    exitbuttontext = screen.create_text(525,770,text = "return to main menu",font = "Helvetica 15")
    
 
def mouseClickHandler(event): #Tracks the position and movement of the mouse
    global exitbutton,exitbuttontext,instructions1,instructions2
    xmouse = event.x
    ymouse = event.y
    if xmouse in range(200,400) and ymouse in range(650,750):
        #When the button is clicked, the rungame function will be called
        rungame()
    elif xmouse in range(650,850) and ymouse in range(650,750):
        #Calls the instructions function when the respective button is clicked
        instruction()
        
    elif xmouse in range(430,620) and ymouse in range(750,900):
        #Calls the menu function when the respective button is clicked
        menu()

        #Deletes all unnecessary features such as buttons from the menu page as well as the instructions
        screen.delete(exitbutton,exitbuttontext,instructions1,instructions2,instructions3,instructions4,instructions5,instructions6,instructions7,instructions8,instructions9,instructions10)

    

def background(): #Draws the background
    global diamond, diamond_drawing
    screen.create_line(350,450,350,600,450,600,width = 10)
    screen.create_line(350,450,350,300,700,300,700,600,600,600,width = 10)
    screen.create_rectangle(450,650,600,600,fill = "white",outline = "black",width = 5)
    screen.create_rectangle(460,690,590,650,fill = "white",outline = "black",width = 5)
    screen.create_rectangle(470,720,580,690,fill = "white",outline = "black",width = 5)
    screen.create_rectangle(0,150,20,0,fill = "brown")

    diamond = PhotoImage(file = "diamond.gif")
    diamond_drawing = screen.create_image(530,400,image = diamond)

    
def endgame():
    global protip,qpressed
    cover2 = screen.create_rectangle(0,0,1000,800,fill = "white") 
    message = screen.create_text(500,300,text ="GAME OVER!",font = "caveat 50")
    
    pro = screen.create_text(400,400,text = "protip:",font = "caveat 20")
    tip = screen.create_text(500,500,text = protip,font = "caveat 20")

    if qpressed == True: 
        root.destroy()
    
    


def wingame():
    
    cover2 = screen.create_rectangle(0,0,1000,800,fill = "white") 
    victory = screen.create_text(500,400,text = "Congratulations you are the winner!",font = "caveat 20")
    if qpressed == True: 
        root.destroy()
    
        

def draw(): #Draws the character and the diamond
    global character
    character = screen.create_oval(xposition,yposition,xposition+10,yposition+10,fill = "yellow")
    

def update(): 
    global xposition,yposition

    
    if xposition in range(690,710) or xposition in range(330,350): #When the xcoordinate is the same as the wall
        if yposition in range(300,600): #Checks if the y coordinate is also the same as the wall
            #If the player is near the left wall
            if 325 <= xposition < 405:
                xposition = xposition - xspeed #Subtract xspeed from the xposition
            #If the player is near the right wall
            elif 595 <= xposition > 600: 
                xposition = 710 #Set player position to 710  
        else:
            #If the player is not colliding with any barriers
            xposition = xposition + xspeed #Increment xposition with xspeed
    else:
        xposition = xposition + xspeed


    #If the player is near the top wall
    if yposition in range(290,310):
        if xposition in range(350,700): #If the xcoordinate of the player is in the same range as the xcoordinate of the wall
            #Set yposition to 285
            yposition = 285
        else:
            yposition = yposition + yspeed #If the player is not near the top wall
    else:
        yposition = yposition + yspeed #Increment xposition by adding xspeed


    #If the player is near the bottom walls
    if yposition in range(590,610):
        if xposition in range(350,450) or xposition in range(600,700): #Checks if the xcoordinates is near the bottom walls
            yposition = 630 #Sets yposition to 630
        else:
            yposition = yposition + yspeed
    else:
        yposition = yposition + yspeed
   
    
def guards():#Creates and stores the guards
    global guardx1,guardy1,guardx2,guardy2,guardx3,guardy3,guard1,guard2,guard3
    guard1 = screen.create_oval(guardx1-50,guardy1-50,guardx1+50,guardy1+50,fill = "black")
    guard2 = screen.create_oval(guardx2-50,guardy2-50,guardx2+50,guardy2+50,fill = "yellow")
    guard3 = screen.create_oval(guardx3-50,guardy3-50,guardx3+50,guardy3+50,fill = "brown")
    

def light(): #Creates the light beams
    global xlight1,ylight1,xlight2,ylight2,xlight3,ylight3
    global guardx1,guardy1,guardx2,guardy2,guardx3,guardy3
    
    global light1, light2, light3, i,l

    #Draws the light beams onto the screen
    light1 = screen.create_line(guardx1, guardy1, xlight1, ylight1, fill="yellow", width=10)
    light2 = screen.create_line(guardx2, guardy2, xlight2, ylight2, fill="yellow", width=10)
    light3 = screen.create_line(guardx3, guardy3, xlight3, ylight3, fill="yellow", width=10)
    #Ensures that the light makes a complete rotation
    #This equation converts degrees to radians
    radians = i*pi/180 

    #Rotating light
    #Using trig ratios to rotate the light
    xlight1 = guardx1 - l*sin(2*radians)#Responsible for moving the light in a circular motion
    ylight1 = guardy1 - l*cos(2*radians)

    xlight2 = guardx2 + l*sin(2*radians)
    ylight2 = guardy2 - l*cos(2*radians)

    xlight3 = guardx3 - l*sin(2*radians)
    ylight3 = guardy3 + l*cos(2*radians)
   
    
    i += 1 #Constant updates the light beam 





def detectCollision(): #Responsible for checking collisions between the player and the light beams
    global xlight1,ylight1,xlight2,ylight2,xlight3,ylight3
    global guardx1,guardy1,guardx2,guardy2,guardx3,guardy3
    global xposition, yposition
    global run
    
    #If player's x position is between the edge of a light ray and a guard's x position - if not, then calculations won't be done to maintain game speed
    if (guardx1 <= xposition <= xlight1 or xlight1 <= xposition <= guardx1) or (guardx2 <= xposition <= xlight2 or xlight2 <= xposition <= guardx2) or (guardx3 <= xposition <= xlight3 or xlight3 <= xposition <= guardx3):
       
        if (xlight1 - guardx1) != 0 and (xlight2 - guardx2) != 0 and (xlight3 - guardx3) != 0:
            
            slope1 = (ylight1 - guardy1)/(xlight1 - guardx1)
            slope2 = (ylight2 - guardy2)/(xlight2 - guardx2)
            slope3 = (ylight3 - guardy3)/(xlight3 - guardx3)

            
            yint1 = ylight1 - (slope1 * xlight1)
            yint2 = ylight2 - (slope2 * xlight2)
            yint3 = ylight3 - (slope3 * xlight3)

            
            y1 = (slope1 * xposition) + yint1
            y2 = (slope2 * xposition) + yint2
            y3 = (slope3 * xposition) + yint3
            

            #checks if the xcoordinates of the player is between the xcoordinate of the guard and light
            #Checks if the yposition of the light beam is within a 10 coordinates difference when compared to the player
            if (guardx1 <= xposition <= xlight1 or xlight1 <= xposition <= guardx1) and abs(yposition - y1) <= 10:
                
                run = False 
                print("Hit1")
            if (guardx2 <= xposition <= xlight2 or xlight2 <= xposition <= guardx2) and abs(yposition - y2) <= 10:
                run = False
                print("Hit2")
            if (guardx3 <= xposition <= xlight3 or xlight3 <= xposition <= guardx3) and abs(yposition - y3) <= 10:
                run = False 
                print("Hit3")

        else: 
            if xposition == guardx1 and (ylight1 <= yposition <= guardy1 or guardy1 <= yposition <= ylight1):
                run = False
                print("Hit1")
            if xposition == guardx2 and (ylight2 <= yposition <= guardy2 or guardy2 <= yposition <= ylight2):
                run = False
                print("Hit2")
            if xposition == guardx3 and (ylight3 <= yposition <= guardy3 or guardy3 <= yposition <= ylight3):
                run = False
                print("Hit3")
    elif xposition in range(520,550) and yposition in range(390,430):
        run = False

#Displays initial time
def displayInitialTime():
    global timeText, currentTime
    timeText = screen.create_text(500, 100, text=("Time Left: " + str(currentTime)), font="Arial 20")

#Updates time
def updateTime():
    global currentTime, timeText, timePassed, startTime, run

    timeNow = time()
    timePassed = timeNow - startTime #The amount of time passed is the current time substract the starting time

    if timePassed >= 1: #If difference between times is one second - update timer
        screen.delete(timeText)
        currentTime = currentTime - 1 #Subtract one second from the current time
        timeText = screen.create_text(500, 100, text=("Time Left: " + str(currentTime)), font="Arial 20")
        startTime = time()

    #If time is up, game over
    if currentTime <= 0:
        run = False
    

def keydownhandler(event): #Responsible for detecting any arrow keys that had been pressed
    global xspeed, yspeed,xposition,yposition,run,qpressed

    if event.keysym == "Left": #when the left arrow is pressed
        xspeed = -5 #Move the player 5 corrdinates backwards

       
    #When the right arrow key is pressed
    elif event.keysym == "Right":
    #Move the player forward by 5 coordinates
        xspeed = 5

    elif event.keysym == "Up":
        yspeed = -5

    elif event.keysym == "Down":
        yspeed = 5

    elif event.keysym == "q" or event.keysym == "Q":
        qpressed = True #If the q key is pressed, the qpressed variable will be set True, which will close the game
        

    else:
        return 0

def keyuphandler(event): #When the key is released, set speed to 0
    global xspeed,yspeed
    xspeed = 0
    yspeed = 0
    
def rungame(): #Main loop of the game
    global run, button3, startTime, timePassed
    initialvalues()
    background()
    startTime = time()
    displayInitialTime()
    
    while run == True and qpressed == False:
        draw()
        light()
        guards()
        detectCollision()
        updateTime()
        
          
        screen.update()
        sleep(0.03)

        #Deletes the objects in the game to prevent overlapping objects 
        screen.delete(character, light1, light2, light3,guard1,guard2,guard3,button1,title,button1text,button2,button2text,instructions1)
        button3.destroy()
        update()    
        
    if xposition in range(400,600) and yposition in range(350,450): #If the player reaches the diamond call wingame function
        wingame()
    else:
        #If the player is hit by the light beams, call endgame function
        endgame()


root.after( 0, menu)
screen.bind( "<Button-1>", mouseClickHandler )
screen.bind("<Key>",keydownhandler)
screen.bind("<KeyRelease>",keyuphandler)
screen.pack()
screen.focus_set()
root.mainloop()





