from hprose import HttpClient

if __name__ == '__main__':
    client = HttpClient('http://localhost:8080/')
    
    print("Update teste:", client.update("teste", 2))  
    print("Get teste:", client.get("teste"))            
    print("Update teste:", client.update("teste", 9))         
    print("Get teste:", client.get("teste"))          
