# Cценарий игры

define config.mouse = {}

define config.mouse["default"] = [("gui/cursors/main32_f.png", 0, 0)]
define config.mouse["feather"] = [("gui/cursors/feather_m.png", 72, 72)]

define minigame_is_active = True

# Определение персонажей игры.
define player_name = ''
define author = Character('Земля. 2030 год', color="94ec4c")
define unnamed = Character('Я', color="#5b23c9")
define player = Character('[player_name]', color="#5b23c9")

define scientist = Character('Учёная', color="#1ffdc6")
define colleague = Character('Коллега', color="#7b74ff")
define assistant = Character('Ассистент', color="#fdc25b")

# Ребенок
define subject1 = Character('Подопытный 1', color="#d35e1d")
# Аня
define subject2 = Character('Подопытная 2', color="#d23d6d")
# Бабушка
define subject3 = Character('Подопытная 3', color="#db454b")
# Байкер
define biker = Character('Байкер', color="#084d99")
# Дамочка
define subject5 = Character('Подопытная 5', color="#f495e1")
# Профессор Галия
define professor = Character('Профессор', color="#00a9b2")

define act_count = 0
define success_tasks_count = 0

default max_laugh = 100
default min_laugh = 0

default current_laugh = 0


screen laughmeter:
    vbar:
        xsize 221
        ysize 771
        xalign 0.85
        yalign 0.3
        value AnimatedValue(value = current_laugh, range = max_laugh, delay = 1.0) 
        bottom_bar Frame("gui/bar/polnaya.png", 10, 10)
        top_bar Frame("gui/bar/pustaya.png", 10, 10)


screen minigame_timer:
    # Jump("minigame_end")
    timer 1 repeat True action If(time > 0 and current_laugh < 100, SetVariable("time", time - 1), [Hide('minigame_timer'), Jump("minigame_end")]) 
    text str(time) xalign 0.5 yalign 0.2 color '#f495e1' font 'font/ofont_ru_shadow.ttf' size 50


screen lauch_place:
    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "gui/proz_button.png"
        hover "gui/proz_button.png"
        action SetVariable("current_laugh", current_laugh + 10)
    

init:
    $ top2 = Position(xalign = 0.5, yalign = 0.6)
    $ left2 = Position(xalign = 0.1, yalign = 0.8)


# Игра начинается здесь:
label start:
    jump intro
    return


label intro:
    # введение

    $ default_mouse = "default"
    scene bg act1n1earth1
    pause 0.5
    author 'Однажды человечество поразил неизвестный науке вирус, лишающий возможности смеяться.'
    scene bg act1n1earth2
    with fade
    pause 0.5

    scene bg act1n2earth3
    author 'Каждый день заражённым людям приходилось начинать с антидепрессантов.'
    scene bg act1n2earth4
    pause 1.0

    scene bg act1n4mml
    with fade
    pause 0.5
    author 'Пока учёные не открыли экспериментальные лаборатории, направленные на изучение больных, под названием  MML lab. '
    extend 'MML lab - лаборатория Make Me Laugh.'
    $ act_count += 1 #act=1
    jump act1


