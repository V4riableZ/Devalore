
#Main List

l = [["name", "dinner"], ["Abraham", "Avi"], ["Hello", "Tree", "Door"], ["Name",
"Glass", "Two", "am"]]

#Sub list for unification 
ll = []

results = sum(l,ll)

#Unification and deduplication of elements in the list

unif = list(map(lambda results:results.title(),results))
unif = list(set(unif))
print("\nNew deduplicated list")
print(unif)

#New unified list for filtering

sl = []
sl = unif+sl

#Creating a mapped list of string elements longer than 6

sl = list(filter(lambda sl: hasattr(sl, "__len__"), sl))
myList_len = list(map(len, sl)) 

xl = list(filter(lambda i: len(i)>= 6, sl))
print("\nMapped list")
print("\n",(xl))


