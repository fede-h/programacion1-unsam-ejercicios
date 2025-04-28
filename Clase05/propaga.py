def propagar(vector):
    'Recibe un vector y devuelve la propagación de 1s a 0s'

    print(vector)
    for i in range(0, len(vector)-1, 1):
        if vector[i] == 1 and vector[i+1] != -1:
            vector[i+1] = 1

    for i in range(len(vector)-1, 0, -1):
        if vector[i] == 1 and vector[i-1] != -1:
            vector[i-1] = 1
    
    return vector


print(propagar([ 0, -1, 0, 1, 0, 0]))
