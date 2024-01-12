import flet as ft
from datetime import datetime


def main(pagina):
    texto = ft.Text('HashZap')  # criar o que você deseja
    pagina.add(texto)  # após isso, adicionar na página para aparecer

    nome_usuario = ft.TextField(label="Escreva seu nome")

    chat = ft.Column()


    # sempre que editar a página, quando ela já estiver concluída, precisa dar update dentro da função 
    def enviar_mensagem_tunel(informacoes):
        chat.controls.append(ft.Text(informacoes))
        pagina.update()


    pagina.pubsub.subscribe(enviar_mensagem_tunel)  # criar o túnel para permitir a troca de informações(mensagens)


    def enviar_mensagem(evento):
        hora_atual = datetime.now().strftime('%H:%M')
        texto_campo_mensagem = f"{hora_atual} {nome_usuario.value}: {campo_mensagem.value}"
        pagina.pubsub.send_all(texto_campo_mensagem)
        campo_mensagem.value = ""
        pagina.update()


    campo_mensagem = ft.TextField(label="Escreva sua mensagem aqui", on_submit=enviar_mensagem)  # on_submit = enviar a msg com o enter
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)


    def entrar_chat(evento):
        popup.open = False  # fechar o popup
        pagina.remove(botao_iniciar)  # remover o botão iniciar
        pagina.add(chat)  # adiciona o chat antes do campo de mensagem
        linha_mensagem = ft.Row(  
            [campo_mensagem, botao_enviar]  # ajusta o campo e botão lado a lado
        )
        print(nome_usuario.value)  # pegar informação que está no campo entrar_chat e mostrar no terminal
        pagina.add(linha_mensagem)
        texto = f"{nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(texto)
        pagina.update()


    popup = ft.AlertDialog(
        open=False, 
        modal=True,  # modal = modelo que aparece no meio da tela
        title=ft.Text('Bem vindo ao HashZap'),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_chat)]
        )


    def iniciar_chat(evento):
        pagina.dialog = popup  # o flet chama o "popup" de "dialog"
        popup.open = True
        pagina.update()


    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=iniciar_chat)
    pagina.add(botao_iniciar)

# ft.app(main)
ft.app(main, view=ft.WEB_BROWSER)  # ctrl + c = parar a aplicação