import pygame
import sys
import random

# Inicialización de Pygame
pygame.init()

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Videojuego")

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AMARILLO = (255, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
estrellas = [(random.randint(0, ANCHO), random.randint(0, ALTO)) for _ in range(100)]
planetas = [(random.randint(0, ANCHO), random.randint(0, ALTO), random.randint(3, 10)) for _ in range(10)]

# Posición inicial de la nave
nave_pos_x = ANCHO // 2
nave_pos_y = ALTO // 2
VELOCIDAD_NAVE = 5
SALTO_NAVE = 10
en_salto = False
altura_salto = 0
reloj = pygame.time.Clock()

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Controles de movimiento
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and teclas[pygame.K_UP]:
        nave_pos_x -= VELOCIDAD_NAVE
        nave_pos_y -= VELOCIDAD_NAVE
    elif teclas[pygame.K_RIGHT] and teclas[pygame.K_DOWN]:
        nave_pos_x += VELOCIDAD_NAVE
        nave_pos_y += VELOCIDAD_NAVE
    elif teclas[pygame.K_LEFT] and teclas[pygame.K_DOWN]:
        nave_pos_x -= VELOCIDAD_NAVE
        nave_pos_y += VELOCIDAD_NAVE
    elif teclas[pygame.K_RIGHT] and teclas[pygame.K_UP]:
        nave_pos_x += VELOCIDAD_NAVE
        nave_pos_y -= VELOCIDAD_NAVE

    # Lógica del salto
    if teclas[pygame.K_SPACE] and not en_salto:
        en_salto = True
        altura_salto = SALTO_NAVE
    
    if en_salto:
        nave_pos_y -= altura_salto
        altura_salto -= 1
        if altura_salto < -SALTO_NAVE:
            en_salto = False
            nave_pos_y = min(ALTO - 50, nave_pos_y + SALTO_NAVE)

    # Dibujar la pantalla y la nave
    pantalla.fill(NEGRO)
    
    # Dibujar estrellas
    for estrella in estrellas:
        pygame.draw.circle(pantalla, BLANCO, estrella, 2)

    # Dibujar planetas lejanos
    for planeta in planetas:
        pygame.draw.circle(pantalla, AMARILLO, (planeta[0], planeta[1]), planeta[2])

    # Dibujar la nave
    pygame.draw.rect(pantalla, ROJO, (nave_pos_x, nave_pos_y, 20, 40))  # Cuerpo
    pygame.draw.rect(pantalla, ROJO, (nave_pos_x - 5, nave_pos_y + 30, 10, 10))  # Pierna izquierda
    pygame.draw.rect(pantalla, ROJO, (nave_pos_x + 15, nave_pos_y + 30, 10, 10))  # Pierna derecha
    pygame.draw.rect(pantalla, ROJO, (nave_pos_x - 5, nave_pos_y + 10, 10, 10))  # Brazo izquierdo
    pygame.draw.rect(pantalla, ROJO, (nave_pos_x + 15, nave_pos_y + 10, 10, 10))  # Brazo derecho
    pygame.draw.rect(pantalla, ROJO, (nave_pos_x + 5, nave_pos_y - 10, 10, 10))  # Cabeza

    # Dibujar detalles en negro dentro de la nave
    pygame.draw.line(pantalla, NEGRO, (nave_pos_x + 10, nave_pos_y), (nave_pos_x + 10, nave_pos_y + 40), 2)  # Línea vertical
    pygame.draw.line(pantalla, NEGRO, (nave_pos_x, nave_pos_y + 20), (nave_pos_x + 20, nave_pos_y + 20), 2)  # Línea horizontal

    # Actualizar la pantalla
    pygame.display.flip()
    reloj.tick(60)



