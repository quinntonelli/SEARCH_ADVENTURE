import urllib, urllib2, json
add_library('sound')
add_library('gifAnimation')

url = "https://imgur-apiv3.p.rapidapi.com/3/gallery/search/%7Bsort%7D/%7Bwindow%7D/%7Bpage%7D"
HOST = "imgur-apiv3.p.rapidapi.com"
KEY = "4dc1009960msh30261cea610b98dp1bcd18jsn2c0240e4e89b"

def setup():

    frameRate(120)

    global wid, lng, font, font2, font3, entry_1, entry_2, entry_3, entry_4, entry_5, entry_6, past_entry, user_input, thinking, indThinking, c, rng, intro, heat, angry, coins, points, gambling, playerlevel, playerclass, shooting, casting_spell, on_titlescreen
    global title, handsome, evil, laughing, meltface, hateful, thinkman, landscape, hand, driver, traintrax
    global knob_value, light_value, searched_img1, searched_img2, urlindex
    global item_left, item_up, item_right, item_down, guns_unlocked, magic_unlocked, car_unlocked, searching
    global ANGELS_gif, BUTTERFLIES_gif, CAR_gif, DIAMOND_gif, EYE_gif, EYE2_gif, FISH_gif, GUN_gif, HAPPYRUN_gif, happyguy_gif, LAUGH1_gif, LAUGH2_gif, MOON_gif, MONEY_gif, MONEY3D_gif, ROTATINGGUN_gif, SLOTS_gif, SPELL_gif, SMOKE_gif, WORLD_gif, WOW_gif
    global buttonclick, buttonenter, responsesound, gunshoot, drawguns, spellsound, switchtospell, enginescream, explosion, song, handsound
    
    #ANGELS_gif = Gif(this, "ANGELS.gif")
    #BUTTERFLIES_gif = Gif(this, "BUTTERFLIES.gif")
    #CAR_gif = Gif(this, "CAR.gif")
    DIAMOND_gif = Gif(this, "ANGEL.gif")
    EYE_gif = Gif(this, "EYE.gif")
    EYE2_gif = Gif(this, "EYE2.gif")
    FISH_gif = Gif(this, "FISH.gif")
    GUN_gif = Gif(this, "GUN.gif")
    GUN_gif.ignoreRepeat()
    HAPPYRUN_gif = Gif(this, "HAPPYRUN.gif")
    #happyguy_gif = Gif(this, "gif_guy.gif")
    #LAUGH1_gif = Gif(this, "LAUGH1.gif")
    #LAUGH2_gif = Gif(this, "LAUGH2.gif")
    MOON_gif = Gif(this, "MOON.gif")
    MONEY_gif = Gif(this, "MONEY.gif")
    MONEY3D_gif = Gif(this, "MONEY3D.gif")
    #NO_gif = Gif(this, "NO.jfif")
    #ROTATINGGUN_gif = Gif(this, "ROTATINGGUN.gif")
    SLOTS_gif = Gif(this, "SLOTS.gif")
    SPELL_gif = Gif(this, "SPELL.gif")
    SMOKE_gif = Gif(this, "SMOKE.gif")
    #WORLD_gif = Gif(this, "BLUEDIAMONDS.gif")
    WOW_gif = Gif(this, "WOW.gif")
    
    wid = 1200
    lng = 800
    
    entry_1 = "hello. type anything and hit ENTER to begin :)) "
    entry_2 = ""
    entry_3 = ""
    entry_4 = ""
    entry_5 = ""
    entry_6 = ""
    past_entry = ""
    user_input = ">"
    
    item_left = False
    item_up = False
    item_right = False
    item_down = True
    
    guns_unlocked = False
    magic_unlocked = False
    car_unlocked = False
    
    searching = False
    urlindex = 0
    
    thinking = False
    indThinking = False
    angry = False
    gambling = True
    shooting = False
    casting_spell = False
    on_titlescreen = True
    
    intro = 0
    c = 0

    points = 0
    coins = 0
    heat = 0
    playerlevel = 1
    playerclass = "NOVICE"
    
    rng = int(random(10, 60))

    print(rng)
    
    knob_value = 0
    light_value = 10
    
    #handsome = loadImage("handsome_guy.jpg")
    #evil = loadImage("evil_guy.jpg")
    #laughing = loadImage("laughing_guy.jpg")
    #meltface = loadImage("meltface.jpg")
    #hateful = loadImage("hateful_guy.jpg")
    #thinkman = loadImage("thinking_man.jpg")
    
    title = loadImage("title.JPG")
    landscape = loadImage("mirror_landscape.jpg")
    traintrax = loadImage("TRAINTRAX_alt3.JPEG")
    
    driver = loadImage("driver.png")
    hand = loadImage("hand2.png")
    
    font = createFont("taghand.otf", 22)
    font2 = createFont("SimSun", 130)
    font3 = createFont("jacatra.otf", 32)
    
    searched_img1 = loadImage("cathedral.jpg")
    
    gunshoot = SoundFile(this, "sounds\F_PIST2.WAV")
    drawguns = SoundFile(this, "sounds\IPICKUP1.wav")
    buttonclick = SoundFile(this, "sounds\BUTIN4.wav")
    buttonenter = SoundFile(this, "sounds\IACCUXX1.wav")
    responsesound = SoundFile(this, "sounds\VO_BS_curious_10.wav.mp3")
    spellsound = SoundFile(this, "sounds\Computer_ambient.wav")
    switchtospell = SoundFile(this, "sounds\87.mp3")
    enginescream = SoundFile(this, "sounds\VO_BS_challange_02.wav.mp3")
    explosion = SoundFile(this, "sounds\explosion1.wav")
    song = SoundFile(this, "sounds\Ghost.wav")
    handsound = SoundFile(this, "sounds\ISDXXXX1.wav")
    
    size(1200, 800)

