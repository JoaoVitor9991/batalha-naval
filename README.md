# batalha-naval
 
# Jogo de Batalha Naval

Este é um jogo de Batalha Naval desenvolvido em Python. O objetivo do jogo é localizar e afundar todos os navios no tabuleiro.

## Funcionalidades

- Criação de um tabuleiro 10x10.
- Posicionamento aleatório de navios no tabuleiro.
- Três tipos de orientação para os navios: horizontal, vertical e diagonal.
- Navios não podem tocar-se.
- Sistema de vidas e acertos consecutivos para ganhar vidas extras.
- Feedback ao jogador sobre acertos e tiros na água.

## Regras do Jogo

- O jogador tem um número inicial de 5 vidas.
- Cada tiro acertado em um navio adiciona 1 ponto aos acertos consecutivos.
- Ao atingir 3 acertos consecutivos, o jogador ganha uma vida extra.
- Se o jogador errar o tiro (acertar na água), ele perde uma vida e os acertos consecutivos são resetados.
- O jogo termina quando o jogador afunda todos os navios ou perde todas as vidas.

## Tipos de Navios

- Porta-aviões (P): Tamanho 5, Quantidade 1
- Cruzador (C): Tamanho 4, Quantidade 1
- Torpedeiro (T): Tamanho 3, Quantidade 2
- Rebocador (R): Tamanho 2, Quantidade 3

## Instruções para Jogar

1. Clone este repositório para sua máquina local:
    ```bash
   (https://github.com/JoaoVitor9991/batalha-naval)
    ```
2. Navegue até o diretório do jogo:
    ```bash
    cd game-naval
    ```
3. Siga as instruções na tela para jogar. Digite as coordenadas da linha e coluna para atirar.

## Estrutura do Código

- `criar_tabuleiro()`: Cria e retorna um tabuleiro vazio.
- `verificar_posicao()`: Verifica se uma posição é válida para posicionar um navio.
- `colocar_navio()`: Posiciona um navio no tabuleiro.
- `navios_nao_se_tocam()`: Verifica se os navios não se tocam.
- `posicionar_navios()`: Posiciona todos os navios no tabuleiro.
- `mostrar_tabuleiro()`: Mostra o estado atual do tabuleiro.
- `jogar()`: Função principal que executa o jogo.

## Melhorias Futuras

- Implementar uma interface gráfica para o jogo.
- Adicionar níveis de dificuldade.
- Permitir jogo multiplayer.
