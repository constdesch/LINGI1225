
class Compte:
    def __init__(self,nom,prenom,sexe,type,montant):
        self.__nom = nom
        self.__prenom = prenom
        self.__sexe = sexe
        self.__type = type
        self.__montant = [montant]

    def getMontant(self):
        return self.__montant[-1]
    def setMontant(self,montant):
        self.__montant[-1] = montant
    def nouveauMois(self):
        self.__montant +=[self.__montant[-1]]
    def interet(self):
        if len(self.__montant) <12 or (self.__type not in ["normal","premium"]):
            return False
        somme = 0
        for i in range(1,13):
            somme += self.__montant[-i]
        mean = somme/12.0
        if type == "premium":
            self.__montant += [self.__montant[-1]+0.02*mean]
        else:
            self.__montant += [self.__montant[-1]+0.01*mean]
        return True

account = Compte("de Schaetzen","Constantin",1,"premium",300.0)
print(account.getMontant()) #should print 300.0
account.nouveauMois()
account.setMontant(600)
account.nouveauMois()
print(account.interet()) #should print False
for i in range(12):
    account.nouveauMois()
print(account.interet()) #should print true
print(account.getMontant())
