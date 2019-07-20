import requests

def mohib(verb,url,api_endpoint):
    if request.method=='GET':
        url+=api_endpoint
        response=requests.request(verb,url=url)
        json_data=response.json()
        
        return json_data

    elif verb=="POST":
        url+=api_endpoint
        response=requests.request(verb,url=url)
        return response

    elif verb=="DELETE":
        url+=api_endpoint
        response=requests.request(verb,url=url)
        return response

    elif verb =='PUT':
        url+=api_endpoint
        response=requests.request(verb,url=url)
        return response


x=mohib('GET','https://reqres.in/','/api/users?page=2')
print(x.status_code)



    
    



