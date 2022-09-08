import os
files=open('../genres.txt','r')
genres=[x.strip('\n') for x in files.readlines()]

os.system('cd ..')
os.system('mkdir abad')

for i in genres:
    os.system(f'mkdir /abad/{i}')

    