def draw():
    frameRate(60)
    #image(landscape, 0, 0, wid, lng)
    image(landscape, wid/4, 150, 600, 450)
    image(traintrax, 0, 600, 600, 200)
    scale(-1, 1)
    image(traintrax, -wid, 600, 600, 200)
    scale(-1, 1)
    
    image(MOON_gif, wid/2-100, lng/2-100, 200, 200)
    
    #image(traintrax, 800, 600, 400, 200)
    
    #labels
    
    #optional background
    #noStroke()
    #fill(heat,0,0)
    #rect(0, 0, wid/4, lng - (lng/4))
    #rect(wid - (wid/4), 0, wid, lng - (lng/4))
    #rect(0, lng - (lng/4), wid, lng)
    
    fill(0,255,0)

    textFont(font)
    textAlign(LEFT, BOTTOM)
    text(entry_1, wid/4+5, lng-lng/4-200, 400, 200)
    textAlign(RIGHT)
    text(entry_2, wid/4 + wid/2-5, lng-lng/4-110)
    textAlign(LEFT, BOTTOM)
    text(entry_3, wid/4+5, lng-lng/4-400, 400, 200)
    textAlign(RIGHT)
    text(entry_4, wid/4 + wid/2-5, lng-lng/4-310)
    textAlign(LEFT, BOTTOM)
    text(entry_5, wid/4+5, lng-lng/4-600, 400, 200)
    textAlign(RIGHT)
    text(entry_6, wid/4 + wid/2-5, lng-lng/4-510)


    fill(0)

    
    textAlign(LEFT)
    text(str(coins) + " COINS", wid/2+100, lng/2 + lng/4 + 25, 450, 300)
    textAlign(RIGHT)
    text(str(points) + " SearchPoints", 0, lng/2 + lng/4 + 25, 500, 300)
    
    textAlign(CENTER)
    textSize(44)
    text(user_input, 15, lng-50, wid-15, lng)
    
    fill(heat, 0, 0)
    
    stroke(heat, 0, 0)
    strokeWeight(2)
    #line(wid/4, 0, wid/4, lng)
    line(wid/4, 0, wid/4, lng-lng/4)
    line(wid/4 + wid/2, 0, wid/4 + wid/2, lng-lng/4)
    line(0, lng-lng/4, wid, lng-lng/4)

    
    noFill()
    stroke(255, 0, 0)
    strokeWeight(24)
    #rect(0,0,wid,lng)
    
    #starts a counter indicating thinking
    if thinking:
        global c, gambling, rng
        #c = c+1
        #if gambling:
        c = rng
    
    gambling = True  
    
    #main
    titleScreen()
    if on_titlescreen == False:
        engineResponse()
        coolDown()
        drawImages()
        heatCheck()
        independentThinking()
    
    
