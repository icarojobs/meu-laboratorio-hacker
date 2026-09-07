from collections import Counter

LADO = 5 # o tabuleiro tem 5 colunas por 5 linhas
GERACOES = 5 # quantas rodadas (gerações) vamos desenhar

# cada célula é um par (coluna, linha) - estas 5 formam o Glider na geração 0
vivas = {(1, 0), (2, 1), (0, 2), (1, 2), (2, 2)}

def vizinhas(coluna, linha):
    volta = []
    for dc in (-1, 0, 1):
        for dl in (-1, 0, 1):
            if (dc, dl) != (0,0): # (0,0) esria a própria célula: não conta como vizinha
                volta.append((coluna + dc, linha + dl)) # soma o deslocamento e guarda a vizinha
    return volta

def proxima(tabuleiro):
    conta = Counter() # vai virar "quantas vizinhas VIVAS cada casa tem"
    for coluna, linha in tabuleiro: # para cada célula viva
        for casa in vizinhas(coluna, linha):
            conta[casa] += 1 # ...ela da 1 ponto para cada vizinha

    nova = set() # o tabuleiro vai valer na próxima geração

    for casa, n in conta.items(): # olha só as casas que tem alguma vizinha viva
        nasce = (n == 3) # com exatamente 3 vizinhas a casa vive: nasce ou continua
        sobrevive = (n == 2 and casa in tabuleiro) # já estava viva e tem 2 vizinhas: continua
        if nasce or sobrevive: # o resto (0, 1, 4 ou mais vizinhas) morre
            nova.add(casa) # quem passou nas regras entra na próxima geração
    return nova # devolve o tabuleiro novinho

fotos = [] # a gente vai guardar uma "foto" do tabuleiro por geração

for g in range(GERACOES): # roda as 5 gerações, uma de cada vez
    fotos.append(vivas) # guarda a foto de como o tabuleiro está agora
    vivas = proxima(vivas) # e avança uma geração

titulos = [] # linha de cima do desenho: Geração 0, Geração 1...

for g in range(GERACOES):
    titulos.append(('Geração %d' % g).ljust(LADO * 2 - 1)) # alinha o título com o tabuleiro

print('   '.join(titulos)) # imprime os 5 titulos lado a lado

for linha in range(LADO): # desenha o tabuleiro de cima para baixo, linha a linha
    tiras = [] # uma tira de texto por geração
    for foto in fotos: # a MESMA linha, vista em cada uma das 5 fotos
        tiras.append(' '.join('#' if (coluna, linha) in foto else '.'
            for coluna in range(LADO))) # #=viva, .=vazia
    print('   '.join(tiras)) # imprime as 5 tiras lado a lado
