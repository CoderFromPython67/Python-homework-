import pygame  
  
pygame.init()  
screen = pygame.display.set_mode((400, 300))  
screen.fill((255,255,255))
done = False 
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480



  
while not done:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  
    pygame.draw.rect(screen, (0, 125, 255), pygame.Rect(30, 30, 60, 60))  
    text = pygame.font.Font(None, 36).render('Rectangle', True, pygame.Color(0,0,0))
    text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110))
  
    pygame.display.flip()  

