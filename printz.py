
import pygame
import antz
import sys


if __name__ == '__main__':

  animate = False
  if len(sys.argv) == 4:
    grf = antz.graph(int(sys.argv[1]))
    colony = antz.colony(grf,int(sys.argv[2]))
    if sys.argv[3] == 'animate' or sys.argv[3] == '-A':
      animate = True
  elif len(sys.argv) == 3:
    grf = antz.graph(int(sys.argv[1]))
    colony = antz.colony(grf,int(sys.argv[2]))
  else:
    print("USAGE: python printz <number nodes> <number ants> [-A | animate ]")
    exit()

            

  pygame.init()

  background_colour = (27,27,27)
  circle_colour = (180,180,180)
  line_colour = (160,120,120)
  text_colour = (22,10,150)
  (width, height) = (1200, 900)

  screen = pygame.display.set_mode((width, height))

  pygame.display.set_caption('Ant Optimization Visualizer')
  screen.fill(background_colour)
  running = True
  Font= pygame.font.Font(pygame.font.get_default_font(),  15)
  FontB = pygame.font.Font(pygame.font.get_default_font(),  24)



  for idx,circ in enumerate(grf.coords):
    number = Font.render(str(idx),False,text_colour)
    pygame.draw.circle(screen,circle_colour,circ,20.0)
    screen.blit(number,circ - (10,10))

  pygame.display.flip()

  if not animate:
    iter = 0
    while running:

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
          iter+=1
          for _ in range(grf.size):
            colony.step()
          colony.update()
          colony.reset()
          screen.fill(background_colour)
          for i in range(grf.size):
            for j in range(i,grf.size):
              pygame.draw.line(screen, (255*grf.pheromones[i,j]%255,80,80), grf.coords[i], grf.coords[j], int(grf.pheromones[i,j]*15))     
          

          for idx,circ in enumerate(grf.coords):
            number = Font.render(str(idx),False,text_colour)
            pygame.draw.circle(screen,circle_colour,circ,20.0)
            screen.blit(number,circ - (10,10))   
          iterations = FontB.render(f"Iterations: {iter}",False,(230,255,255))
          screen.blit(iterations,(10,10))
          lennn = FontB.render(f"Minimum tour: {colony.tourlen:.2f}", False,(230,255,255))
          screen.blit(lennn,(10,50))
      
        pygame.display.flip()

  else:
    clock = pygame.time.Clock()
    iter = 0
    pause = 1
    while running:

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
          pause ^= 1
        
        
      if pause == 0 :
        for _ in range(grf.size):
          colony.step()
        colony.update()
        colony.reset()
        screen.fill(background_colour)
        for i in range(grf.size):
          for j in range(i,grf.size):
            pygame.draw.line(screen, (255*grf.pheromones[i,j]%255,80,80), grf.coords[i], grf.coords[j], int(grf.pheromones[i,j]*15))     
          

        for idx,circ in enumerate(grf.coords):
          number = Font.render(str(idx),False,text_colour)
          pygame.draw.circle(screen,circle_colour,circ,20.0)
          screen.blit(number,circ - (10,10))   

        iterations = FontB.render(f"Iterations: {iter}",False,(230,255,255))
        screen.blit(iterations,(10,10))
        lennn = FontB.render(f"Minimum tour: {colony.tourlen:.2f}", False,(230,255,255))
        screen.blit(lennn,(10,50))

        clock.tick(12)
        iter+=12
        pygame.display.flip()
        
    

        