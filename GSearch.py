# Google search in firefox list of entries
import webbrowser
print("Write your google search entries separated by ;\n" +
      "Example: how to Python;run Python script; \n" +
      "If you want to do a wiki search, insert wiki at the end\n" +
      "Example: cat;dog;wiki;\n")

searchN = 1
while True:
    searchList = str(input("Search #" + str(searchN) +"\n"))
    searchList = searchList.split(";")
    
    #Delete empty list element
    del searchList[-1]
    
    #Wiki search?
    if searchList[-1] == "wiki":
        wiki = True
        del searchList[-1]
    else:
        wiki = False
    
    n = 1
    for searchEntry in searchList: 
        searchEntry = searchEntry.split(" ")
        gQuery = "www.google.com/search?q=" 
        
        m = 1
        for word in searchEntry:
            if m == 1:
                gQuery = gQuery + word
                m = 2
            else:
                gQuery = gQuery + "+" + word
        if wiki == True:
            gQuery = gQuery + "+wikipedia+en"
        webbrowser.open(gQuery, n)
        n = 0
    searchN += 1