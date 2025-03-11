import os
import asyncio
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Token del bot
load_dotenv()
TOKEN = os.getenv("TOKEN")

tasks = [] # Lista para almacenar las tareas

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("¡Hola! Soy HenrrietaBot tu bot de tareas. Usa /agregar para añadir una tarea y /ver para verlas.")

async def agregar(update: Update, context: CallbackContext) -> None:
    tarea = " ".join(context.args)
    if tarea:
        tasks.append(tarea)
        await update.message.reply_text(f"✅ Tarea agregada: {tarea}")
    else:
        await update.message.reply_text("⚠️ Usa: /agregar [tarea]")

async def ver(update: Update, context: CallbackContext) -> None:
    if tasks:
        await update.message.reply_text("📌 Tareas pendientes:\n" + "\n".join(f"- {t}" for t in tasks))
    else:
        await update.message.reply_text("🎉 No tienes tareas pendientes.")

def main():
    
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("agregar", agregar))
    app.add_handler(CommandHandler("ver", ver))
    
    app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())