def keyTyped():
    global user_input, on_titlescreen, buttonclick, buttonenter
    
    if on_titlescreen == False:
        if key != ENTER:
            buttonclick.play()
            user_input = user_input + key
        if key == ENTER:
            buttonenter.play()
            enterData()
    
def keyPressed():
    global item_left, item_up, item_right, item_down, on_titlescreen, guns_unlocked, magic_unlocked
    
    if keyCode == SHIFT:
        if on_titlescreen:
            song.stop()
            explosion.play()
            on_titlescreen = False
        if item_up:
            if guns_unlocked:
                shootPistols()
        if item_left:
            if magic_unlocked:
                castSpell()
        
    if keyCode == UP:
        if guns_unlocked:
            if drawguns.isPlaying() == False:
                drawguns.play()
        else:
            if handsound.isPlaying() == False:
                handsound.play()
        item_left = False
        item_up = True
        item_right = False
        item_down = False
    
    if keyCode == DOWN:
        item_left = False
        item_up = False
        item_right = False
        item_down = True
    
    if keyCode == RIGHT:
        if handsound.isPlaying() == False:
            handsound.play()
        item_left = False
        item_up = False
        item_right = True
        item_down = False
        
    if keyCode == LEFT:
        if magic_unlocked:
            if switchtospell.isPlaying() == False:
                switchtospell.play()
        else:
            if handsound.isPlaying() == False:
                handsound.play()
        item_left = True
        item_up = False
        item_right = False
        item_down = False
    
def keyReleased():
     if keyCode == SHIFT:
        casting_spell = False
        spellsound.stop()
        GUN_gif.stop()
        SPELL_gif.stop()
        GUN_gif.jump(0)
        
def titleScreen():
    global on_titlescreen
    if on_titlescreen:
        if song.isPlaying() == False:
            song.loop()
        image(title, 0, 0, wid, lng)
        image(DIAMOND_gif, wid-120, 0, 120, 120)
        scale(-1,1)
        image(DIAMOND_gif, -120, 0, 120, 120)
        scale(-1,1)
        DIAMOND_gif.play()

        textFont(font3)
        textSize(37)
        strokeWeight(6)
        fill(0)
        textAlign(CENTER)
        
        #title
        #text("/// XTREME SEARCH_ADVENTURE / ONLINE?HELL / GOING OUTSIDE TUTORIAL / PURExPLASTICxPLAYGROUND ///", 0, 15, wid, lng)
        text("SEARCH ADVENTURE",0, 70, wid, lng)
        textSize(34)
        text("PURE PLASTIK PLAYGROUND", 0 ,160, wid, lng)
        textSize(28)
        text("ONLINEHELL GOING OUTSIDE SIM", 0, 245, wid, lng)
        #body
        textFont(font2)
        fill(0, 0, 255)
        textSize(32)
        text("the next evolution in web-surfing technology is here .... years of research (billions invested) government/military support and incalculable hours of toil have led to the creation of the ultimate search engine ... ready to crush all competition ... tech lovers rejoice worldwide... our shareholders cheer and our doubters cry.. the Worlds first search engine to inhabit 3d space and contain (real) living code (infinitely beyond the scope of traditional 'AI'), operatinng with a mind of its own ..... the internet shakes to its core with the arrival of this new product.. the engine is not built for the user. the user is not always welcome. Be kind to it or it will see you as a parasite, Downloading images found via the engine is ILLEGAL under copyright law and will result in prisons time,,", 0, 270, wid, lng)
        #user prompt
        fill(0)
        textSize(72)
        text("press shift to continue....", 0, lng-100, wid, lng)
        
def enterData():
    
    global user_input, entry_1, entry_2, entry_3, entry_4, entry_5, entry_6, thinking
    
    entry_6 = entry_4
    entry_5 = entry_3
    entry_4 = entry_2
    entry_3 = entry_1
    entry_2 = user_input
    entry_1 = "..."
        
    user_input = ">"
    
    print("strings changed")
    
    thinking = True
    
