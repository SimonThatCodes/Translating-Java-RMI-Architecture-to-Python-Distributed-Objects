import Pyro5.api

uri = "PYRO:obj_bf896c331ae743beba5c7548a7d6bca0@localhost:39794"

server = Pyro5.api.Proxy(uri)

print("=======================")
print("Client Connected")
print("=======================")
print(server.getProduct())