label act1:
    # 1 акт

    $ default_mouse = "default"
    scene bg laba
    with fade
    unnamed 'В одной из таких лабораторий с сегодняшнего дня работаю и я.'
    $ player_name = renpy.input("Моё имя:", length = 12, allow = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ ').strip()

    if(player_name == ''):
        $ player_name = 'Новенький'
    
    show polina normal at top2
    scientist '[player_name], пора браться за работу!'
    menu: 
        scientist 'Ты готов приступить?'
        
        'Да': 
            scientist 'Коллега, ведите подопытного.'
            $ act_count += 1 #act=2
            jump minigame_intro


label minigame_intro:
    # mini-game intro

    $ default_mouse = "default"
    scene bg laba
    show subject1 sad at top2
    show dasha normal at left
    with dissolve
    colleague 'Подопытный номер 1, ' 
    extend 'его больше не радуют победы в БриверСтурсе.'
    
    show nastya feather:
        xalign 0.95 yalign 0.8
    assistant 'Удачи, салага.'
    hide nastya
    jump minigame1


label minigame1:
    $ minigame_is_active = True
    $ default_mouse = "feather"
    $ time = 15
    show screen minigame_timer
    show screen lauch_place
    show screen laughmeter
    $ current_laugh = 0
    while time > 0:
        player 'Что же делать?'
    jump minigame_end

    #while current_laugh < 100:
    #    pause 0.2
    #    $ current_laugh +=1



label minigame_end:
    if current_laugh < 100:
        jump minigame_fail
    else:
        jump minigame_success


label minigame_success:
    $ default_mouse = "default"
    $ success_tasks_count += 1
    hide screen laughmeter
    if act_count == 2:
        show subject1 laugh
        pause 3
        jump act2
    
    elif act_count == 3:
        show subject2 laugh at top2
        pause 3
        jump lunch
    elif act_count == 5:
        show subject3 laugh:
            xalign 0.5 yalign 0.8
        pause 3
        jump act5
    elif act_count == 6:
        show subject4 laugh:
            xalign 0.5 yalign 0.8
        pause 3
        jump act6
    elif act_count == 7:
        show subject5 laugh:
            xalign 0.5 yalign 0.8
        pause 3
        jump end


label minigame_fail:
    $ default_mouse = "default"
    pause 1
    hide screen laughmeter
    if act_count == 2:
        jump act2
    elif act_count == 3:
        jump lunch
    elif act_count == 5:
        jump act5
    elif act_count == 6:
        jump act6
    elif act_count == 7:
        jump end


label act2:
    # 2 акт

    $ default_mouse = "default"
    scene bg laba
    show polina normal at top2
    scientist 'Ведите следующего!'

    scene bg laba
    show subject2 sad at top2
    show dasha normal at left
    with dissolve
    
    colleague 'Подопытный номер 2, ' 
    extend 'не радовалась даже удачно сданной сессии.'
    subject2 'Я тут подопытный, смеюсь, когда вылезает гном, после нажимания на картинки.'

    show nastya tablet:
        xalign 0.95 yalign 0.8
    
    menu: 
        assistant 'Справишься с этой задачей?'
        
        'Да': 
            $ act_count += 1 #act=3
            jump minigame1


label lunch:
    # 3 акт
    # обед

    $ default_mouse = "default"
    if(player_name == ''):
        $ player_name = 'Новенький'
    
    
    scene bg lunchtime
    with fade
    pause 0.3
    colleague 'Ого, уже время обеда!'

    scene bg buffet
    with fade

    show polina lunch:
        xalign 0.45 yalign 0.8
    show dasha lunch:
        xalign 0.25 yalign 0.8
    show nastya lunch:
        xalign 0.85 yalign 0.8
    show professor lunch:
        xalign 0.65 yalign 0.8

    pause 3

    player 'Как дела?'
    scientist 'В выходной день приснилась работа'
    scientist 'Кто мне оплатит ночную смену?'

    player 'Как жизнь?'
    colleague 'Просторный офис, дружный коллектив, кондиционер и удобное кресло. Что может быть лучше?'
    colleague 'Ну, например, поспать дома.'
    
    player 'Как поживаешь?'
    assistant 'Не люблю вслух объявлять сумму своих доходов, людям становится неловко.'
    assistant 'Некоторые даже начинают протягивать мне монетки.'

    menu: 
        player 'Дать монетку ассистенту?'
        
        'Да': 
            assistant 'Ассистент убегает как крысюк'
            hide nastya
    
    player 'Как дела?'
    professor 'Говорят «кто не работает, тот не ест», но мне удалось перехитрить систему.'
    professor 'Я работаю и не ем.'
    scene bg lunchtime
    with fade
    pause 0.3
    colleague 'Ого, уже пора вернуться к работе!'
    $ act_count += 1 #act=4
    jump act4
    

label act4:
    # 4 акт

    $ default_mouse = "default"
    scene bg laba
    show polina normal at top2
    scientist 'Ведите следующего!'

    scene bg laba
    show subject3 sad:
        xalign 0.5 yalign 0.8
    show dasha normal at left
    with dissolve
    
    colleague 'Подопытный номер 3, ' 
    extend 'не смеялась... '
    extend 'ну очень давно не смеялась'
     
    show nastya bump1:
        xalign 0.95 yalign 0.8
    assistant '...'
    hide nastya
    
    menu: 
        colleague 'Поможешь бабушке?'
        
        'Да': 
            $ act_count += 1  #act=5
            jump minigame1


label act5:
    # 5 акт

    $ default_mouse = "default"
    scene bg laba
    show polina normal at top2
    scientist 'Ведите следующего!'

    scene bg laba
    show subject4 sad:
        xalign 0.5 yalign 0.8
    show dasha normal at left
    with dissolve
    
    colleague 'Подопытный номер 4, ' 
    extend 'перестал смеяться над байкерскими анекдотами.'

    show nastya bump1:
        xalign 0.95 yalign 0.8
    
    menu: 
        assistant 'Сможешь рассмешить байкера?'
        
        'Да': 
            $ act_count += 1 #act=6
            jump minigame1


label act6:
    # 6 акт

    $ default_mouse = "default"
    scene bg laba
    show polina normal at top2
    scientist 'Ведите следующего!'

    scene bg laba
    show subject5 sad:
        xalign 0.5 yalign 0.8
    show dasha normal at left
    with dissolve
    
    colleague 'Подопытный номер 5, ' 
    extend 'утверждает, что не умеет смеяться.'

    show nastya bump2:
        xalign 0.95 yalign 0.8

    menu: 
        assistant 'Справишься в этот раз?'
        
        'Да': 
            $ act_count += 1 #act=7
            jump minigame1


label end:
    $ default_mouse = "default"
    if success_tasks_count >= 3: 
        jump happy_end
    else:
        jump fail_end


label happy_end:

    $ default_mouse = "default"
    scene bg happyend
    pause 10
    return

label fail_end:

    $ default_mouse = "default"
    scene bg fail
    pause 10
    return