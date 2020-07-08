# jogo-genius
Este programa é uma simulação de um jogo de memória eletrônico. 

Eu não quis complicar muito o programa. O importante 
é que já da pra brincar e ir aprendendo um pouco mais
sobre Python e ncurses e que vocês entendam a lógica.

Observação: 

- Para rodar o programa use o Python3
- No Debian, instale o pacote "sox" através do apt-get 
para poder reproduzir os beeps através do "play"
- O play é um utilitário de linha de comando (shell). Para
testar o play direto do terminal copie e cole a linha abaixo: 

play --no-show-progress --null -t alsa --channels 1 synth.5 sine 1000

