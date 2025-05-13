from hprose import HttpClient
if __name__ == '__main__':
    client2 = HttpClient('http://localhost:8080/')
    
    print("Update teste2:", client2.update("teste2", 10))  
    print("Get teste2:", client2.get("teste2"))            
    print("Update teste2:", client2.update("teste2", 20))         
    print("Get teste2:", client2.get("teste2"))          
