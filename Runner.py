import pygame
import random

pygame.init()

display_width = 800
display_height = 600

pygame.display.set_caption('Runner Simulator')   # Game name

icon = pygame.image.load('esche.png')
pygame.display.set_icon(icon)

class Object:
    def __init__(self, x, y, width, image, speed):
        self.x = x
        self.y = y
        self.width = width
        self.image = image
        self.speed = speed
    def move(self):
        if self.x >= - self.width:
            display.blit(self.image, (self.x, self.y))
            self.x -= 4
            return True
        else:
            return False
    def return_self(self, radius, y, width, image):
        self.x = radius
        self.y = y
        self.width = width
        self.image = image
        display.blit(self.image, (self.x, self.y))

class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.inactive_clr = (71, 31, 131)
        self.active_clr = (98, 33, 196)

    def draw(self, x, y, messege, action=None, font_size=30):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(display, self.active_clr, (x, y, self.width, self.height))

            if click[0] == 1 and action is not None:
                clck_snd = pygame.mixer.Sound('clicksound.mp3')
                pygame.mixer.Sound.play(clck_snd)
                pygame.time.delay(300)
                if action() is not None:
                    if action == quit:
                        pygame.quit()
                        quit()
                    else:
                        action()
        else:
            pygame.draw.rect(display, self.inactive_clr, (x, y, self.width, self.height))
        print_text(messege, x=x + 10, y=y + 10, font_size=font_size)

user_width = 48
user_height = 70 # жирнота героя
user_x = display_width // 3  # Расположение героя на экране по X
user_y = display_height - user_height - 60 # Тоже самое по Y

cactus_width = 40
cactus_height = 50
cactus_x = display_width + 10
cactus_y = display_height - cactus_height - 100

clock = pygame.time.Clock()   # Пугеймовский счетчик времени

display = pygame.display.set_mode((display_width, display_height))   # Определение разрешения

pygame.mixer.music.load('forrun.mp3') # Music
pygame.mixer.music.set_volume(0.2)
jump_sound = pygame.mixer.Sound('jumpstart.mp3')
fall_sound = pygame.mixer.Sound('padenie.mp3')
end_sound = pygame.mixer.Sound('dead.mp3')
jump_hero_voice = pygame.mixer.Sound
loss_sound = pygame.mixer.Sound('game_lost.mp3')
hit_sound = pygame.mixer.Sound('hit_voice.mp3')
heart_plus_sound = pygame.mixer.Sound('est.mp3')
hit_sound.set_volume(0.2)
heart_plus_sound.set_volume(0.1)
end_sound.set_volume(0.5)
zeus_thunder_sound = pygame.mixer.Sound("Thundergod.mp3")
zeus_thunder_sound.set_volume(0.5)
havenotmana = pygame.mixer.Sound('havenotmana.mp3')
havenotmana.set_volume(0.2)
hahahaha = pygame.mixer.Sound('bogdal.mp3')
hahahaha.set_volume(0.2)
zeus_attack_shield = pygame.mixer.Sound('zeus_attack_shield.mp3')
zeus_attack_shield.set_volume(0.2)

cactus_img = [pygame.image.load('cactus0.xcf'), pygame.image.load('cactus1.png'), pygame.image.load('cactus2.png')]   # Массив картинок препятствий
cactus_options = [82, 382, 51, 385, 70, 441]
cloud_options = [127, 420, 144, 407, 358, 385]
zeus_options = [548, 0]

                # Координаты спавна препятствий для х и у для каждого кактуса как 1 и 2 и 3 соответственно [x1, y1, x2, y2, x3, y3] х определяется шириной объекта, у = display_hight - 100 - cactus_height.
                # Хитбокс определяется по размеру картинки и в функции столкновения с барьером ниже

stone_img = [pygame.image.load('stone0.xcf'), pygame.image.load('stone1.xcf')]
cloud_img = [pygame.image.load('cloud0.xcf'), pygame.image.load('cloud1.xcf'), pygame.image.load('cloud2.xcf')]

jump_img = [pygame.image.load('herojump.png'), pygame.image.load('herojump.png'), pygame.image.load('herojump.png'), pygame.image.load('herojump.png')]   # Animation of jump
jump_dfnc_img = [pygame.image.load('herojump dfnc.xcf'), pygame.image.load('herojump dfnc.xcf'), pygame.image.load('herojump dfnc.xcf'), pygame.image.load('herojump dfnc.xcf')]
hero_thundered = [pygame.image.load('herothundered.xcf'), pygame.image.load('herothundered.xcf'), pygame.image.load('herothundered.xcf'), pygame.image.load('herothundered.xcf')]
hero_dfnc_img = [pygame.image.load('heromoving0 dfnc.xcf'), pygame.image.load('heromoving2 dfnc.xcf'), pygame.image.load('heromoving1 dfnc.xcf'), pygame.image.load('heromoving2 dfnc.xcf')]
hero_img = [pygame.image.load('heromoving0.png'), pygame.image.load('heromoving2.png'), pygame.image.load('heromoving1.png'), pygame.image.load('heromoving2.png')] # Массив с анимацией героя

