#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# rcaphair, 03/07/21 modified original script
# Added code to class CD() 
# Created function add_row w/ ValueError exception
# Added code to classFileIO ()
# Two functions: save & load inventory added
# Completed all TODO's for class IO ()
# Added all code to the main body for program functionality
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD():
    
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """

    # [Done - TODO Add Code to the CD class]

    def __init__(self, obj):
        
        self.add_row = obj
        
    def add_row (cd_id, cd_title, cd_artist, table):
    
      try: 
           int_id = int(cd_id)
           dicRow = {'ID': int_id, 'Title': cd_title, 'Artist': cd_artist}
           table.append(dicRow)   
      except ValueError:
           print('\n' + 'Please re-check entry for ID - a non-integer number was entered or the position was left empty.' + '\n')
        
# -- PROCESSING -- #
class FileIO:
    
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    def __init__(self, obj):
        
        self.save_inventory = obj
        self.load_inventory = obj
        
    # @property        
    def save_inventory(self, table):      
        objFile = open(strFileName, 'w')
        for row in table:
            lstValues = list(row.values())
            lstValues[0] = str(lstValues[0])
            objFile.write(','.join(lstValues) + '\n')
        objFile.close()

    # @property 
    def load_inventory(self, table):
        table.clear()  
        objFile = open(strFileName, 'r')
        for line in objFile:
            data = line.strip().split(',')
            dicRow = {'ID': int(data[0]), 'Title': data[1], 'Artist': data[2]}
            table.append(dicRow)
        objFile.close()

    # [Done - TODO Add code to process data to a file]

    # [Done - TODO Add code to process data from a file]

# -- PRESENTATION (Input/Output) -- #

class IO:

    @staticmethod
    def print_menu():
        
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, s, or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')
        
    @staticmethod
    def add_cd_input():
        
        """Takes user input of: ID, Title and Artist to be added to inventory file
        
        Args:
            None.
    
        Returns:
            cd_id, cd_title, cd_artist
        """
        
       
        cd_id = input('Enter ID: ').strip()
        cd_title = input('What is the CD\'s title? ').strip()
        cd_artist = input('What is the Artist\'s name? ').strip()
         
        return cd_id, cd_title, cd_artist


    # [Done - TODO add docstring]
    # [Done - TODO add code to show menu to user]
    # [Done - TODO add code to captures user's choice]
    # [Done - TODO add code to display the current data on screen]
    # [Done - TODO add code to get CD data from user]
    

# -- Main Body of Script -- #

# 1. When program starts, read in the currently saved Inventory

# FileIO.load_inventory(strFileName, lstOfCDObjects)

# 2. start main loop

while True:
    
    # 2.1 Display Menu to user and get choice
    
    IO.print_menu()
    
    strChoice = IO.menu_choice()

    # 3.0 Process menu selection
    # 3.1 process exit first
    
    if strChoice == 'x':
        break
    
    # 3.2 process load inventory

    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            
            FileIO.load_inventory(strFileName, lstOfCDObjects)
            
            IO.show_inventory(lstOfCDObjects)
            
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.

    # 3.3 process add a CD
    
    
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
      
        cd_id, cd_title, cd_artist = IO.add_cd_input()
        # 3.3.2 Add item to the table
        
        CD.add_row (cd_id, cd_title, cd_artist, lstOfCDObjects)        

        IO.show_inventory(lstOfCDObjects)
        
        continue  # start loop back at top.
        
    # 3.3.3 process display current inventory
    
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.


    elif strChoice == 's':
        
        # 3.4.0 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        
        # 3.4.1 Process choice
        if strYesNo == 'y':
            
            # 3.4.1.0 save data

            FileIO.save_inventory(strFileName, lstOfCDObjects)

        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.

    # 3.5 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')

# [Done - TODO Add Code to the main body]

# [Done - Display menu to user]

# [Done - Load data from file into a list of CD objects on script start]

    # [Done - show user current inventory]
    # [Done - let user add data to the inventory]
    # [Done - let user save inventory to file]
    # [Done - let user load inventory from file]
    # [Done - let user exit program]

