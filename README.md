# ALFABETIZAÇÃO LITERÁRIA 1.0

---

## DESCRIÇÃO 

Esta é a versão 1.0 dum aplicativo de alfabetização literária que estou a desenvolver para meus irmãos mais novos em paralelo a minhas aulas de POO.
Os personagens aqui contidos são principalmente das obras de J.R.R. Tolkien, mas há também dos Limeriques (Edward Lear), Alice no País das Maravilhas e Além do Espelho (L. Caroll), O Mágico de Oz (F. Baum), etc. Todas bem conhecidas por meus irmãos. 

---

## EXECUÇÃO 

1 - Instale a mais recente versão do Python.

2 - Abra o prompt de comando com "Windows + R" e digite "cmd".

3 - No cmd, digite "cd CAMINHO_DIRETÓRIO", substituindo "CAMINHO_DIRETÓRIO" pelo endereço da pasta "Alfabetizacao_Literaria_1.0".

4 - Digite "py requerimentos.py", para que as bibliotecas necessárias sejam instaladas em sua máquina.

5 - Por fim, digite "py main.py" e se divirta!

---

## CASO DE USO:
- Atores: Jogador
- Fluxo principal:
  1. O sistema sorteia um personagem.
  2. O jogador escolhe uma sílaba.
  3. O sistema verifica se a sílaba está correta.
  4. Em caso de acerto, entra na fase de digitação.
  5. O jogador deve digitar a sílaba correta. Nada ocorre até que ela seja acertada.
  6. Após digitar a sílaba correta, a pontuação interna do jogo aumenta.
  7. O incremento da pontuação interna do jogo incrementa a pontuação global jogador.
  7. O retrato do personagem evolui (3, 6 e 10 pontos internos), conforme o número de acertos do jogador.

- Fluxo alternativo:
  - O jogador erra a sílaba → sistema reinicia a tentativa.

---

## OBSERVAÇÕES 

  1. A mudança de música a cada personagem é proposital, evitando a monotonia para a criança que joga.

  2.  Erros na escolha da sílaba são desfeitos após 5 segundos. Não há correção automatizada para o modo de digitação.

  3.  Não foi adicionado, no diagrama UML do projeto, uma representação detalhada da classe ParticleEffect e das classes a ela associadas, pois seria extremamente difícil e complexo. O PyIgnite é uma biblioteca externa complicada e antiga, e já foi dispendido muito tempo para convertê-la ao Python 3. Infelizmente, não achei outra solução para a implementação das partículas que necessitava.

---

## PARADIGMAS DE OO

Herança; Composição; Associação; Polimorfismo; Encapsulamento.

---

## ROADMAP V.2.0

❌ Implementar uma outra instância de jogo, aonde os pontos minerados pela criança poderão ser gastos, desbloqueando permanentemente fundos e retratos.

❌ Implementar leitura em voz das sílabas selecionadas corretamente (em verde) na 1ª fase, para reforçar a associação entre grafia e som.

❌ Implementar leitura em voz do nome completo do personagem no início da fase e novamente após o acerto da palavra.

❌ Implementar leitura do nome incorreto formado após a seleção de uma sílaba errada (em azul), reforçando a consequência do erro.

❌ Colocar fala guiada para montagem da sílaba, com a estrutura: "letra com vogal faz...". Após acerto, pronunciar: "letra com vogal faz... + nome da palavra".

❌ Adicionar botão de som ao lado do nome da palavra para o jogador ouvir a pronúncia correta, enquanto as sílabas piscam em vermelho.

❌ Fazer a sílaba correspondente piscar em vermelho enquanto o nome inteiro é pronunciado, para facilitar a identificação visual do som.

❌ Antes de selecionar a sílaba, o jogo deve dizer a sílaba faltante em voz alta e o jogador deve adivinhar qual vogal ela possui, promovendo escuta ativa.


❌ Criar um modo de jogo simplificado para ensinar sílabas isoladas, voltado ao público iniciante.

❌ Criar um modo de jogo para ensino de acentuação, focando nas relações entre acentos gráficos e sons (ex: á, ê, ó).

❌ Adicionar ao menos uma sílaba com a mesma vogal da correta em cada conjunto de personagem, aumentando a exigência de atenção auditiva.

❌ Implementar sistema de recompensas por pontos, com desbloqueio de novas artes visuais para os tazos (cada um com efeito visual único).

❌ Definir que o preço de um boneto novo será 5 créditos, mantendo padrão claro de progressão.

❌ Implementar perda de pontos em caso de erro, incentivando cuidado nas respostas e criando desafio equilibrado.

❌ Adicionar mais personagens e novas combinações de sílabas para ampliar a variedade e replay do jogo.

❌ Adicionar mais músicas ao jogo para enriquecer a experiência sonora e dar identidade única a cada fase ou personagem.

---