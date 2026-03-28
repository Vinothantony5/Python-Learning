class laptop():
    price = ""
    processor = ""
    RAM = ""
    Brandname = ""
    def LaptopModel(self):
        print("This is a", self.Brandname, "laptop with", self.processor, "processor and", self.RAM, "RAM. It costs", self.price)

HP = laptop()
HP.price = "50000"
HP.processor = "i5"
HP.RAM = "8GB"
HP.Brandname = "HP"
Lenovo = laptop()
Lenovo.price = "60000"
Lenovo.processor = "i7"
Lenovo.RAM = "16GB"
Lenovo.Brandname = "Lenovo"
Dell = laptop()
Dell.price = "55000"
Dell.processor = "i5"
Dell.RAM = "8GB"
Dell.Brandname = "Dell"
HP.LaptopModel()
Lenovo.LaptopModel()
Dell.LaptopModel()