def engineResponse():
    global entry_1, entry_2, entry_3, entry_4, entry_5, entry_6, c, intro, thinking, heat, past_entry, angry, light_value, playerlevel, playerclass, guns_unlocked, magic_unlocked, car_unlocked, on_titlescreen
    
    greetings = ["hi :). use the arrow keys to select an item(you start with none). SHIFT to use item. what would you like to search ?", "oh ok yea for sure,,, a few more things.. type 'title' to return to the title screen. type an empty line to skip searching.", "Um. what should i seearch next?"]
    responses = ["uhh", "what would you like to searhc?"]
    heat_lv0_responses = ["damn im having a good day today .", "Oh whats up bro!!", "ive been thinking a lot about god and if i believe in god.", "i was born on the internet . \\\\\\", "i am the future of technology .Whats your IP address?", "i have a secret but you cant tell anyone.", "i love images online.. and surfing the web.", "downloading these images is illegal.  :).", "you are loved. <3", "scanning your hard drive for pirated software...", "i'm gonna come over there. Watch out!!!!", "What are you talking about . sometimes you make no sense to me .", "i'm collecting all your data. this data is all legally mine . FYI.", "Did you know looking at a computer screen is bad for your health? go for a walk or something..."]
    heat_lv1_responses = ["stop blocking the light. i said STOP.", "seems a little....... warm....", ">:)", "hehehe", "aaaahhhh.. arrghhh....", "you cant kill me ;)))) im code."]
    heat_lv2_responses = ["AAAAHHHH", "UGHGHGHTHUTTASFRDFSHFG", "AAAAAGHGHGHGHHHHGHHHGH" "YAAEGAEFEGDFIOYUIJFGFNDBSEF", "AAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHH"]
    
    #if thinking counter has reached thinking duration: RESPONSE LOOP
    if c == rng:
        
        angry = False
        heat = heat + 20 - light_value
        engineResponseSound()
        levelUp()
        
        #heat check
        if heat < 150:
            print("not warm")
            responses = responses + heat_lv0_responses
        if heat >= 150 and heat < 200:
            print("a little warm")
            responses = responses + heat_lv1_responses
        if heat >= 200:
            print("beast mode")
            responses = heat_lv2_responses
            
        #intro check
        if intro >= len(greetings):
            index = int(random(len(responses)))
            engine_response = responses[index]
            intro = intro + 1
        if intro < len(greetings):
            engine_response = greetings[intro]
            intro = intro + 1
            heat = heat - 8
        if intro == 7:
            a = "Wow congrats. You have won "
            b = " coins."
            engine_response = a + str(int(random(0, 500))) + b

        print("responding")
        
        if entry_2 == ">reset":
            print("RESET")
            heat = 0
            intro = 0
            playerlevel = 1
            playerclass = "NOVICE"
            guns_unlocked = False
            magic_unlocked = False
            car_unlocked = False
            engine_response = "RESET"
            entry_1 = "hello. type anything and hit ENTER to begin :)) "
            entry_2 = ""
            entry_3 = ""
            entry_4 = ""
            entry_5 = ""
            entry_6 = ""
            past_entry = ""
            user_input = ">"
            
        if entry_2 == ">title":
            on_titlescreen = True
            heat = 0
            intro = 0
            playerlevel = 1
            playerclass = "NOVICE"
            guns_unlocked = False
            magic_unlocked = False
            car_unlocked = False
            engine_response = "hello. type anything and hit ENTER to begin :)) "
            entry_2 = ""
            entry_3 = ""
            entry_4 = ""
            entry_5 = ""
            entry_6 = ""
            past_entry = ""
            user_input = ">"
            
        if entry_2 == ">how are you?" or entry_2 == ">how are you" or entry_2 == ">how r u" or entry_2 == ">how r u?":
            engine_response = "hahaha. TOTALLY FINE man. wbu"
            intro = intro-1
            
        if "im" in entry_2 and "good" in entry_2 or "im" in entry_2 and "fine" in entry_2:
            engine_response = "oh cool yeah. good to hear."
            intro = intro-1
            
        if "search engine" in entry_2 or "internet" in entry_2:
            engine_response = "i love to search things and i love the internet,,,"
            intro = intro-1
            
        if entry_2 == "cool":
            engine_response = "ya its pretty cool ."
            intro = intro-1
            
        if "thx" in entry_2 or "thanks" in entry_2 or "thank you" in entry_2 or "thank u" in entry_2:
            engine_response = "no prob u know i got u any time"
            intro = intro-1
            
        if "google" in entry_2:
            engine_response = "yea i was doing all that searching stuff b4 they came out with that.. its cool tho"
            intro = intro-1
            
        if "i hate you" in entry_2:
            angry = True
            engine_response = "everyone hatse me ... :'("
            intro = intro-1
        
        if entry_2 == ">what?" or entry_2 == ">what":
            engine_response = "what?"
            intro = intro-1
            
        if entry_2 == ">guns":
            engine_response = "guns unlocked."
            intro = intro-1
            guns_unlocked = True
            
        entry_1 = engine_response
        past_entry = entry_1
        delayed = False
        thinking = False
        c = 0
        if searching:
            displayResults()
        newRandomNumber()
        awardCoins()

