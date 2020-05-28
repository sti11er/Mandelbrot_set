import pygame

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption('множество Мандельброта')
done = False

for x in range(600):
  for y in range(600):
    i, j = (x - 300) / 150, (y - 300) / 150 #вещественная и мнимая части числа
    c = (i + j*((-1)**.5))

    in_mandelbrot = True
    z = 0
    for i in range(1000):
      z = z**2 + c
      if abs(z) >= 2:
        in_mandelbrot = False
        break

    if in_mandelbrot:
      pygame.draw.line(win, (255,255,255), (x, y), (x + 1, y + 1), 1)

while not done:
  pygame.time.delay(100)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True

  #x
  pygame.draw.line(win, (255,255,255), (0, 300),(600, 300), 1)
  #y
  pygame.draw.line(win, (255,255,255), (300, 0),(300, 600), 1)

  pygame.display.update()
  pygame.time.delay(33)#задержка

pygame.quit()
