from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Update
from telegram.ext import CallbackContext
import json
import threading
import time
import requests

TOKEN = ""
LEMBRETES_FILE = "lembretes.json"



# 📤 Função para enviar mensagem para o site via POST
def enviar_para_site(chat_id, mensagem):
    dados = {
        'chat_id': chat_id,
        'mensagem': mensagem
    }
    try:
        response = requests.post(URL_SITE, data=dados)
        if response.status_code == 200:
            print("✅ Mensagem enviada ao site com sucesso!")
        else:
            print(f"⚠️ Erro ao enviar para o site: {response.status_code} - {response.text}")
    except Exception as e:
        print("❌ Erro ao conectar com o site:", e)

# 📂 Carregar lembretes
def carregar_lembretes():
    try:
        with open(LEMBRETES_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# 💾 Salvar lembretes
def salvar_lembretes(lembretes):
    with open(LEMBRETES_FILE, "w") as f:
        json.dump(lembretes, f)

# ⏰ Agendar lembrete
def agendar_lembrete(chat_id, texto, segundos, context: CallbackContext):
    def esperar():
        time.sleep(segundos)
        context.bot.send_message(chat_id=chat_id, text=f"⏰ Lembrete: {texto}")
    threading.Thread(target=esperar).start()

# 💡 Comando /lembra
def lembra(update: Update, context: CallbackContext):
    try:
        partes = update.message.text.split(" em ")
        texto = partes[0].replace("/lembra ", "").strip()
        tempo = partes[1].strip()
        segundos = int(tempo.split()[0])

        lembrete = {"chat_id": update.effective_chat.id, "texto": texto, "tempo": segundos}
        lembretes = carregar_lembretes()
        lembretes.append(lembrete)
        salvar_lembretes(lembretes)

        agendar_lembrete(update.effective_chat.id, texto, segundos, context)
        update.message.reply_text(f"✅ Lembrete criado para '{texto}' em {segundos} segundos")

    except Exception as e:
        update.message.reply_text("❌ Formato inválido. Use: /lembra beber água em 60 segundos")
        print(e)

# 💰 Cotação
def cotacao(update: Update, context: CallbackContext):
    try:
        resposta = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL,BTC-BRL")
        dados = resposta.json()
        dolar = dados['USDBRL']['bid']
        bitcoin = dados['BTCBRL']['bid']
        update.message.reply_text(f"💵 Dólar: R${dolar}\n₿ Bitcoin: R${bitcoin}")
    except Exception as e:
        update.message.reply_text("Erro ao buscar cotação.")
        print(e)

# 🚀 Comando inicial
def start(update, context):
    update.message.reply_text("Olá! Eu sou seu bot no Discloud 😎\nUse /lembra ou /cotacao")

# 💬 Texto comum
def reply_text(update, context):
    if update.message and update.message.text:
        msg = update.message.text
        chat_id = update.message.chat.id
        chat_type = update.message.chat.type

        print(f"[{chat_type}] Mensagem recebida: {msg}")
        update.message.reply_text(f"Você disse: {msg}")

        # 🔁 Enviar para o site
        enviar_para_site(chat_id, msg)
    else:
        print("⚠️ Recebido update sem texto")

# ▶️ Main
def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("lembra", lembra))
    dp.add_handler(CommandHandler("cotacao", cotacao))
    dp.add_handler(MessageHandler(Filters.text, reply_text))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
