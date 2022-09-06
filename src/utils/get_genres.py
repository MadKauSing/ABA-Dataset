



def get_genres(path_to_file):
    foo=open(path_to_file,'r')
    lines=foo.readlines()
    
    lines=[x.strip('\n') for x in lines]
    
    return lines
    
    
    
if __name__=="__main__":
    get_genres('./genre.txt')