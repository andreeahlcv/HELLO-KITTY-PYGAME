import pygame
import time
import random
pygame.font.init()

width, height= 900, 700
window=pygame.display.set_mode((width, height))
pygame.display.set_caption("HELLO KITTY GAME")

background=pygame.transform.scale(pygame.image.load("wallpaperflare.com_wallpaper.jpg"), (width, height))  #this will be the image imported
player_width=40
player_height=60
player_velocity=5
apple_width=10
apple_height=20
apple_velocity=2
font=pygame.font.SysFont("arial", 30)

def draw(player, elapsed_time, apples):
    window.blit(background, (0, 0))
    time_text=font.render(f"Time: {round(elapsed_time)}s", 1, "white")
    window.blit(time_text, (10, 10))

    pygame.draw.rect(window, "purple", player)

    for apple in apples:
        pygame.draw.rect(window, "yellow", apple)

    pygame.display.update()    #with this line we will update every new change by background

def main():
    run=True

    player=pygame.Rect(200, height - player_height, player_width, player_height)
    clock=pygame.time.Clock()
    start_time=time.time()
    elapsed_time=0

    apple_add_increment=2000  #this will be our "appels" we have to run from, witch will come one by one after 2000miliseconds
    apple_count=0

    apples=[]
    hit=False

    while run:
        apple_count += clock.tick(60)
        elapsed_time=time.time() - start_time  #will show us the number of seconds that elapsed from the beginning of the game
        
        if apple_count > apple_add_increment:
            for _ in range(2):
                apple_x = random.randint(0, width - apple_width)
                apple = pygame.Rect(apple_x, -apple_height, apple_width, apple_height)
                apples.append(apple)

            apple_add_increment = max(200, apple_add_increment - 50)
            apple_count=0

        for event in pygame.event.get():     
            if event.type==pygame.QUIT:      #this wil allow us to exit our game when press the 'X' button
                run=False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - player_velocity >=0:     #this condition will make us incapable of moving off the screen
            player.x -= player_velocity   #when the player will press the key to the left the x will move about 5 pixels
        if keys[pygame.K_RIGHT] and player.x + player_velocity + player_width <= width:
            player.x += player_velocity

        for apple in apples[:]:
            apple.y += apple_velocity
            if apple.y > height:
                apples.remove(apple)
            elif apple.y + apple.height >= player.y and apple.colliderect(player):
                apples.remove(apple)
                hit=True
                break

        if hit:
            lost_text=font.render("OOPS...HEHE, DON'T WORRY SWEATY. TRY AGAIN! :3", 1, "white")
            window.blit(lost_text, (width/2 - lost_text.get_width()/2, height/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(6000)
            break

        draw(player, elapsed_time, apples)

    pygame.quit()

if __name__ == "__main__":    #this function will make our code run
    main()