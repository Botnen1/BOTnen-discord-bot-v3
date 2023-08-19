from main import * 
import random as rnd
listehei = ["hello", "hallo", "hei", "halla", "yo", "hey", "hola", "hei på deg", "hallais"]


def get_response(message: str) -> str:
  p_message = message.lower()

  if p_message in listehei:
    return "Hei menneske"

  if p_message == "help me bot":
    return "'you want me to help you?\nhow aboyt maybe this time, you try using your brain for once?!?'"
