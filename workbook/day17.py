lists = [
    [1,2,3],
    ['a','b','c']
    [1,1,1]
    
]

t = [True,False,True,False,False,True]

res = [x for x in lists if all([isinstance(item, int) for item in x] and sum(x)>4 )]

res1 = list(filter(lambda x: all([isinstance(item, int) for item in x] and sum(x)>4,lists),lists))
    
         
    


    