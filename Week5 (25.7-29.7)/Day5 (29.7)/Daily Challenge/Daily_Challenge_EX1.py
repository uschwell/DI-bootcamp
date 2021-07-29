from os import waitpid
import requests
import time



#dictionary- each key is a website, for each key we have an array (list) that stores the access address, AND the response time it requires
our_urls_time={'google': ['https://www.google.com/',-1], 'ynet': ['https://www.ynet.co.il/home/0,7340,L-8,00.html',-1], 'imdb':['https://www.imdb.com/',-1]}
#for each 
for key in our_urls_time:
    startTime=time.perf_counter()
    r = requests.get(our_urls_time[key][0])

    endTime=time.perf_counter()
    #after making (and receiving) the request, we figure out how much time it took
    totalTime=endTime-startTime
    
    our_urls_time[key][1]=totalTime


#we now print the results
for key in our_urls_time:
    print('It took: '+str(our_urls_time[key][1])+' (fractional) seconds to load '+key)