def read_file(filename): 
    try: 
        f = open(filename, 'r')
        text = f.read()
        f.close()
        return text
    except OSError: 
        return 'Файлът не може да бъде отворен'
