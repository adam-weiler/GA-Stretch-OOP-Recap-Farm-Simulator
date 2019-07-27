from farm import Field
import sys #Needed to trigger the exit command.

class HighlandFarmsManager:

    def main_menu(self):
        print('Starting up the Highland Farms Manager app')
        while True:
            print('\nWhat would you like to do?')
            self.print_main_menu()
            user_selected = 1
            #user_selected = int(input())
            self.call_option(user_selected)
            break



    def print_main_menu(self):
        print('[1] Add Field --> Adds a new field.')
        # print('[2] Harvest crops --> Harvests crops, & adds to total harvested.')
        # print('[3] Check Status')
        # print('[4] Relax --> Provides lovely description of the fields.')
        print('[5] Exit\n')


    # def valid_input(self, user_input, expected_input, expected_input2=''):
    #     while True:
    #         print(user_input)
    #         print(expected_input)
    #         print(expected_input2)

    #         if (user_input == expected_input) or (user_input == expected_input2):
    #             print('Valid input.\n')
    #             return user_input
    #         else:
    #             print('Invalid input.\n')
    #             # break
    #             user_input = input()


    def call_option(self, user_selected):
        if user_selected == 1:
            self.add_field()
        pass



    def add_field(self, removeme):
        print('What kind of field is it: corn or wheat?')
        new_crop = removeme
        # crop = input()
        print('How large is the field in hectares?')
        new_hectare = 50
        # hectare = input()
        Field.create(new_crop, new_hectare)

        # return 'Added a {crop} field of {hectare} hectares!'

    def harvest_crops(self):
        #for crop in crops
            #optional: print ('Harvesting {} food from a {} hectare corn field.')
            #optional: print ('Harvesting {} food from a {} hectare corn field.')
            #..etc
        # return f'The farm has {} harvested food so far.'
        pass
        

    def check_status(self):
        print('\nDisplay Info about the farm:')
        Field.check_status()




    def relax(self):
        print('\nEnjoy the beauty of each one of your fields:')
        print(Field.relax())


    def exit(self):
        print('Exiting...')
        # exit()














# HighlandFarmsManager.valid_input('corn', 'corn', 'wheat')

# HighlandFarmsManager.valid_input('ducks', 'corn', 'wheat')    #validate_string

# HighlandFarmsManager.valid_input(0, type(0))      #Maybe validate_number  ?


our_hfm_app = HighlandFarmsManager()

# our_hfm_app.main_menu()
# our_hfm_app.print_main_menu()


our_hfm_app.add_field('corn')
our_hfm_app.add_field('wheat')

our_hfm_app.check_status()

our_hfm_app.relax()






#Stretch
#Users enter bad input.
#new field type - blueberries?
#Pastures
    #To store animals
    #On harvest animals breed to make more animals.