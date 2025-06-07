from model.restaurant import Restaurant

restaurant_caseiro = Restaurant('Cantinho da Sô', 'brazilian food')
restaurant_caseiro.receiver_assessment('Vero', 10)
restaurant_caseiro.receiver_assessment('Will', 8)
restaurant_caseiro.receiver_assessment('Maya', 9)



def main():
    Restaurant.list_restaurants()

if __name__ == '__main___':
    main()