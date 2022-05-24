
from reqUrlTo import reqURL

def moviesVerse(url_base,automate=False,bolly=False,fstLink=int(1),sndLink=int(1)):
   
   
   
   soup = reqURL(url_base)

   movieCards = [x.a['href'] for x in soup.find_all(
      'h2', attrs={'class': 'title front-view-title'})]

   j = 1
   for i in movieCards:
      print(j, i, end="\n----------------------------------------------------\n")
      j += 1


   if (automate==True):
      select_result = fstLink  # Automated Selction MOVIE HERE ////////////////////
   else:
      select_result = int(input('👉select: ')) # TAKING INPUT FOR MOVIE HERE ////////////////////
   
   
   if(select_result > len(movieCards)):              # SELECTING PAGE RESULT LINK ////////////////////   
      print('Invalid Selection Number')              #                            //////////////////// 
   else:                                             #                            ////////////////////   
      selected_result = movieCards[(select_result-1)]#                            ////////////////////   
   
   
   selected_result_downloads_links = reqURL(selected_result)
   
   # ----////////////////////-- FIDING---DOWNLOAD---LINKS---////////////////////
   download_links = [x['href'] for x in selected_result_downloads_links.find_all( 'a', attrs={'class': 'maxbutton-1 maxbutton maxbutton-download-links'})]

   download_num = 1

   print('\nO->>Select from download links\n')
   
   
   
   
   
   
   #------ /\/\/\/\/\/\/\/\/\/\/\/\/\///////ITERATING DOWNLOAD lINKS ------------------------------/\//\//\/\/\/\//\/\//\/\/\/\/\/\/
   
   for i in download_links:
      
      if(download_num == 1):
         print('\nQuality : Low Res \n-----------')
         
      if(j == 2):
         print('\nQuality : High Res \n-----------')
         
      download_num += 1
      
      print(f"⬇️o{download_num-1}", i,end="\n----------------------------------------------------\n")
   
   
   
   ##   -----------////////////////////SELECTION OF LINK-------------////////////////////
   if (automate==True):
      selected_downloads = sndLink
   else:
      selected_downloads = int(input('👉Select Links From Here: '))
   
   if(selected_downloads > len(download_links)):
      
      print('Invalid Selection Number')
      
   else:
      
      selected_download_links = download_links[(selected_downloads-1)]

   
   soup_download=reqURL(selected_download_links)
   if(bolly):
      nextLink = soup_download.find(
          'a', attrs={'class': 'maxbutton-5 maxbutton maxbutton-fast-server-gdrive'})['href']
   else:
      nextLink=soup_download.find('a',attrs={'class':'maxbutton-1 maxbutton maxbutton-fast-server-gdrive'})['href']
   return nextLink
    



