import Pyro5.api
from product import Product

@Pyro5.api.expose
class ProductService:

    def getProduct(self):

        product = Product(
            101,
            "Laptop",
            45000
        )

        return str(product)


def main():

    daemon = Pyro5.api.Daemon()

    uri = daemon.register(ProductService)

    print("===================================")
    print(" Pyro5 Server Running ")
    print("===================================")
    print(uri)
    print()
    print("Copy this URI into client.py")
    print()

    daemon.requestLoop()


if __name__ == "__main__":
    main()