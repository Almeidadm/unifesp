
if __name__ == '__main__':
  while True:
    cards = list([int(i) for i in input().split(' ')])
    cards.sort()

    if(cards[0] == 0):  break

    elif(cards[0] == cards[1] == cards[2]):
      
      if(cards[0] == 13)
        print('*')
      else: print('%d %d %d' % (cards[0] + 1, cards[0] + 1, cards[0] + 1))
      
    elif (cards[0] == cards[1] or cards[1] == cards[2]):
      
      if(cards[0] == cards[1]):
      # [11, 11, 13]
        if(cards[2] == 13):
          print('%d %d %d' %(1, cards[0]+1, cards[1]+1))
        else:
          print('%d %d %d' %(cards[0], cards[1], cards[2]+1))
      elif(cards[1] == cards[2]):
        # [12, 12, 13] ou [12, 13, 13]
        if (cards[0] == 12 and cards[1] == 13):
          print('1 1 1')
        # [11, 12, 12]
        elif(cards[0]+1 == cards[1]):
          print('%d %d %d' %(cards[1], cards[2], cards[0]+2))
        # [1, 12, 12]
        else:
          print('%d %d %d' % (cards[0] + 1, cards[1], cards[2]))
    
    #não par
    else:
      print('1 1 2')
	
