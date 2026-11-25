"""PyGA - um clone simples de Pong com modo contra a CPU e dois jogadores."""

from .game import run


def main() -> None:
    """Inicia a até o jogador fechar a janela."""
    run()


__all__ = [ "main"]
