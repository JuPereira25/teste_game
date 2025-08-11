import pgzrun
import random
from pgzero.rect import Rect

# --- Configurações da tela ---
WIDTH = 800
HEIGHT = 407
TITLE = "Cat Platformer"

# --- Constantes de física e gameplay ---
GRAVITY = 0.5
JUMP_POWER = 10
MOVE_SPEED = 3
CAT_SPEED = 2
CAT_SPAWN_INTERVAL = 2.0
GROUND_Y = HEIGHT - 60

# --- Posições fixas das moedas no cenário ---
coin_positions = [(250, GROUND_Y - 40), (400, GROUND_Y - 40), (550, GROUND_Y - 40)]

# --- Estado do jogo e variáveis globais ---
score = 0
hero_health = 3
game_state = "MENU"
sound_on = True

# --- Criação do herói (actor) e suas propriedades ---
hero = Actor("hero_idle", (100, GROUND_Y))
hero.vel_y = 0
hero.on_ground = True

# --- Listas para armazenar objetos da fase ---
coins = []
cats = []
cat_spawn_timer = 0.0

# --- Definição das áreas dos botões (x, y, largura, altura) ---
REPLAY_BTN = (WIDTH//2 -120, HEIGHT//2 +10, 240, 50)
MENU_BTN = (WIDTH//2 -120, HEIGHT//2 +80, 240, 50)

BTN_START = (WIDTH//2 -150, HEIGHT//2 -30, 300, 50)
BTN_SOUND = (WIDTH//2 -150, HEIGHT//2 +40, 300, 50)
BTN_EXIT = (WIDTH//2 -150, HEIGHT//2 +110, 300, 50)

# --- Função para detectar clique dentro de uma área (caixa) ---
def point_in_box(pos, box):
    x,y = pos
    bx,by,bw,bh = box
    return bx <= x <= bx+bw and by <= y <= by+bh


# --- Inicia uma nova partida ---
def start_game():
    global score, hero_health, coins, cats, cat_spawn_timer, game_state
    score, hero_health = 0, 3
    hero.pos = (100, GROUND_Y)
    hero.vel_y = 0
    hero.on_ground = True
    coins.clear()
    coins.extend([Actor("coin", pos) for pos in coin_positions])
    cats.clear()
    cat_spawn_timer = 0.0
    game_state = "GAME"
    if sound_on:
        music.play("background_music")
    else:
        music.stop()

# --- Volta para o menu principal ---
def back_to_menu():
    global game_state
    game_state = "MENU"
    music.stop()

# --- Liga ou desliga o som ---
def toggle_sound():
    global sound_on
    sound_on = not sound_on
    if sound_on:
        music.play("background_music")
    else:
        music.stop()

# --- Função que desenha tudo na tela ---
def draw():
    screen.clear()
    if game_state == "MENU":
        screen.fill("black")
        screen.draw.text("CAT PLATFORMER", center=(WIDTH//2, HEIGHT//2 -100), fontsize=56, color="white")
        screen.draw.filled_rect(Rect(*BTN_START), (50,150,50))
        screen.draw.text("Começar o Jogo", center=(BTN_START[0]+BTN_START[2]//2, BTN_START[1]+BTN_START[3]//2), fontsize=36, color="white")
        color_sound = (50,150,50) if sound_on else (150,50,50)
        screen.draw.filled_rect(Rect(*BTN_SOUND), color_sound)
        screen.draw.text(("Som: Ligado" if sound_on else "Som: Desligado"), center=(BTN_SOUND[0]+BTN_SOUND[2]//2, BTN_SOUND[1]+BTN_SOUND[3]//2), fontsize=36, color="white")
        screen.draw.filled_rect(Rect(*BTN_EXIT), (150,50,50))
        screen.draw.text("Sair", center=(BTN_EXIT[0]+BTN_EXIT[2]//2, BTN_EXIT[1]+BTN_EXIT[3]//2), fontsize=36, color="white")

    elif game_state == "GAME":
        try:
            screen.blit("background_1", (0,0))
        except:
            screen.fill("skyblue")
        for coin in coins:
            coin.draw()
        for cat in cats:
            cat.draw()
        hero.draw()
        screen.draw.text(f"Score: {score}", (10,10), color="white", fontsize=28)
        screen.draw.text(f"Vidas: {hero_health}", (10,40), color="white", fontsize=28)

    elif game_state == "VICTORY":
        screen.fill("black")
        screen.draw.text("VITÓRIA!", center=(WIDTH//2, HEIGHT//2 -60), fontsize=64, color="yellow")
        box = Rect(WIDTH//2 -220, HEIGHT//2 -120, 440, 260)
        screen.draw.filled_rect(box, (30,30,30))
        rx, ry, rw, rh = REPLAY_BTN
        mx, my, mw, mh = MENU_BTN
        screen.draw.filled_rect(Rect(rx,ry,rw,rh), "green")
        screen.draw.text("Jogar novamente", center=(rx+rw//2, ry+rh//2), fontsize=32, color="white")
        screen.draw.filled_rect(Rect(mx,my,mw,mh), "grey")
        screen.draw.text("Voltar ao menu", center=(mx+mw//2, my+mh//2), fontsize=32, color="white")

    elif game_state == "GAME_OVER":
        screen.fill("red")
        screen.draw.text("GAME OVER!", center=(WIDTH//2, HEIGHT//2 -20), fontsize=56, color="white")
        screen.draw.text("Pressione ENTER para voltar ao menu", center=(WIDTH//2, HEIGHT//2 +40), fontsize=28, color="white")


# --- Atualiza o estado do jogo a cada frame ---
def update(dt):
    global cat_spawn_timer, score, hero_health, game_state

    if game_state != "GAME":
        return

    if keyboard.right:
        hero.x += MOVE_SPEED
    if keyboard.left:
        hero.x -= MOVE_SPEED

    hero.x = max(0, min(WIDTH, hero.x))

    hero.vel_y += GRAVITY
    hero.y += hero.vel_y

    if hero.y >= GROUND_Y:
        hero.y = GROUND_Y
        hero.vel_y = 0
        hero.on_ground = True

    for coin in coins[:]:
        if hero.colliderect(coin):
            coins.remove(coin)
            score += 1
            if sound_on:
                sounds.coin.play()

    cat_spawn_timer += dt
    if cat_spawn_timer >= CAT_SPAWN_INTERVAL:
        cat_spawn_timer = 0
        new_cat = Actor("cat_walk_1")
        new_cat.pos = (WIDTH + 50, GROUND_Y)
        new_cat.vel_x = -CAT_SPEED
        cats.append(new_cat)

    for cat in cats[:]:
        cat.x += cat.vel_x
        if cat.right < 0:
            cats.remove(cat)
            continue

        if hero.colliderect(cat):
            if hero.vel_y > 0 and hero.bottom <= cat.top + 10:
                try: cats.remove(cat)
                except: pass
                hero.vel_y = -JUMP_POWER * 0.8
                score += 2
                if sound_on:
                    sounds.jump.play()
            else:
                hero_health -= 1
                hero.pos = (100, GROUND_Y)
                hero.vel_y = 0
                hero.on_ground = True
                cats.clear()
                cat_spawn_timer = 0
                if sound_on:
                    sounds.hurt.play()
                if hero_health <= 0:
                    game_state = "GAME_OVER"
                return

    if hero.x >= WIDTH - 10:
        game_state = "VICTORY"
        cats.clear()
        cat_spawn_timer = 0
        music.stop()

# --- Resposta a teclas pressionadas ---
def on_key_down(key):
    global game_state

    if game_state == "MENU" and key == keys.RETURN:
        start_game()
    elif game_state == "GAME":
        if key == keys.SPACE and hero.on_ground:
            hero.vel_y = -JUMP_POWER
            hero.on_ground = False
            if sound_on:
                sounds.jump.play()
    elif game_state == "VICTORY":
        if key in (keys.RETURN, keys.R):
            start_game()
        elif key == keys.M:
            back_to_menu()
    elif game_state == "GAME_OVER" and key == keys.RETURN:
        back_to_menu()

def on_mouse_down(pos):
    global game_state
    if game_state == "MENU":
        if point_in_box(pos, BTN_START):
            start_game()
        elif point_in_box(pos, BTN_SOUND):
            toggle_sound()
        elif point_in_box(pos, BTN_EXIT):
            exit()
    elif game_state == "VICTORY":
        if point_in_box(pos, REPLAY_BTN):
            start_game()
        elif point_in_box(pos, MENU_BTN):
            back_to_menu()

# --- Inicialização ---
coins = []
cats = []
pgzrun.go()
