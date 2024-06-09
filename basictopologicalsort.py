from Activities import Activity
from basicConstraint import PrecedenceConstraint
import collections
class TopologicalSort:
   def bruteForceSort(activities, contraintList):
      acts = activities
      resultat = list([])
      while(len(acts)!= 0):
         activiTe = TopologicalSort.auxiliaire(acts, resultat, contraintList)
         if (activiTe == None):
            return None
         resultat.append(activiTe)
         acts.remove(activiTe)
      return resultat
   def auxiliaire(activities,liste,contraintList):
      for activite in activities:
         ok = True
         for element in contraintList:
            if activite == element.getSecond() and element.getFirst() not in liste:
               ok = False
               break
         if ok:
            return activite
      return None
   def shedule(activities,contraintList,date):
      result = TopologicalSort.bruteForceSort(activities, contraintList)
      print('-------------ORDONNANCEMENT---------------------')
      if result is None:
         print("ordonancement impossible !")
      else:
         for element in result:
            print(element.getDescription())
         liste = collections.defaultdict(list)
         for element in result:
            liste[date] = element
            date += element.getDuration()
         return liste
   def afficheEmploi(activities,contraintList,date):
      emploiDuTemp = TopologicalSort.shedule(activities, contraintList, date)
      print('------------EMPLOI DU TEMPS----------------------')
      if emploiDuTemp is None:
         print("Emploi Impossible")
      else:
         print("DATE              DESCRIPTION                      DUREE ")
         for cle, valeur in emploiDuTemp.items():
            print(cle, "          ", valeur.getDescription(), "        ", valeur.getDuration())

if __name__=='__main__':
   #___________________ Case 1 _ Routine matinale_________________________________

   activite1 = Activity("se lever", 1)
   activite2 = Activity("aller au travail ", 15)
   activite3 = Activity("prendre une douche", 10)
   activite4 = Activity("se brosser les dents",3)
   activite5 = Activity("s'habiller ", 2)
   activite6 = Activity("prendre le p'tit dej ", 15)

   # activities est une liste d'activités (activite1,activite2,activite3...)
   activities = list([activite1, activite2, activite3, activite4, activite5,activite6])

   emploi1 = PrecedenceConstraint(activite1, activite6)
   emploi2 = PrecedenceConstraint(activite1, activite5)
   emploi3 = PrecedenceConstraint(activite6, activite4)
   emploi4 = PrecedenceConstraint(activite3, activite5)
   emploi5 = PrecedenceConstraint(activite4, activite2)
   emploi6 = PrecedenceConstraint(activite5, activite2)
   emploi7 = PrecedenceConstraint(activite1, activite3)
   emploi8 = PrecedenceConstraint(activite6, activite2)

   #contraintList est une liste de constraint (emploi1,emploi2,emploi3...)
   contraintList = list([emploi1, emploi2, emploi3,emploi4,emploi5,emploi6,emploi7])

   # Une fonction qui affcihe l'emploi du temps
   TopologicalSort.afficheEmploi(activities,contraintList,500)


   #_________________________ Case 2_ salle d'examen____________________________________

   activite1 = Activity("prendre connaissance du sujet", 30)
   activite2 = Activity("reviser ", 300)
   activite3 = Activity("Entrer dans la salle d'examen", 8)

   # activities est une liste d'activités (activite1,activite2,activite3)
   activities = list([activite1,activite2,activite3])

   emploi1 = PrecedenceConstraint(activite2, activite3)
   emploi2 = PrecedenceConstraint(activite3, activite1)
   emploi3 = PrecedenceConstraint(activite1, activite2)

   # contraintList est une liste de constraint (emploi1,emploi2,emploi3)
   contraintList = list([emploi1, emploi2, emploi3])

   # Une fonction qui affcihe l'emploi du temps
   TopologicalSort.afficheEmploi(activities,contraintList,500)