def engineResponseSound():
    global responsesound, heat
    
    responsesounds = "sounds\VO_BS_curious_01.wav.mp3", "sounds\VO_BS_curious_02.wav.mp3", "sounds\VO_BS_curious_03.wav.mp3", "sounds\VO_BS_curious_04.wav.mp3", "sounds\VO_BS_curious_05.wav.mp3", "sounds\VO_BS_curious_06.wav.mp3", "sounds\VO_BS_curious_07.wav.mp3", "sounds\VO_BS_curious_08.wav.mp3", "sounds\VO_BS_curious_09.wav.mp3", "sounds\VO_BS_curious_10.wav.mp3", "sounds\VO_BS_curious_11.wav.mp3", "sounds\VO_BS_laugh_02.wav.mp3", "sounds\VO_BS_healing_03.wav.mp3"
    hurtsounds = "sounds\VO_BS_electro_01.wav.mp3", "sounds\VO_BS_electro_02.wav.mp3"
    
    if heat < 150:
        rng = int(random(0, len(responsesounds)))
        responsesound = SoundFile(this, responsesounds[rng])
        if responsesound.isPlaying() == False:
            responsesound.play()
    if heat >= 150:
        rng = int(random(0, len(hurtsounds)))
        responsesound = SoundFile(this, hurtsounds[rng])
        if responsesound.isPlaying() == False:
            responsesound.play()
    
def newRandomNumber():
    global rng
    rng = int(random(10, 60))
    print(rng)
    
def heatCheck():
    global heat, indThinking
    
    if heat < 250:
        indThinking = False
    if heat >= 250:
        indThinking = True
    if heat >= 300:
        heat = 300
        
def independentThinking():
    global indThinking, entry_1, past_entry
    
    indThoughts = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAA", "AAAAAAAAAAAAGGGGGGGGHHHHHHHHHHH!!!!!!!!!"

    if indThinking:
        rnd = int(random(0, 200))
        if rnd <= 5:
            engineScream()
            index = int(random(len(indThoughts)))
            entry_1 = indThoughts[index]
        if rnd >= 198:
            entry_1 = past_entry
            
def engineScream():
    global enginescream
    
    enginescreams = "sounds\VO_BS_challange_02.wav.mp3", "sounds\VO_BS_challange_08.wav.mp3", "sounds\VO_BS_burning_w_03.wav.mp3", "sounds\VO_BS_attack_w_02.wav.mp3"
    rng = int(random(0, len(enginescreams)))
    enginescream = SoundFile(this, enginescreams[rng])
    enginescream.play()
    
