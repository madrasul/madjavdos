

def kwargsAcceptFun(**kwargs):
    # Print all key-value pairs
    for key, value in kwargs.items():
        print(f"{key}: {value}")


kwargsAcceptFun(city="Tashkent", temperature=25, humidity="60%")
