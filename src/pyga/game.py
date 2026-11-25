import pygame  # type: ignore
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Jogo da Cobrinha")

clock = pygame.time.Clock()
running = True

# Cores
PRETO = (25, 28, 40)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
BRANCO = (255, 255, 255)

# Tamanho dos blocos
tamanho = 20

# Fonte
fonte = pygame.font.SysFont(None, 40)

def reiniciar():
    cobra = [(400, 300)]
    direcao = (tamanho, 0)
    comida = (
        random.randrange(0, 800, tamanho),
        random.randrange(0, 600, tamanho)
    )
    pontos = 0
    game_over = False
    return cobra, direcao, comida, pontos, game_over

cobra, direcao, comida, pontos, game_over = reiniciar()

contador = 0

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if not game_over:

                if event.key == pygame.K_UP and direcao != (0, tamanho):
                    direcao = (0, -tamanho)

                elif event.key == pygame.K_DOWN and direcao != (0, -tamanho):
                    direcao = (0, tamanho)

                elif event.key == pygame.K_LEFT and direcao != (tamanho, 0):
                    direcao = (-tamanho, 0)

                elif event.key == pygame.K_RIGHT and direcao != (-tamanho, 0):
                    direcao = (tamanho, 0)

            if event.key == pygame.K_SPACE and game_over:
                cobra, direcao, comida, pontos, game_over = reiniciar()
                contador = 0

    # Movimentação da cobrinha
    if not game_over:

        contador += 1

        if contador >= 6:
            contador = 0

            cabeca = (
                cobra[0][0] + direcao[0],
                cobra[0][1] + direcao[1]
            )

            cobra.insert(0, cabeca)

            # Verificar se comeu
            if cabeca == comida:
                pontos += 1

                while True:
                    comida = (
                        random.randrange(0, 800, tamanho),
                        random.randrange(0, 600, tamanho)
                    )

                    if comida not in cobra:
                        break
            else:
                cobra.pop()

            # Verificar colisão com a parede
            if (cabeca[0] < 0 or cabeca[0] >= 800 or
                cabeca[1] < 0 or cabeca[1] >= 600):
                game_over = True

            # Verificar colisão com o próprio corpo
            if cabeca in cobra[1:]:
                game_over = True

    # Desenhar fundo
    screen.fill(PRETO)

    # Desenhar comida
    pygame.draw.rect(
        screen, VERMELHO,
        (comida[0], comida[1], tamanho, tamanho)
    )

    # Desenhar cobrinha
    for parte in cobra:
        pygame.draw.rect(
            screen, VERDE,
            (parte[0], parte[1], tamanho, tamanho)
        )

    # Mostrar pontuação
    texto = fonte.render(f"Pontos: {pontos}", True, BRANCO)
    screen.blit(texto, (10, 10))

    # Tela de Game Over
    if game_over:
        mensagem = fonte.render("GAME OVER", True, VERMELHO)
        reiniciar_texto = fonte.render(
            "Aperte ESPACO para reiniciar", True, BRANCO
        )

        screen.blit(mensagem, (300, 250))
        screen.blit(reiniciar_texto, (190, 310))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()