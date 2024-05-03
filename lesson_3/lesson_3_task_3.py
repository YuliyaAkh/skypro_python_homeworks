from address import Address
from mailing import Mailing

to_address = Address("987065", "Москва", "Пушкина", "55", "12")
from_address = Address("876541", "Казань", "Петербургская", "32", "5")
mailing = Mailing(to_address, from_address, 500, "12345")

print(f'Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city},'
      f'{mailing.from_address.street}, {mailing.from_address.house},'
      f'- {mailing.from_address.apartment} в {mailing.to_address.index},'
      f'{mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house},'
      f' - {mailing.to_address.apartment} . Стоимость {mailing.cost} рублей')
 
