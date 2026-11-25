"""PyGA - um clone simples de Pong com modo contra a CPU e dois jogadores."""

from .game import Game


def main() -> None:
    """Inicia a até o jogador fechar a janela."""
    Game().run()


__all__ = ["Game", "main"]
