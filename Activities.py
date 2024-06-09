class Activity:
    def __init__(self,description:str,time:int):
        self.description = description
        self.time = time
    def getDescription(self):
        return self.description
    def getDuration(self):
        return self.time
if __name__ == "__main__":
    description = input("Entrer une description : ")
    time = input("Entrer la duree : ")
    try:
        time = int(time)
        emploi= Activity(description,time)
        print("la description est :", emploi.getDescription())
        print("la duree est :",emploi.getDuration())
    except:
        print("veuillez respecter le type des variables")
    finally:
        print("FIN DU TEST !")

