class MyCircularQueue:
    def __init__( self, k: int ):
        self.queue = [ None ]*k
        self.size = k
        self.it = 0
        self.qu = 0
    
    def enQueue( self, value: int ) -> bool:
        if self.queue[ self.it % self.size ] != None:
            return False
        self.queue[ self.it % self.size ] = value
        self.it = ( self.it + 1 )
        return True
    
    def deQueue( self ) -> bool:
        if self.queue[ self.qu % self.size ] == None:
            return False
        self.queue[ self.qu % self.size ] = None
        self.qu = ( self.qu + 1 )
        return True

    def Front( self ) -> int:
        if self.queue[ (self.it-1) % self.size ] == None:
            return -1
        return self.queue[ (self.it-1) % self.size ]

    def Rear( self ) -> int:
        if self.queue[ (self.qu) % self.size ] == None:
            return -1
        return self.queue[ (self.qu) % self.size ]

    def isEmpty( self ) -> bool:
        if self.it == self.qu and self.queue[ (self.it) % self.size ] == None:
            return True
        return False
    
    def isFull( self ) -> bool:
        if (self.it%self.size) == (self.qu%self.size) and self.queue[ (self.it) % self.size ] != None:
            return True
        return False
