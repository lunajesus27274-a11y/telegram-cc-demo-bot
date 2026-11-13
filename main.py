import os
from telegram import Update
from telegram.ext import (
Application,
CommandHandler,
ContextTypes
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
await update.message.reply_text(
"🤖 Bienvenido a CC Demo Checker\n\n"
"Usa /check para probar la tarjeta de demostración.\n"
"Usa /help para ver los comandos."
)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
await update.message.reply_text(
"/start - Iniciar bot\n"
"/check - Probar tarjeta ficticia\n"
"/about - Información del bot"
)

async def check(update: Update, context: ContextTypes.DEFAULT_TYPE):
if not context.args:
await update.message.reply_text(
"Uso: /check 4242424242424242\n"
"Solo acepta esta tarjeta de prueba."
)
return

number = "".join(context.args)

if number == "4242424242424242":
await update.message.reply_text(
"✅ Tarjeta de demostración reconocida.\n"
"Esto no verifica tarjetas bancarias reales."
)
else:
await update.message.reply_text(
"❌ Solo se permite la tarjeta ficticia de demostración."
)

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
await update.message.reply_text(
"CC Demo Checker\n"
"Bot educativo de validación de pruebas."
)

def main():
token = os.getenv("BOT_TOKEN")
if not token:
raise RuntimeError("Falta configurar BOT_TOKEN")

app = Application.builder().token(token).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("check", check))
app.add_handler(CommandHandler("about", about))

app.run_polling()

if __name__ == "__main__":
main()
