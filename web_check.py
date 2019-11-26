def urlSimilarity(url1, url2):
    import urllib    
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
    return scor
    
#functia returneaza un scor bazat pe similaritatile dintre cele 2 url-uri