zeus_img = [pygame.image.load('zeusFly.xcf'), pygame.image.load('zeusattack1.xcf')]


health_img = pygame.image.load('hp.png')
health_img = pygame.transform.scale(health_img, (50, 50))
meat_img = pygame.image.load('healka.xcf')
meat_img = pygame.transform.scale(meat_img, (50, 50))
img_counter = 0    # Счетчик чтоб герой делал анимацию
health = 2
zeus_img_counter = 0

defense_stance = False

make_thunder = False
make_jump = False
jump_counter = 30
scores = 0
max_scores = 0

max_above = 0

def show_menu():

    menu_bckgr = pygame.image.load('menu.jpg')

    start_button = Button(255, 70)
    quit_button = Button(120, 70)

    show = True

    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.blit(menu_bckgr, (0, 0))
        start_button.draw(270, 200, 'START GAME', start_game, 35)
        quit_button.draw(340, 300, 'QUIT', quit, 35)
        pygame.display.update()
        clock.tick(60)

def start_game():
    # Функция начинающая игру, создана отдельно чтобы активировалась как action для кнопки
    global scores, make_jump, jump_counter, user_y, health
    health = 2
    scores = 0
    while game_cycle():
        health = 2
        scores = 0
        make_jump = False
        jump_counter = 30
        user_y = display_height - user_height - 60

def game_cycle():
    'Основной цикл игры'
    global make_jump, make_thunder, defense_stance
    pygame.mixer.music.play(-1)
    run = True
    zeus = Object(random.randrange(4000, 6000), 0, 550, zeus_img[0], 1)
    cactus_arr = []
    create_cactus_arr(cactus_arr)
    heart = Object(display_width, 280, 50, meat_img, 4)
    ground = pygame.image.load('ground.png')
    stone, cloud = open_random_object()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        check_collision(cactus_arr)
        if keys[pygame.K_w]:
            defense_stance = True
        else:
            defense_stance = False
        if keys[pygame.K_SPACE]:
            make_jump = True
        if make_jump:
            jump()
        if keys[pygame.K_ESCAPE]:
            pause()
        count_scores(cactus_arr)
        display.blit(ground, (0, 0))
        print_text('Press Space to jump', 520, 550)
        print_text('Score: ' + str(scores), 600, 10)

        draw_array(cactus_arr)
        draw_zeus(zeus)
        draw_hero()
        move_objects(stone, cloud)
        if check_collision(cactus_arr):
            pygame.mixer.Sound.play(end_sound)
            pygame.mixer.music.stop()
            run = False
        hearts_plus(heart)
        heart.move()
        show_health()
        pygame.display.update()
        clock.tick(60)
    return game_over()

