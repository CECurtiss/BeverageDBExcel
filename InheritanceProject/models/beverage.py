#Beverage class, Alcohol class, and Beer class go here( maybe also IPA for another?)
class Beverage:
    def __init__(self, name, volume_oz, price):
        self.name = name
        self.volume_oz = volume_oz
        self.price = price

    def serve(self):
        return f"Serving {self.volume_oz}oz of {self.name}."

class Alcohol(Beverage):
    def __init__(self, name, volume_oz, price, alcohol_content):
        super().__init__(name, volume_oz, price)
        self.alcohol_content = alcohol_content

    def serve(self):
        super().serve()
        return f"This product contains {self.alcohol_content}% alcohol. Must be 21+ to consume."
    
    
class Beer(Alcohol):
    def __init__(self, name, volume_oz, price, alcohol_content, beer_type):
        super().__init__(name, volume_oz, price, alcohol_content)
        self.beer_type = beer_type

    def serve(self):
        super().serve()
        return f"Beer is tasty! Enjoy your {self.beer_type}!"
  
class IPA(Beer):
    def __init__(self, name, volume_oz, price,alcohol_content, ibu):
        super().__init__(name, volume_oz, price, alcohol_content, beer_type="IPA")
        self.ibu = ibu

    def serve(self):
        super().serve()
        return f"This IPA has a bitterness of {self.ibu} IBU. Cheers!"
    
class Wine(Alcohol):
    def __init__(self, name, volume_oz, price, alcohol_content, grape_varietal, country):
        super().__init__(name, volume_oz, price, alcohol_content)
        self.grape_varietal = grape_varietal
        self.country = country

    def volume_ml(self):
        return self.volume_oz*29.5735
    
    def serve(self):
        super().serve()
        return f"I love wine! Enjoy your {self.grape_varietal} from {self.country}!"