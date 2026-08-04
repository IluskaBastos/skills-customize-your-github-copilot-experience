
# 📘 Atividade: Jogo da Forca

## 🎯 Objetivo

Desenvolver um jogo da Forca em Python usando manipulação de strings, estruturas de repeticao e condicionais.
Ao final, voce sera capaz de controlar o fluxo de um jogo simples com entradas do usuario e regras claras de vitoria e derrota.

## 📝 Tarefas

### 🛠️	Implementar a logica principal da forca

#### Descricao
Crie a mecanica central do jogo, incluindo escolha da palavra, exibicao do progresso e validacao dos palpites do jogador.

#### Requisitos
O programa concluido deve:

- Selecionar uma palavra aleatoria a partir de uma lista predefinida.
- Mostrar a palavra oculta no formato `_ _ _` e atualizar os acertos a cada rodada.
- Aceitar um palpite de uma letra por vez e ignorar entradas invalidas.
- Registrar letras ja tentadas para evitar repeticoes.


### 🛠️	Controlar fim de jogo e feedback ao jogador

#### Descricao
Implemente as regras de encerramento e apresente mensagens finais conforme o resultado da partida.

#### Requisitos
O programa concluido deve:

- Definir um numero maximo de tentativas incorretas e decrementa-lo quando necessario.
- Encerrar o jogo com mensagem de vitoria quando toda a palavra for descoberta.
- Encerrar o jogo com mensagem de derrota quando as tentativas acabarem, exibindo a palavra correta.
- Exibir, a cada rodada, o estado atual do jogo (palavra parcial e tentativas restantes).