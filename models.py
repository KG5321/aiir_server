from server import db


class Uzytkownik(db.Model):
    ID = Column(Integer, primary_key=True)
    Login = Column(String(150), unique=True, nullable=False)
    E_mail = Column(String(150), unique=True, nullable=False)
    Sol = Column(String(150))
    Uprawnienia = Column(String(20))
#    __tablename__ = 'users'
    def __repr__(self):
        return self.name



class Zlecenie(db.Model):
    relacja = relationship("Uzytkownik")
    ID_Uzytkownika = Column(Integer, nullable=False, ForeignKey('relacja.ID')
    ID_Zlecenia = Column(Integer, primary_key=True)
    Data = Column(Date)
    Dane_wejsciowe = Column(String(150))
    Liczba_Klastrow = Column(Integer)
    Ziarnistosc = Column(Integer)
    Metoda = Column(String(150))
    Parametry = Column(String(150))
    Status = Column(String(150))
    Hash = Column(String(150))
    Czas = Column(Integer)
    Haslo = Column(String(150))

    def __repr__(self):
        return self.name