def draw_zeus(zeus):
    global img_counter, health, make_thunder
    zeus.move()
    zeus_img_counter = 60
    make_thunder = False
    if health == 1:
        if zeus.x + (zeus_options[0] // 2) <= user_x + (user_width // 2) <= zeus.x + (zeus_options[0] // 2) + 3:
            pygame.mixer.Sound.play(havenotmana)
    else:
        if zeus.x + (zeus_options[0] // 2) <= user_x + (user_width // 2) <= zeus.x + (zeus_options[0] // 2) + 3 and not defense_stance:
            pygame.mixer.Sound.play(zeus_thunder_sound)
            health = 1
            pygame.mixer.Sound.play(hahahaha)
        if zeus.x + (zeus.width // 2) in range(user_x - 10, user_x+user_width + 10):
            make_thunder = True
            display.blit(zeus_img[zeus_img_counter // 60], (zeus.x, 0))
        else:
            make_thunder = False
    if user_x - display_width >= zeus.x:
        zeus.return_self(random.randrange(5000, 15000), zeus_options[1], zeus.width, zeus_img[0])
    if zeus.x + (zeus_options[0] // 2) <= user_x + (user_width // 2) <= zeus.x + (zeus_options[0] // 2) + 3 and defense_stance:
        pygame.mixer.Sound.play(zeus_thunder_sound)
        pygame.mixer.Sound.play(zeus_attack_shield)

def jump():
    'Прыжок героя'
    global user_y, jump_counter, make_jump
    if jump_counter >= -30:
        if jump_counter == 30:
            pygame.mixer.Sound.play(jump_sound)
        if jump_counter == -30:
            pygame.mixer.Sound.play(fall_sound)
        user_y -= jump_counter / 2.5     # Height of hero jump
        jump_counter -= 1
    else:
        jump_counter = 30
        make_jump = False

def create_cactus_arr(array):
    "первичный spawn препятствий"
    choice = random.randrange(0, 3)
    img = cactus_img[choice]
    width = cactus_options[choice * 2]
    height = cactus_options[choice * 2 + 1] + 50
    array.append(Object(display_width + 100, height, width, img, 4))

    choice = random.randrange(0, 3)
    img = cactus_img[choice]
    width = cactus_options[choice * 2]
    height = cactus_options[choice * 2 + 1] + 50
    array.append(Object(display_width + 300, height, width, img, 4))

    choice = random.randrange(0, 3)
    img = cactus_img[choice]
    width = cactus_options[choice * 2]
    height = cactus_options[choice * 2 + 1] + 50
    array.append(Object(display_width + 600, height, width, img, 4))

def find_radius(array):
    "Определение расстояния между препятствиями"
    maximum = max(array[0].x, array[1].x, array [2].x)

    if maximum < display_width:
        radius = display_width
        if radius - maximum < 50:
            radius += 200  #Расстоние далеко
    else:
        radius = maximum

    choice = random.randrange(0, 5)
    if choice == 0:
        radius += random.randrange(35, 50) # Расстояние между кактусами когда они близко
    else:
        radius += random.randrange(500, 550)

    return radius

def draw_array(array):
    'Создание препятствий'
    for cactus in array:
        check = cactus.move()
        if not check:
            object_return(array, cactus)

def object_return(objects, obj):
    # Функция возвращающая препятствие за пределы экрана после того как оно скроется за экраном
    radius = find_radius(objects)
    choice = random.randrange(0, 3)
    img = cactus_img[choice]
    width = cactus_options[choice * 2]
    height = cactus_options[choice * 2 + 1] + 50
    obj.return_self(radius, height, width, img)

def open_random_object(): # Довести до ума
    'Создание фауны, рандомные штуки на земле и небе'
    choice = random.randrange(0, 2)
    img_of_stone = stone_img[choice]

    choice = random.randrange(0, 2)
    img_of_cloud = cloud_img[choice]

    stone = Object(display_width, display_height - 100, 15, img_of_stone, 4)
    cloud = Object(display_width, 80, 46, img_of_cloud, 2)
    return stone, cloud

def move_objects(stone, cloud): # Довести до ума
    "Передвижение рандомных штук на земле и небе"
    check = stone.move()
    if not check:
        choice = random.randrange(0, 2)
        img_of_stone = stone_img[choice]
        stone.return_self(display_width, random.randrange(510, 590), stone.width, img_of_stone)
    check = cloud.move()
    if not check:
        choice = random.randrange(0, 3)
        img_of_cloud = cloud_img[choice]
        width = cloud_options[choice * 2]
        cloud.return_self(display_width + 400, random.randrange(-10, 100), width, img_of_cloud)

def draw_hero():
    'Анимация передвижения героя'
    global img_counter
    if img_counter == 44:
        img_counter = 0
    if make_jump and not defense_stance:
        display.blit(jump_img[img_counter // 11], (user_x, user_y))
        if make_thunder and not defense_stance:
            display.blit(hero_thundered[img_counter // 11], (user_x, user_y))
    if not make_jump and not defense_stance:
        display.blit(hero_img[img_counter // 11], (user_x, user_y))
        if make_thunder and not defense_stance:
            display.blit(hero_thundered[img_counter // 11], (user_x, user_y))
    if make_jump and defense_stance:
            display.blit(jump_dfnc_img[img_counter // 11], (user_x, user_y))
    if not make_jump and defense_stance:
            display.blit(hero_dfnc_img[img_counter // 11], (user_x, user_y))
    img_counter += 1

def print_text(message, x, y, font_color = (0, 0, 0), font_type='GameFont.otf', font_size = 30):
    'Это параметры текста выводимого на игровой экран'
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x, y))

def pause():
    "F9"

    paused = True

    pygame.mixer.music.pause()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        print_text('Game Paused. Press enter to continue.', 160, 300)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RETURN]:
            paused = False
        pygame.display.update()
        clock.tick(15)
    pygame.mixer.music.unpause()

def check_collision(barriers): # Механизм работы столкновения, условия для разных препятствий
    for barrier in barriers:
        if barrier.y == 441:           # Little barrier
            if not make_jump:  # условия для смол барьера при просто беге
                if barrier.x <= user_x + user_width - 10 <= barrier.x + barrier.width:
                    if check_health():
                        object_return(barriers, barrier)
                        return False
                    else:
                        return True
            elif jump_counter > 0: # Проверка во время прыжка
                if user_y + user_height >= barrier.y:
                    if barrier.x <= user_x + user_width - 10 <= barrier.x + barrier.width:
                        if check_health():
                            object_return(barriers, barrier)
                            return False
                        else:
                            return True
            elif user_y + user_height - 5 >= barrier.y:  # Условия ударения пятки с правым верхним краем препятствия ( Потом дорабатывается учитывая спрайт herojump) для смол барьера
                if barrier.x <= user_x + 5 <= barrier.x + barrier.width:
                    if check_health():
                        object_return(barriers, barrier)
                        return False
                    else:
                        return True
            else:
                if user_y + user_height - 10 >= barrier.y: # условие для сМол барьера при повышении высоты при прыжке
                    if barrier.x <= user_x <= barrier.x + barrier.width:
                        if check_health():
                            object_return(barriers, barrier)
                            return False
                        else:
                            return True
        else:
            if not make_jump: # Условия при просто беге
                if barrier.x <= user_x + user_width - 15 <= barrier.x + barrier.width:
                    if check_health():
                        object_return(barriers, barrier)
                        return False
                    else:
                        return True
            elif jump_counter >= 10: # Условия при поднятии наверх при прыжке
                if user_y + user_height -5 >= barrier.y:
                    if barrier.x <= user_x + user_width - 15 <= barrier.x + barrier.width:
                        if check_health():
                            object_return(barriers, barrier)
                            return False
                        else:
                            return True
            elif jump_counter <= -1: # Условия при снижении высоты при прыжке
                if user_y + user_height - 5 >= barrier.y:
                    if barrier.x <= user_x + user_width - 37 <= barrier.x + barrier.width:
                        if check_health():
                            object_return(barriers, barrier)
                            return False
                        else:
                            return True
                else:
                    if user_y + user_height - 5 >= barrier.y: # Условия ударения пятки с правым верхним краем препятствия ( Потом дорабатывается учитывая спрайт herojump)
                        if barrier.x <= user_x + 5 <= barrier.x + barrier.width:
                            if check_health():
                                object_return(barriers, barrier)
                                return False
                            else:
                                return True
    return False

def count_scores(barriers): # Подсчет для набивания счета
    global scores, max_above
    above_cactus = 0

    if -20 <= jump_counter <= 25:
        for barrier in barriers:
            if user_y + user_height - 5 <= barrier.y:
                if barrier.x <= user_x <= barrier.x + barrier.width:
                    above_cactus += 1
                elif barrier.x <= user_x + user_width <= barrier.x + barrier.width:
                    above_cactus += 1

        max_above = max(max_above, above_cactus)
    else:
        if jump_counter == -30:
            scores += max_above
            max_above = 0

def game_over():
    global scores, max_scores
    if scores > max_scores:
        max_scores = scores
    stopped = True
    while stopped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        print_text('YOY DIED. Press enter to restart or escape to exit.', 50, 250)
        print_text('Max scores: ' + str(max_scores), 300, 350)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            return False
        if keys[pygame.K_RETURN]:
            return True

        pygame.display.update()
        clock.tick(15)

def check_health():
    global health
    health -= 1
    if health == 0:
        return False
    else:
        pygame.mixer.Sound.play(hit_sound)
        pygame.mixer.Sound(hit_sound)
        return True

def hearts_plus(heart):   # Условия для исцеления от подбора хилки + перемещение хилки
    global health, user_y, user_x, user_width, user_height

    y_random = random.randrange(275, 350)

    if user_x <= heart.x + heart.width <= user_x + user_width or user_x <= heart.x <= user_x + user_width: # Условия хавания хилки
        if user_y <= heart.y <= user_y + user_height or user_y <= heart.y + 50 <= user_y + user_height:
            pygame.mixer.Sound.play(heart_plus_sound)
            if health < 5:
                health += 1
            radius = display_width + random.randrange(1500, 4000)
            heart.return_self(radius, y_random, heart.width, meat_img)
    else:
        if user_x - 300 > heart.x:
            radius = display_width + random.randrange(1000, 4000)
            heart.return_self(radius, y_random, heart.width, meat_img)

def show_health(): # Отображение хп
    global health
    show = 0
    x = 20
    while show != health:
        display.blit(health_img, (x, 20))
        x += 50
        show += 1

show_menu()
pygame.quit()
quit()