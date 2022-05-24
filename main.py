try:
    automate=int(input('01.Manual \n02.To Automate \n --> '))
    if automate!=1:
        select_1=int(input('O> Select Movie No. -->  '))
        select_2=int(input('O> Select Quality --> '))
    select_wood=int(input(' 01 Hollywood \n 02.Bollywood \n --> '))
    search_movie=str(input('❤️ Search Movie Here :: \n '))
    #automate=2
    # if automate!=1:
    #     select_1=1
    #     select_2=3
    # select_wood=2 BOLLYWOOD
    # search_movie= batman
except KeyboardInterrupt :
    quit()



if select_wood==1:
    base_url=f'https://moviesverse.cc/?s={search_movie}'
else:
    base_url=f'https://betamoviez.xyz/?s={search_movie}'    






from moviesverse import moviesVerse
from bollyverse import bollyVerse
from autoDownld import autoDownld

def Hollywood(bolly=False):
    if automate==1:
        return(moviesVerse(base_url))
    else:
        return(moviesVerse(base_url,True,bolly,select_1,select_2))
def Bollywood():
    if automate==1:
        print(bollyVerse(base_url))
    else:
        print(bollyVerse(base_url,True))
if __name__=='__main__':
    if select_wood==1:
        
        autoDownld(Hollywood())
    else:
        autoDownld(Hollywood(True))