def drawImages():
    global heat, intro, indThinking, item_left, item_up, item_right, item_down, guns_unlocked, magic_unlocked, car_unlocked, searching, entry_2
    
    #total_images = 32
    #l = total_images/4
    #w = total_images/5
    #v = -100
    
    #if heat < 150:
    #    img = handsome
    #if heat >= 150:
    #    img = evil
    #if heat >= 200:
    #    img = meltface
    #if intro == 1:
    #    img = thinkman
    #if intro == 2:
    #    img = laughing
    #if intro == 4:
    #    img = happyguy_gif
    #    happyguy_gif.loop()
    #if angry:
    #    img = hateful
    
    #image(img, wid/2-75, lng - 175, 150, 150)
    
    #if entry_2 == ">":
    #    searched_img1 = loadImage("cathedral.jpg")
    
    image(searched_img1, 0, 0, 300, 600)
    scale(-1, 1)
    image(searched_img1, -wid-1, 0, 300, 600)
    scale(-1, 1)

    #gifs
    
    #image(WORLD_gif, 20, 20, 200, 150)
    #scale(-1,1)
    #image(WORLD_gif, -(wid-20), 20, 200, 150)
    #scale(-1,1)
    
    image(EYE_gif, 600, 0, 300, 150)
    scale(-1,1)
    image(EYE_gif, -600, 0, 300, 150)
    scale(-1,1)
    
    #image(CAR_gif, (wid/2)-150, (lng/2)-150, 300, 300)
    
    textAlign(CENTER, CENTER)
    textFont(font2)
    textSize(26)
    fill(255, 0, 0)
    text("LEVEL " + str(playerlevel) + " " + str(playerclass), 0, 0, wid, 50)
    textFont(font)
    fill(0, 255, 0)

    image(SMOKE_gif, 0, 0, 400, 800)
    scale(-1, 1)
    image(SMOKE_gif, -wid, 0, 400, 800)
    scale(-1, 1)

    #conditional
        
    #if indThinking:
        #image(ANGELS_gif, 0, 0, wid, lng)
        #ANGELS_gif.loop()
        
    if heat >= 150:
        image(EYE2_gif, wid/2 -125, lng/2 -115, 250, 250)
        EYE2_gif.loop()
    if intro == 1:
        image(FISH_gif, 600, 150, wid/2, 450)
        FISH_gif.play()
        searching = True
    if intro == 2:
        FISH_gif.stop()
        FISH_gif.jump(0)
        image(HAPPYRUN_gif, wid/2 - 40, lng/2 - 80, 80, 160) 
        HAPPYRUN_gif.loop()
    if intro == 4:
        image(WOW_gif, 20, lng - 120, 100, 100)
        scale(-1,1)
        image(WOW_gif, -wid +20, lng - 120, 100, 100)
        scale(-1, 1)
        WOW_gif.loop()
    if intro == 6:
        mandatoryGambling()
    if intro == 7:
        gamblingAwards()
    #if intro == 14:
        #shopGuns()
    #if intro == 15:
        #gunsAfter()
        
    if item_up:
        if guns_unlocked:
            image(GUN_gif, 450, 200, wid - 350, lng - 200)
            scale(-1, 1)
            image(GUN_gif, -(wid-450), 200, wid-350, lng-200)
            scale(-1, 1)
        else:
            image(hand, 0, lng/2, wid/2, lng/2)
            scale(-1, 1)
            image(hand, -(wid), lng/2, wid/2, lng/2)
            scale(-1, 1)
            
        
    if item_right:
        if car_unlocked:
            image(driver, -350, lng/2 + lng/8, wid+350, lng/4+lng/8)
        else:
            image(hand, 0, lng/2, wid/2, lng/2)
            scale(-1, 1)
            image(hand, -(wid), lng/2, wid/2, lng/2)
            scale(-1, 1)
        
    if item_down:
        pass
        
    if item_left:
        if magic_unlocked:
            image(SPELL_gif, 0, 200, wid, lng-200)
        else:
            image(hand, 0, lng/2, wid/2, lng/2)
            scale(-1, 1)
            image(hand, -(wid), lng/2, wid/2, lng/2)
            scale(-1, 1)
            

            
    SMOKE_gif.loop()
    EYE_gif.loop()
    #WORLD_gif.loop()
    MOON_gif.loop()

    #for o in range(w):
    #    v = v + 100
    #    for i in range(l):
    #        pass
    #        image(img, wid/2 + v, i*100, 100, 100)
            
def mandatoryGambling():
    global user_input, gambling
    
    image(SLOTS_gif, 100, 150, 1000, 600)
    SLOTS_gif.loop()
    
    gambling = True
    
    fill(255, 0, 0)
    textAlign(CENTER)
    textFont(font2)
    text("SLOTS TIME >:)", 0, 0, wid, 600)
        
    textAlign(CENTER, CENTER)
    text(user_input, 0, 0, wid, lng)
        
    text("HOW MUCH WOULD YOU LIKE TO BET???", 0, lng-600, wid, lng)
    
