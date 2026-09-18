# URL SHORTNER
from random import choice
from string import ascii_letters , digits
import json

try:
     with open('urls.json','r') as file:
        urls=json.load(file)
except(FileNotFoundError,json.JSONDecodeError):
        urls={}

def shorten_url():
         print("URL SHORTNER")
         url=input('Enter URL:')

         if not(url.startswith('https://')or url.startswith('http://')):
              print('INVALID URL')
              return
         
         for code, exsiting_url in urls.items():
             if exsiting_url==url:
                  print('Short URL already exist')
                  print('Short URL: ',code)
                  return
             
         characters= ascii_letters+digits
         shortcode= ''.join(choice(characters)for _ in range(6))
         shorturl= 'https://'+shortcode
         urls[shorturl]=url
         with open('urls.json','w') as file:
              json.dump(urls, file)
              print(shorturl)
                  
     

# shorturl is key and url is value

def resolve_code():
        code=input('Enter Short URL: ')
        if code in urls:
            print(urls[code])
        else:
            print('Short URL not found')
def url_list():
        print('''List of Short URL and URL: ''')
        for code,url in urls.items():
            print(code, '--->', url)
while True:
     print('''*****************MENU****************

     1.Convert long url into short url
     2.Search original url from short url
     3.List of urls
     4.EXIT
     ''')
     option= str(input('Enter your option:  '))
     if option=='1':
         shorten_url()
     elif option=='2':
         resolve_code()
     elif option=='3':
         url_list()
     elif option=='4':
           break
     else:
          print('INVALID CHOICE')



#qDw6iC ---> https://www.youtube.com/
#MRzMJG ---> https://open.spotify.com/
#TqlIZp ---> https://www.chess.com/home
#j0RNPG ---> https://in.pinterest.com/homefeed/
