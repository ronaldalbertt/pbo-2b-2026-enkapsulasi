class Member:
    # Constructor
    def __init__(self, id, nama, email):

        if not isinstance(id, str):
            raise TypeError("Id harus String")
        
        if not isinstance(nama, str):
            raise TypeError("Nama harus String")
        
        if not isinstance(email, str):
            raise TypeError("Email harus String")
        
        if len(id) < 1:
            raise ValueError("Id minimal 1 karakter")
        
        if len(nama) < 3:
            raise ValueError("Nama minimal 3 karakter")

        self.__id = id
        self.__nama = nama
        self.__email = email
        self.__last_visited = None
    
    # Setter
    def set_nama(self, nama):
        if not isinstance(nama, str):
            raise TypeError("Nama harus String")
        

        if len(nama) < 3:
            raise ValueError("Nama minimal 3 karakter")

        self.__nama = nama



    # Getter
    def get_id(self):
        return self.__id
    
    # Getter
    def get_nama(self):
        return self.__nama