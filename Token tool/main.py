#imports needed modules
from requests import post
import colorama

#returns input given by the user
email=str(input("Enter your email : "))
passwrd=str(input("Enter your password : \n"))

#url: request URL (API)
#payload: request payload (JSON)
url='https://discord.com/api/v9/auth/login'
payload={"login": email, "password": passwrd}

#takes both the request URL & the request payload
def Send_request(request_url : str ,request_payload : any):
    #tries to send a request to the given url

    try:
        Request = post(request_url,json=request_payload)
        Response = Request.json()

        #returns both the results and a success message if the response code is 200. 
        if Request.status_code == 200:
            print(f"{colorama.Fore.GREEN} [+] {colorama.Style.RESET_ALL}User_id - {Response['user_id']}\n{colorama.Fore.GREEN} [+] {colorama.Style.RESET_ALL}Token - {Response['token']}\n")
        else:
            pass
    except:
        #returns an error message if the response code is not 200 or if any other issue happend. 
        print(f"{colorama.Fore.RED} [-] {colorama.Style.RESET_ALL} Unexpected error.")

#runs the function
if __name__=="__main__":
    #imports needed modules
from requests import post
from time import sleep
import colorama

#returns input given by the user
email=str(input("Enter your email : "))
passwrd=str(input("Enter your password : \n"))

#url: request URL (API)
#payload: request payload (JSON)
url='https://discord.com/api/v9/auth/login'
payload={"login": email, "password": passwrd}

#takes both the request URL & the request payload
def Send_request(request_url : str ,request_payload : any):
    #tries to send a request to the given url

    try:
        Request = post(request_url,json=request_payload)
        Response = Request.json()

        #returns both the results and a success message if the response code is 200. 
        if Request.status_code == 200:
            print(f"{colorama.Fore.GREEN} [+] {colorama.Style.RESET_ALL}User_id - {Response['user_id']}\n{colorama.Fore.GREEN} [+] {colorama.Style.RESET_ALL}Token - {Response['token']}\n")
        else:
            pass
    except:
        #returns an error message if the response code is not 200 or if any other issue happend. 
        print(f"{colorama.Fore.RED} [-] {colorama.Style.RESET_ALL} Unexpected error.")

#runs the function
if __name__=="__main__":
    Send_request(url,payload)
