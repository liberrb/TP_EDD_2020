"""Load configuration from .ini file."""
import configparser

# Read local file `config.ini`.
config = configparser.ConfigParser()                                     
config.read('config.ini')

print(config)

# Get values from our .ini file
#config.get('DATABASE', 'HOST')
#config['DATABASE']['HOST']

print(config['DATABASE']['HOST'])
print(config['FILES']['TEMPLATES_FOLDER'])
print(config['APP']['ENVIRONMENT'])
print(config['APP']['DEBUG'])
print(config['BOTS']['SPIDERS'])