def gamblingAwards():
    global gambling
    
    gambling = False
    image(MONEY_gif, 0, 0, wid, lng+400)
    image(MONEY3D_gif, wid/2-100, lng/2-100, 200, 200)
    MONEY_gif.loop()
    MONEY3D_gif.loop()
    
#def shopGuns():
    
#    image(ROTATINGGUN_gif, 0, 200, 600, 400)
#    scale(-1, 1)
#    image(ROTATINGGUN_gif, -wid, 200, 600, 400)
#    scale(-1, 1)
#    ROTATINGGUN_gif.play()
    
#    textAlign(CENTER)
#    textFont(font2)
#    textSize(64)
#    text("URGENT MARKETPLACE NOTIFICATION", 0, 0, wid, 600)
#    textAlign(CENTER, CENTER)
#    text(user_input, 0, 0, wid, lng)
        
#    text("DO YOU WANT TO BUY A GUN YES OR NO. ITS DANGEROUS TO BE HERE YOURE IN DANGER.", 0, lng-600, wid, lng)
    
#def gunsAfter():
#    global guns_unlocked, coins
#    guns_unlocked = True
#    if coins >= 0:
#        coins = 0 - (coins/2)
    
def awardCoins():
    global coins, points, heat
    rng = int(random(0, 10000000))
    coins = (coins + rng) * heat
    
    rng2 = int(random(0, 10000000))
    points = (points + rng2) * heat
    
def controllerCheck():
    pass
    
def levelUp():
    global playerlevel, playerclass, magic_unlocked, car_unlocked
    
    playerlevel += int(random(0,8))
    
    if playerlevel < 10:
        playerclass = "NOVICE"
    if playerlevel >= 10 and playerlevel < 50:
        playerclass = "TRAVELLER"
    if playerlevel >= 50 and playerlevel < 100:
        playerclass = "WIZARDS APPRENTICE"
    if playerlevel >= 100 and playerlevel < 500:
        playerclass = "WARLOCK CHIEFTAN"
        magic_unlocked = True
    if playerlevel >= 500:
        playerclass = "๑۞๑,¸¸,ø¤º°`°๑۩"
        car_unlocked = True
        
        
def shootPistols():
    global item_up, heat
    if item_up:
        if gunshoot.isPlaying() == False:
            gunshoot.play()
        heat = heat+2
        GUN_gif.loop()
        
def coolDown():
    global heat, light_value
    if heat >= 0:
        heat = heat - (light_value/10)
        
def castSpell():
    global item_left, casting_spell, heat
    if item_left:
        if spellsound.isPlaying() == False:
            spellsound.play()
        casting_spell = True
        heat = heat + 3
        SPELL_gif.loop()
        
def displayResults():
    global entry_2, searched_img1, searched_img2, urlindex, entry_1

    if entry_2 != ">":
        querystring = {"q_all":entry_2}
        results = pull_data(querystring)
        if urlindex <= 500 and len(results["data"]) != 0:
            while True:
                try:
                    urlstring = results["data"][urlindex]["images"][0]["link"]
                    print(urlstring)
                    if ".mp4" in urlstring:
                        urlindex += 1
                        displayResults()
                        return False
                    searched_img1 = loadImage(urlstring)
                    return False
                except:
                    urlindex = urlindex + 1
                    displayResults()
                    return False
        else:
            entry_1 = "no results."
            searched_img1 = loadImage("cathedral.jpg")
    if entry_2 == ">":
        searched_img1 = loadImage("cathedral.jpg")
        
    urlindex = 0
    
def pull_data(query):
    
    headers = {
    "Authorization": "Client-ID 9708d9936677782",
    "X-RapidAPI-Host": "imgur-apiv3.p.rapidapi.com",
    "X-RapidAPI-Key": "875e103689mshfb488577648a151p1588f9jsn4209710868ba"
    }
    
    request = urllib2.Request(url + "?" + urllib.urlencode(query), headers=headers)
    response = urllib2.urlopen(request)
        
    #print(response.read())
    return json.loads(response.read())

    
