import os
import time
import Card_Generator
import evaluate_hand

num_players = 0
player_names = []
while num_players < 2 or num_players > 6:
    try:
        num_players = int(input("Enter number of players (2-6): "))
    except ValueError:
        print("Invalid input. Please enter a number between 2 and 6.")
for i in range(num_players):
    name = input(f"Enter name for Player {i + 1}: ")
    player_names.append(name)       
flop = Card_Generator.flop()
turn = Card_Generator.turn()
river = Card_Generator.river()
for player_name in player_names:
    with open(f"{player_name}.txt", "w") as f:
        f.write(f"Player: {player_name}\n")
        hand = Card_Generator.gen_hand()
        f.write(f"Hand: {hand}\n")
        print(f"{player_name}'s hand: {hand}")
        print("make your bets now!")
        time.sleep(1)
        f.write(f"Flop: {flop}\n")
        print(f"Flop: {flop}")
        print("make your bets now!")
        hand_rank = evaluate_hand.evaluate_hand(hand + flop)
        f.write(f"Hand Rank: {hand_rank}\n")
        print(f"{player_name}'s hand rank: {hand_rank}\n")
    time.sleep(1)
