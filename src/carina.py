from browser import document, html
UNIVERSO= "assets/universo.jpg"
CARINA= "assets/carina.png"
CARINA_STYLE= dict(position="absolute", left=10,top=10)
posicao_carina=dict (left=10, top=10)
def main():
    global posicao_carina
    universo= html.IMG(src=UNIVERSO)
    document ["pydev"] <= universo
    carina= html.IMG(src=CARINA, style=CARINA_STYLE)
    document ["pydev"] <= carina
    def anda_carina (evento):
        x,y=evento.x,evento.y

        global posicao_carina
        left,top=posicao_carina["left"],posicao_carina["top"]
        left=x
        top=y
        posicao_carina= dict (left=left, top=top)
        novo_estilo=dict(position="absolute", left=100,top=100)
        novo_estilo.update(posicao_carina)
        carina.style=novo_estilo
    universo.onclick=anda_carina
