import os
import time
import Card_Generator
import evaluate_hand
Card_Generator.gen_dealer()
Card_Generator.gen_dealer()
Card_Generator.gen_dealer()
Card_Generator.gen_dealer()
Card_Generator.gen_dealer()


print("cards dealt..."f"{Card_Generator.gen_dealer()}")

print("evaluating hands..."+str(evaluate_hand.evaluate_hand(Card_Generator.used_cards)))
