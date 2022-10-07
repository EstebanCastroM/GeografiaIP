#Obtener la ubicacion geografica de una IP
#import geoip2.database
import geoip2.database

#cargar base de datos
reader = geoip2.database.Reader('/path/to/GeoLite2-City.mmdb')

#obtener informacion de la IP
response = reader.city('189.203.7.59')

#imprimir informacion

print(response.country.iso_code)
print(response.country.name)
print(response.postal.code)
print(response.subdivisions.most_specific.name)
print(response.city.name)
print(response.location.latitude)
print(response.location.longitude)
