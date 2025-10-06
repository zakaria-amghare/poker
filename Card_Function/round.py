def round(table,playerlist):
    table.Up_Date_The_Card()
            choice:str = ""
            print("\n",table)
            print("\n",playerList[i])
            playerList[i].Give_Card(gen_hand)
            actionList :list[str] = returnPossibleAction(playerList[i],table)
            if(actionList[2] == ""):
                choice = int(input(f"1. {actionList[0]}\n2. {actionList[1]}\n"))

            choice = int(input (f"1. {actionList[0]}\n2. {actionList[1]}\n3. {actionList[2]}\n"))

            print(takeAction(playerList,playerList[i],table,actionList[choice-1]))
            print(playerList[i])
            if (allBitched(playerList)):
                table.currentState = tableState.RIVER
                break