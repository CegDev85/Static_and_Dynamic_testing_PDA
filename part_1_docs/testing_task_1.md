### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:  #this should have a == to check for equality
      return True
    else     #missing : after else
      return False
   

  dif highest_card(self, card1 card2): #def spelled wrong and , missed between card1 and card 2
  if card1.value > card2.value:  #the if statement should be indented within the function
    return card   #this should be card1,as card isnt being passed
  else:
    return card2
  


def cards_total(self, cards): #the whole function needs moved to be withink the class.
  total      #this needs set to something to start i.e = 0
  for card in cards:
    total += card.value
    return "You have a total of" + total  #this line should be back to match the indentation of the for loop initialising
    #total needed to be a string not an int for the assertion to be correct.
  
```
