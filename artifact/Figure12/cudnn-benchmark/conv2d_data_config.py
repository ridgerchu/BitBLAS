conv_infos = [
    {'N': 128,'C':128,'H': 28,'W': 28,'F':128,'K': 3,'S':1,'D': 1,'P': 'SAME','HO':28,'WO':28},
    {'N': 128,'C':128,'H': 58,'W': 58,'F':128,'K': 3,'S':2,'D': 1,'P': 'VALID','HO':28,'WO':28},
    {'N': 128,'C':256,'H': 30,'W': 30,'F':256,'K': 3,'S':2,'D': 1,'P': 'VALID','HO':14,'WO':14},
    {'N': 128,'C':168,'H': 42,'W': 42,'F':168,'K': 1,'S':1,'D': 1,'P': 'VALID','HO':42,'WO':42},
    {'N': 128,'C':512,'H': 7,'W': 7,'F':512,'K': 3,'S':1,'D': 1,'P': 'SAME','HO':7,'WO':7},
    {'N': 128,'C':256,'H': 14,'W': 14,'F':1024,'K': 1,'S':1,'D': 1,'P': 'SAME','HO':14,'WO':14},
    {'N': 128,'C':1024,'H': 14,'W': 14,'F':256,'K': 1,'S':1,'D': 1,'P': 'SAME','HO':14,'WO':14},
    {'N': 128,'C':1024,'H': 14,'W': 14,'F':512,'K': 1,'S':1,'D': 1,'P': 'SAME','HO':14,'WO':14},
    {'N': 128,'C':1008,'H': 21,'W': 21,'F':168,'K': 1,'S':1,'D': 1,'P': 'SAME','HO':21,'WO':21},
    {'N': 128,'C':42,'H': 83,'W': 83,'F':42,'K': 1,'S':1,'D': 1,'P': 'VALID','HO':83,'WO':83},
    {'N': 128,'C':4032,'H': 11,'W': 11,'F':672,'K': 1,'S':1,'D': 1,'P': 'SAME','HO':11,'WO':11},
    {'N': 128,'C':512,'H': 16,'W': 16,'F':512,'K': 3,'S':2,'D': 1,'P': 'VALID','HO':7,'WO':7},
    {'N': 128,'C':96,'H': 83,'W': 83,'F':42,'K': 1,'S':1,'D': 1,'P': 'SAME','HO':83,'WO':83},
    {'N': 128,'C':96,'H': 165,'W': 165,'F':42,'K': 1,'S':1,'D': 1,'P': 'SAME','HO':165,'WO':165},
    {'N': 128,'C':168,'H': 83,'W': 83,'F':84,'K': 1,'S':1,'D': 1,'P': 'SAME','HO':83,'WO':83},
    {'N': 128,'C':336,'H': 21,'W': 21,'F':336,'K': 1,'S':1,'D': 1,'P': 'VALID','HO':21,'WO':21},
    {'N': 128,'C':512,'H': 28,'W': 28,'F':1024,'K': 1,'S':2,'D': 1,'P': 'VALID','HO':14,'WO':14},
    {'N': 128,'C':64,'H': 56,'W': 56,'F':256,'K': 1,'S':1,'D': 1,'P': 'SAME','HO':56,'WO':56},
    {'N': 128,'C':256,'H': 56,'W': 56,'F':64,'K': 1,'S':1,'D': 1,'P': 'SAME','HO':56,'WO':56},
    {'N': 128,'C':128,'H': 28,'W': 28,'F':512,'K': 1,'S':1,'D': 1,'P': 'SAME','HO':28,'WO':28},
    {'N': 128,'C':512,'H': 28,'W': 28,'F':128,'K': 1,'S':1,'D': 1,'P': 'SAME','HO':28,'WO':28},
    {'N': 128,'C':168,'H': 42,'W': 42,'F':84,'K': 1,'S':1,'D': 1,'P': 'SAME','HO':42,'WO':42},
    {'N': 128,'C':512,'H': 28,'W': 28,'F':256,'K': 1,'S':1,'D': 1,'P': 'SAME','HO':28,'WO':28},
    {'N': 128,'C':64,'H': 56,'W': 56,'F':64,'K': 3,'S':1,'D': 1,'P': 'SAME','HO':56,'WO':56},
    {'N': 128,'C':2016,'H': 21,'W': 21,'F':672,'K': 1,'S':1,'D': 1,'P': 'SAME','HO':21,'WO':21},
    {'N': 128,'C':512,'H': 7,'W': 7,'F':2048,'K': 1,'S':1,'D': 1,'P': 'SAME','HO':7,'WO':7},
    {'N': 128,'C':2048,'H': 7,'W': 7,'F':512,'K': 1,'S':1,'D': 1,'P': 'SAME','HO':7,'WO':7},
    {'N': 128,'C':84,'H': 42,'W': 42,'F':84,'K': 1,'S':1,'D': 1,'P': 'VALID','HO':42,'WO':42},
    {'N': 128,'C':336,'H': 42,'W': 42,'F':168,'K': 1,'S':1,'D': 1,'P': 'SAME','HO':42,'WO':42},
    {'N': 128,'C':672,'H': 11,'W': 11,'F':672,'K': 1,'S':1,'D': 1,'P': 'VALID','HO':11,'WO':11},
    {'N': 128,'C':1024,'H': 14,'W': 14,'F':2048,'K': 1,'S':2,'D': 1,'P': 'VALID','HO':7,'WO':7},
    {'N': 128,'C':2016,'H': 11,'W': 11,'F':336,'K': 1,'S':1,'D': 1,'P': 'SAME','HO':11,'WO':11},
    {'N': 128,'C':2016,'H': 21,'W': 21,'F':336,'K': 1,'S':1,'D': 1,'P': 'SAME','HO':21,'WO':21},
    {'N': 128,'C':1008,'H': 42,'W': 42,'F':336,'K': 1,'S':1,'D': 1,'P': 'SAME','HO':42,'WO':42},
    {'N': 128,'C':64,'H': 56,'W': 56,'F':64,'K': 1,'S':1,'D': 1,'P': 'SAME','HO':56,'WO':56},
    {'N': 128,'C':3,'H': 230,'W': 230,'F':64,'K': 7,'S':2,'D': 1,'P': 'VALID','HO':112,'WO':112},
    {'N': 128,'C':3,'H': 331,'W': 331,'F':96,'K': 3,'S':2,'D': 1,'P': 'VALID','HO':165,'WO':165},
    {'N': 128,'C':256,'H': 56,'W': 56,'F':128,'K': 1,'S':1,'D': 1,'P': 'SAME','HO':56,'WO':56},
    {'N': 128,'C':256,'H': 14,'W': 14,'F':256,'K': 3,'S':1,'D': 1,'P': 'SAME','HO':14,'WO':14},
    {'N': 128,'C':2688,'H': 11,'W': 11,'F':672,'K': 1,'S':1,'D': 1,'P': 'SAME','HO':11,'WO':11},
    {'N': 128,'C':1008,'H': 42,'W': 42,'F':168,'K': 1,'S':1,'D': 1,'P': 'SAME','HO':42,'WO':42},
    {'N': 128,'C':96,'H': 83,'W': 83,'F':42,'K': 1,'S':1,'D': 1,'P': 'VALID','HO':83,'WO':83},
    {'N': 128,'C':256,'H': 56,'W': 56,'F':512,'K': 1,'S':2,'D': 1,'P': 'VALID','HO':28,'WO':28},
    {'N': 128,'C':1344,'H': 21,'W': 21,'F':336,'K': 1,'S':1,'D': 1,'P': 'SAME','HO':21,'WO':21},
]