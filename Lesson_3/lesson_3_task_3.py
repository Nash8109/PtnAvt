from address import Address
from mailing import Mailing

to_address = Address("426000", "Ижевск", "Лихвинцева", "58", "72")
from_address = Address("427000", "Хохряки", "Трактовая", "2Г", "23")
mailing = Mailing(to_address, from_address, 426, "AFJ345")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city},"
      f" {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartament} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
      f"{mailing.to_address.house} - {mailing.to_address.apartament}. Стоимость {mailing.cost} рублей.")