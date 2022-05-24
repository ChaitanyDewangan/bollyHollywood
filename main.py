try:
    select_wood=int(input(' 01 Hollywood \n 02.Bollywood \n --> '))
    search_movie=str(input('❤️ Search Movie Here :: \n '))
except KeyboardInterrupt :
    quit()

from moviesverse import moviesVerse

if select_wood==1:
    base_url=f'https://moviesverse.cc/?s={search_movie}'
else:
    base_url=f'https://bollyverse.xyz/?s={search_movie}'    

automate=int(input('01.Manual \n02.To Automate \n --> '))

if automate!=1:
        select_1=int(input('O> Select Movie No. -->  '))
        select_2=int(input('O> Select Quality --> '))

        
def Hollywood():
    if automate==1:
        print(moviesVerse(base_url))
    else:
        print(moviesVerse(base_url,True,select_1,select_2))
def Bollywood():
    if automate==1:
        print(moviesVerse(base_url))
    else:
        print(moviesVerse(base_url,True,select_1,select_2))
if __name__=='__main__':
    if select_wood==1:
        Hollywood()
    else:
        Bollywood()
