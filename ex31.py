print "MY PURELY TEXT RPG"

print "Game input is done using numbers only."

print "You enter a cave.\n The path splits into two branches.\n Do you go left or right?"

path = raw_input("> ")

if path == "left":
    print ("The path goes downhill.\n The cavern collapses behind you.\nBefore you appears a orc.\nWhat do you do?") 
    print "1. Run"
    print "2. Hide"
    print "3. Attack with a nearby stone."
    
    orc = raw_input("> ")
    
    if orc =="1":
        print "Nowhere to run. Nowhere to hide. The orc hears you and attacks with his sword."
    elif orc == "2":
        print "You die of starvation."
    elif orc == "3":
        print "You hit the orc. However the attack is not enough to finish him off. He attacks you with his sword."
    else:
        print "Well, %s got you nowhere" %orc
        
    print "GAME OVER!"
    
elif path == "right"
    print "The path goes uphill.\nYou are exhausted by te time you reach the top.\n You hear the cavern collapse behind you."
    print "You reach a cliff. Below you can see a orc. The orc has a sword as well as a bow and arrow."
    print "You ponder on whether to navigate the narrow path next to the cliff to an opening on the other side, to jump across or to throw a stone at the orc..."    
    
    cliff = raw_input("> ")
    
    if cliff == "1"
    
