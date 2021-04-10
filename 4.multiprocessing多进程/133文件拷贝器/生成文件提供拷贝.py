for i in range(21):
    f = open("text/"+str(i)+".txt", "wb")
    f.write(((str(i)+"|")*1000000).encode())
    f.close()
