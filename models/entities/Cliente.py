""" 
priNom: Obligatorio
segNom: Opcional
priApe: Obligatorio
segApe: Opcional
nit: Obligatorio
 """

class Cliente:
    _id: int = None
    _priNom: str
    _segNom: str
    _priApe: str
    _segApe: str
    _nit: str

    def __init__(self, priNom:str, segNom:str, priApe:str, segApe:str, nit:str):
        self._priNom = priNom
        self._segNom = segNom
        self._priApe = priApe
        self._segApe = segApe
        self._nit = nit

    def getPriNom(self) -> str:
        return self._priNom
    
    def getSegNom(self) -> str:
        return self._segNom
    
    def getPriApe(self) -> str:
        return self._priApe
    
    def getSegApe(self) -> str:
        return self._segApe
    
    def getNit(self) -> str:
        return self._nit
    
    def getId(self) -> int:
        return self._id
    
    def getFullName(self) -> str:
        fullName:str = self._priNom

        if self._segNom != "":
            fullName += f" {self._segNom}"
        
        fullName += f" {self._priApe}"

        if self._segApe != "":
            fullName += f" {self._segApe}"

        return fullName
    
    def setId(self, id:int):
        if self._id is None:
            self._id = id