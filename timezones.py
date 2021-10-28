from datetime import datetime
import pytz

bogota_timezone = pytz.timezone('America/Bogota')
bogota_date = datetime.now(bogota_timezone)
print("Bogotá: ", bogota_date.strftime("%d/%m/%Y %H:%M:%S"))


santiago_timezone = pytz.timezone('America/Santiago')
santiago_date = datetime.now(santiago_timezone)
print("Santiago: ", santiago_date.strftime("%d/%m/%Y %H:%M:%S"))


buenos_aires_timezone = pytz.timezone('America/Argentina/Buenos_Aires')
buenos_aires_date = datetime.now(buenos_aires_timezone)
print("Buenos Aires: ", buenos_aires_date.strftime("%d/%m/%Y %H:%M:%S"))

san_francisco_timezone = pytz.timezone('America/Los_Angeles')
san_francisco_date = datetime.now(san_francisco_timezone)
print("San Francisco: ", san_francisco_date.strftime("%d/%m/%Y %H:%M:%S"))

mexico_timezone = pytz.timezone('America/Mexico_City')
mexico_date = datetime.now(mexico_timezone)
print("Mexico: ", mexico_date.strftime("%d/%m/%Y %H:%M:%S"))