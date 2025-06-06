import os

restaurants = [{'name':'Cantinho da Sô', 'category':'Caseira', 'ative':False},
               {'name':'Monkey', 'category':'Japonesa', 'ative':True},
               {'name':'Cantinho da Sô Pizzas', 'category':'Pizzaria', 'ative':True}]

def program_name():
    ''' Displays the stylized name of the program on the screen '''
    print("""
𝕗𝕣𝕖𝕕 𝕕𝕖𝕝𝕚𝕧𝕖𝕣𝕪
""")

def options_action():
    ''' Displays the options available in the main menu '''
    print('1. Register restaurant')
    print('2. List restaurant')
    print('3. Toggle restaurant status')
    print('4. Exit\n')

def finish_app():
    ''' Displays application termination message '''
    show_subtitle('Finalize app')

def back_menu():
    ''' Prompts for a key to return to the main menu
    
    Outputs:
    - Return to main menu
    '''
    input('\nPress a key to return to the main menu')
    main()

def not_found_option():
    ''' Displays invalid option message and returns to main menu
    
    Outputs:
    - Return to main menu
    '''
    print('Invalid option!\n')
    back_menu()

def show_subtitle(text):
    ''' Displays a stylized subtitle on the screen 
    
    Inputs:
    - text: str - The subtitle text
    '''
    os.system('cls')
    line = '*' * (len(text)) 
    print(line)
    print(text)
    print(line)
    print()

def new_restaurant_register():
    ''' This function is responsible for registering a new restaurant 
    
    Inputs:
    - Restaurant name
    - Category

    Outputs:
    - Add a new restaurant to the restaurant list

    '''
    show_subtitle('Registration of new restaurants')
    restaurant = input('Enter the name of the restaurant you want to register: ')
    category_restaurant = input(f'Enter the restaurant category {restaurant}: ')
    restaurant_data = {'name':restaurant, 'category':category_restaurant, 'ative':False}
    restaurants.append(restaurant_data)
    print(f'The restaurant {restaurant} was successfully registered!')
    back_menu()

def restaurant_list():
    ''' List the restaurants present in the list 
    
    Outputs:
    - Displays the list of restaurants on the screen
    '''
    show_subtitle('Listing restaurants')

    print(f'{"Restaurant name".ljust(24)} | {"Category".ljust(20)} | Status')
    for restaurant in restaurants:
        restaurant_name = restaurant['name']
        restaurant_category = restaurant['category']
        ative = 'activated' if restaurant['ative'] else 'disabled'
        print(f'- {restaurant_name.ljust(22)} | {restaurant_category.ljust(20)} | {ative}')

    back_menu()

def change_restaurant_status():
    ''' Changes the active/deactivated status of a restaurant 
    
    Outputs:
    - Displays message indicating the success of the operation
    '''
    show_subtitle('Changing restaurant status')

    name_restaurant = input('Enter the name of the restaurant you want to change the status of: ')
    restaurant_check = False

    for restaurant in restaurants:
        if name_restaurant == restaurant['name']:
            restaurant_check = True
            restaurant['ative'] = not restaurant['ative']
            msg = f'The restaurant {name_restaurant} has been activated successfully!' if restaurant['ative'] else f'The restaurant {name_restaurant} has been successfully deactivated!'
            print(msg)

    if not restaurant_check:
        print('Restaurant not found')

    back_menu()

def choose_option():
    ''' Requests and executes the option chosen by the user 
    
    Outputs:
    - Executes the option chosen by the user
    '''
    try:
        option_select = int(input('Choose an option: '))
        match option_select:
            case 1:
                new_restaurant_register()
            case 2:
                restaurant_list()
            case 3:
                change_restaurant_status()
            case 4:
                finish_app()
            case _:
                not_found_option()
    except:
        not_found_option()

def main():
    ''' Main function that starts the program '''
    os.system('cls')
    program_name()
    options_action()
    choose_option()

if __name__ == '__main__':
    main()