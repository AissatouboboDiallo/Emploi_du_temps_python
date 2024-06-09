from Activities import Activity
class PrecedenceConstraint:
    def __init__(self,firstActivity : Activity, secondActivity :Activity):
        self.firstActivity = firstActivity
        self.secondActivity = secondActivity
    def getFirst(self):
        return self.firstActivity
    def getSecond(self):
        return self.secondActivity
    def isSatisfied(self,debutFirst,debutSecond):
      contraint = True
      calculDuree = debutFirst + self.getFirst().getDuration()
      if debutSecond < calculDuree:
        contraint = False
      return contraint
if __name__ == "__main__":
    debutFirst = input("Entrer le debut de l'activité 1 : ")
    nameFristActivity =input("Entrer la description de la prémiere activité : ")
    timeFristActivity =input("Entrer sa durée :")
    debutSecond = input("Entrer le debut de l'activité 2 : ")
    nameSecondActivity =input("Entrer la description de la seconde activité : ")
    timeSecondActivity= input("Entrer sa durée :")
    try:
        debutFirst = int(debutFirst)
        debutSecond = int(debutSecond)
        timeFristActivity =int(timeFristActivity)
        timeSecondActivity=int(timeSecondActivity)
        firstActiv = Activity(nameFristActivity,timeFristActivity)
        secondActiv = Activity(nameSecondActivity,timeSecondActivity)
        emploi = PrecedenceConstraint(firstActiv,secondActiv)
        print( "Debut ",debutFirst,emploi.getFirst().getDescription(),'    ',emploi.getFirst().getDuration())
        print("Debut ",debutSecond,emploi.getSecond().getDescription(),'    ', emploi.getSecond().getDuration())
        print(emploi.isSatisfied(debutFirst,debutSecond))
    except ValueError:
        print("Respecter les types des variables")
    finally:
        print("FIN DU PROGRAMME !")