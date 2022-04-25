from tkinter import E


class EmailClient(object):
    
    def __init__(self, config):
        self._config = config
        self.connect(self._config)
    
    def connect(self, config):
        #Implement function here
        pass
    
class EmailReader(object):
    
    def __init__(self, client):
        try:
            self._client = client
        except Exception as e:
            raise e
        
    
    def read(self):
        # Implement fuction here
        pass
    

from dependency_injector import providers, containers
from email_client import EmailClient
from email_reader import EmailReader

class Client(containers.DeclarativeContainer):
    config = providers.Configuration('config')
    # other config
    
class Clients(containers.DeclarativeContainer):
    email_client = providers.Singleton(EmailClient, Configs.config)
    # other clients
    
class Readers(containers.DeclarativeContainer):
    email_reader = providers.Factory(EmailReader, client=Clients.email_client)
    # other readers
    
from containers import Readers, Clients, Configs

if __name__ == "__main__":
    Configs.config.override({
        "domain_name": "imap.gmail.com",
        "email_address": "YOUR_EMAIL_ADDRESS",
        "password": "YOUR_PASSWORD",
        "mailbox": "INBOX"
    })
    email_reader = Readers.email_reader()
    print email_reader.read()