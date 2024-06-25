import configparser
config = configparser.ConfigParser()


config.read(r'D:\my_apps\warhammer\config.ini')

DROPBOX_API_TOKEN: str = config['APIKEY']['DROPBOX']
BOOK_NAME: str = config['BOOK']['NAME']
