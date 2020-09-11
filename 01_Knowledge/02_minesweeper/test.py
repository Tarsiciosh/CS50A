from minesweeper import Minesweeper, MinesweeperAI


myM = Minesweeper(height=8,width=8,mines=8)
myMAI = MinesweeperAI(height=8,width=8)

def main():
  myM.print()
  
  myMAI.mark_safe((0,1))
  myMAI.mark_safe((1,0))
  
  print("moves_made:",myMAI.moves_made)
  print("mines:",myMAI.mines)
  print("safes:",myMAI.safes)

  myMAI.add_knowledge((0,0),1)

  print("moves_made:",myMAI.moves_made)
  print("mines:",myMAI.mines)
  print("safes:",myMAI.safes)

  print("knowledge:")
  for sentence in myMAI.knowledge:
    print(sentence)

  cell=myMAI.make_safe_move()
  print("safe move:",cell)


if __name__ == "__main__":
    main()