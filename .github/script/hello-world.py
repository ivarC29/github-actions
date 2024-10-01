import os

def run():
    name = os.getenv("USERNAME")
    print(f"Hola, {name} desde github !")


if __name__ == "__main__":
    run()
