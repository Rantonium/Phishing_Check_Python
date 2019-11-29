#Functie care compara 2 url-uri in ideea de a gasi tentativele de phishing
#Compar scheme,netloc,paths,query-uri
#in cazul de fata daca comparam url1 cu url2 (url1 are un scor de 18) iar url2 va primi scor 8 in urma comparatiei, determinand
#clar incercarea de phishing
url1="https://webmail.tuiasi.ro/squirrel/src/webmail.php"
url2="https://webmai1.tuiasi.ro/squirrel/src/webmail.php"
def urlSimilar(url1, url2):
    import urllib.parse   
    u1 = urllib.parse.urlparse(url1)
    q1 = urllib.parse.parse_qs(u1.query, keep_blank_values=True)
    p1 = u1.path.split('/')[1:]
    
    u2 = urllib.parse.urlparse(url2)
    q2 = urllib.parse.parse_qs(u2.query, keep_blank_values=True)
    p2 = u2.path.split('/')[1:]
    
    scor = 0
    
    if u1.scheme == u2.scheme: 
        scor += 5
    if u1.netloc == u2.netloc: 
        scor += 10
        
    perechi_path = zip(p1, p2)
    for a, b in perechi_path:
        if a == b:
            scor += 1
        else:
            break
    key_query_comune = q1.keys() & q2.keys()
    scor += len(key_query_comune)
    for key in key_query_comune:
        if q1[key] == q2[key]:
            scor += 1
    print(scor)
    return scor
urlSimilar(url1,url1)
print("vs")
urlSimilar(url1,url2)
