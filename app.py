from telegram import bot 
from decouple import config
from flask import Flask,request

TOKEN= config("TOKEN")
bot = bot.Bot(TOKEN)
chat_id=config("CHAT_ID")
app = Flask(__name__)
@app.route(f'/api/{TOKEN}',methods=["POST"])
def send():
  data = request.get_json()
  title = data["post"]["post_title"]
  post = data["post"]["post_content"]
  link = data["post_permalink"]
  text=f"<b>{title}</b>\n{post}\n{link}"
  bot.send_message(chat_id,text,parse_mode="HTML")
  return "1" 