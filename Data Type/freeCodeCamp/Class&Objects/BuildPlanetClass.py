class Planet:
    def __init__(self,name,planet_type,star):
        #Handle the case where the user might input a non-string value for name, planet_type, or star, or an empty string.
        if not isinstance(name,str) and isinstance(planet_type,str) and isinstance(star,str):
            raise TypeError("name, planet type, and star must be strings")
        elif not isinstance(planet_type,str):
            raise TypeError("name, planet type, and star must be strings")
        elif not isinstance(star,str):
            raise TypeError("name, planet type, and star must be strings")
        if not (name and planet_type and star):
            raise ValueError("name, planet_type, and star must be non-empty strings")
        self.name=name
        self.planet_type=planet_type
        self.star=star
        
    def orbit(self):
        return f'{self.name} is orbiting around {self.star}...'
    def __str__(self):
        return f'Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}'

planet_1=Planet("Earth", "Terrestrial", "Sun")
planet_2=Planet("Earth", "Terrestrial", "Sun")
planet_3=Planet("Earth", "Terrestrial", "Sun")

print(planet_1)
print(planet_2)
print(planet_3)

print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())