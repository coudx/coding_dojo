from classes.product import product
from classes.store import store

nordstorm = store("nordstorm")
tanktop = product("tanktop", "cloth", 16)
dress = product("dress", "cloth", 50)
shorts = product("shorts", "cloth", 20)
nordstorm.add_product(tanktop).add_product(dress).add_product(shorts)
