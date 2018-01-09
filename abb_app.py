
#from appdata import AppData
#import predictionio
import sys
#from sets import Set

class App:

  def __init__(self):
    pass 

  def run(self):
    state = "Main Menu"
    
    # prompt = "\n" + 
    #   "%s\n" +
    #   "%s\n" +
    #   "Please input selection:\n" +
    #   " 0: Quit application.\n"   +
    #   " 1: Get personalized abbreviation.\n" +   # calc_abbr_task
    #   " 2: Read input file .\n"     +
    #   " 3: Display output file.\n"  +

    while True:
      print("\n {} \n {} \n Please input selection:\n" .format(state, '-'*len(state) )   )
      choice = input().lower()
      if choice == '0':
        print( "\nGood Bye!\n" )
        break
      elif choice == '1':
        self.calc_abbr_task(state)
      elif choice == '2':
        self.calc_abbr_from_file(state)
      elif choice == '3':
        self.display_out_file(state)
      else:
        print( '{} \'%s\' is not a valid selection.' .format( choice))

  def calc_abbr_task(self, prev_state):
    state = prev_state + " / Calc AB "
    print("\n {} \n {} \n Please enter a word for calculating." .format(state, '-'*len(state) )   )

  def calc_abbr_from_file(self, prev_state):
    state = prev_state + " / Calc AB from file"
    print("\n {} \n {} \n Please enter file name to cal AB:" .format(state, '-'*len(state) )   )


  def display_out_file(self, prev_state):
    state = prev_state + " / Display AB with Multiple Movies"
    print("\n {} \n {} \n Please enter file name to display ABs" .format(state, '-'*len(state) )   )

if __name__ == '__main__':

  print( "\nWelcome To Python App!" )
  print( "============================================\n")

  my_app = App()
  my_app.run()
