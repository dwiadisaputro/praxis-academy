
class Api:
    def fetch_remote_data(self):
        print('Api called')
        return 42

class BusinessLogic:
    def __init__(self, api: Api):
        self.api = api
        
    def do_stuff(self):
        api_result = self.api.fetch_remote_data()
        print(f'the api returned a result: {api_result}')
        #do something with the data and return a result
        
# ---

if __name__ == '__main__':
    api = Api()
    logic = BusinessLogic(api=api)
    
    # ...
    print(logic.do_stuff())

## lebih komplek lagi, dengan menggunakan injector, dengan memasukkan "pip install injector" di dalam terminal
## hasilnya sbagai berikut----
## blk@blk-HP-Pavilion-Gaming-Laptop-15-dk1xxx:~$ pip install injector
## Collecting injector
##   Downloading injector-0.19.0-py2.py3-none-any.whl (19 kB)
## Collecting typing-extensions>=3.7.4; python_version < "3.9"
##   Downloading typing_extensions-4.2.0-py3-none-any.whl (24 kB)
## Installing collected packages: typing-extensions, injector
## Successfully installed injector-0.19.0 typing-extensions-4.2.0



class Api:
    def fetch_remote_data(self):
        print('Api called')
        return 42
    
class BusinessLogic:
    def __init__(self, api: Api):
        self.api = api
    
    
    def do_stuff(self):
        api_result = self.api.fetch_remote_data()
        print(f'the api returned a result: {api_result}')
        # do something with the data and return a result

from injector import Injector, Module, singleton, provider


class AppModule(Module):
    
    @singleton
    @provider
    def provide_business_logic(self, api: Api) -> BusinessLogic:
        return BusinessLogic(api=api)
    
    @singleton
    @provider
    def provide_api(self) -> Api:
        # there is no complex logic in our case,
        # but you can use this method to hide the complexity of inittial configuration
        # e.g. when instantiating a particular DB connector.
        return Api()
if __name__ == '__main__':
    injector = Injector(AppModule())
    
    logic = injector.get(BusinessLogic)
    logic.do_stuff()

class TestApi(Api):
    def fetch_remote_data(self):
        print('DemoApi called')
        return 24
    
class TestAppModule(Module):
    
    @singleton
    @provider
    def provide_api(self) -> Api:
        return TestApi()

if __name__ =='__main__':
    real_injector = Injector(AppModule())
    test_injector = Injector([AppModule(), TestAppModule()])
    
    real_logic = real_injector.get(BusinessLogic)
    real_logic.do_stuff()
    
    test_logic = test_injector.get(BusinessLogic)
    test_logic.do_stuff()