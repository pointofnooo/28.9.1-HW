import requests

class OrderBaseClient:
    url = "https://restful-booker.herokuapp.com"

    # создание токена
    def create_token(self):
        return requests.post(self.url + '/auth')

    # получение списка гостей
    def booking_all(self):
        return requests.get(self.url + f'/booking/')

    # получение ID
    def booking_id(self):
        return requests.get(self.url + f'/:id/{id}')

    # создание бронирования
    def booking_create(self, traveller):
        return requests.post(self.url + '/booking', json=traveller)

    # обновление бронирования
    def booking_update(self, traveller):
        return requests.put(self.url + '/booking', json=traveller)

    # частичное обновление бронирования
    def booking_part_update(self, traveller):
        return requests.patch(self.url + '/:id', json=traveller)

    # удаление бронирования
    def booking_delete(self, traveller):
        return requests.delete(self.url + '/:id', json=traveller)

    # пинг (работает)
    def booking_ping(self):
        return requests.get(self.url + '/ping')

    #def create_order(self, order):
        # Создание заказа
    #    return requests.post(self.url + '/orders', json=order)

    #def get(self, order_id):
        # Получение заказа
    #    return requests.get(self.url + f'/orders/{order_id}')


order_base_client = OrderBaseClient()
