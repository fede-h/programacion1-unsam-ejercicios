class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0

class TorreDeControl:
    '''Administra una pista de aterrizaje'''

    def __init__(self):
        self.aterrizajes = Cola()
        self.despegues = Cola()

    def nuevo_arribo(self, nombre):
        '''
        Aguarda un nuevo aterrizaje
        y lo coloca al final de la lista
        '''

        self.aterrizajes.encolar(nombre)

    def nueva_partida(self, nombre):
        '''
        Aguarda un despegue y lo
        coloca al final de la lista
        '''

        self.despegues.encolar(nombre)

    def ver_estado(self):
        '''
        Devuelve la lista de espera para
        los arribos y los despegues
        '''

        print('Vuelos esperando para aterrizar:', end=' ')
        if not self.aterrizajes.esta_vacia():
            for avion in self.aterrizajes.items[0:-1]:
                print(avion, end=', ')
            print(self.aterrizajes.items[-1])
        else: print('')

        print('Vuelos esperando para despegar:', end=' ')
        if not self.despegues.esta_vacia():
            for avion in self.despegues.items[0:-1]:
                print(avion, end=', ')
            print(self.despegues.items[-1])
        else: print('')

    def asignar_pista(self):
        '''
        Asigna aterrizajes y luego despegues
        en ese orden de prioridad
        '''

        if not self.aterrizajes.esta_vacia():
            print(f'El vuelo {self.aterrizajes.items[0]} aterrizó con éxito.')
            self.aterrizajes.desencolar()
            
        elif not self.despegues.esta_vacia():
            print(f'El vuelo {self.despegues.items[0]} despegó con éxito.')
            self.despegues.desencolar()
        else:
            print('No hay vuelos en espera')

torre = TorreDeControl()
torre.nuevo_arribo('AR156')
torre.nueva_partida('KLM1267')
torre.nuevo_arribo('AR32')

torre.ver_estado()
torre.asignar_pista()
torre.ver_estado()
torre.asignar_pista()
torre.ver_estado()
torre.asignar_pista()
torre.ver_estado()
torre.asignar_pista()
