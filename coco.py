import argparse
import os
parser=argparse.ArgumentParser()
parser.add_argument("Team",help="Chose between Real Madrid ,Chelsea,PSG,Liverpool",type=str)
parser.add_argument("Formation",help="Chose the formation:433,4231,442,4212",type=int)
args=parser.parse_args()
#initialisation des pos et stats

gk = ["GK"]
defense= ["LB","CB","RB"]
midfielder= ["CDM","CM","CAM"]
attacker= ["RW","LW","ST"]

L=["Name","Pos","Foot","WF","SM","Attacking Average","Crossing","Finishing","Heading Accuracy","Short Passing","Volleys","Attacking Total","Skill Average","Dribbling","Curve","FK Accuracy","Long Passing","Ball Control","Skill Total","Movement Average","Acceleration","Sprint Speed","Agility","Reactions","Balance","Movement Total","Power Average","Shot Power","Jumping","Stamina","Strength","Long Shots","Power Total","Mentality Average","Aggression","Interceptions","Positioning","Vision","Penalties","Composure","Mentality Total","Defending Average","Marking","Standing Tackle","Sliding Tackle","Defending Total","Goalkeeping Average","GK Diving","GK Handling","GK Kicking","GK Positioning","GK Reflexes","Goalkeeping Total"]
i=0
d={}
while i<len(L):   #on a creer un dictionnaire contenant le nom de chaque attribut avec son i dans la liste L
        d[L[i]]=i
        i=i+1






#creation d'une liste de liste , equipe=[joueur , joueur2...] et joueur est une liste
equipe=[]
os.chdir("C:\\Users\\elias\\Desktop\\Project\\PSG")

with open (f"{args.Team}.txt") as f :

        liste= f.readlines()  #chaque ligne du texte file est en element de liste
        for element in liste:
                joueur=element.split(",")
                equipe.append(joueur)


#definir la Pos2 de chaque joueur
for joueur in equipe:
        if joueur[1]=="GK":
                joueur.append("gk")
        elif joueur[1]=="LB" or joueur[1]=="CB" or joueur[1]=="RB":
                joueur.append("defense")
        elif joueur[1]=="CDM" or joueur[1]=="CM" or joueur[1]=="CAM":
                joueur.append("midfielder")
        elif joueur[1]=="RW" or joueur[1]=="LW" or joueur[1]=="ST":
                joueur.append("attacker")

#definir les fonctions permettant de determiner le meilleur joueur dans chaque position
#il faut d'abord ecrire une fonction qui renvoie le nom du joueur possedant le meilleur total
finalteam={}
def bestname(choix,Pos):
        for name in choix.keys():
                for names in finalteam.values():
                        if names==name:
                                choix[name]-=9999999999999

        i=0
        if Pos in finalteam.keys():
                i=i+1
                if i!=0:
                        Pos2=Pos+str(i)
                total=1
                for val in choix.values():  #la premiere boucle sert a determiner le meilleur total et la deuxime sert a trouver le nom du meilleur
                        if val>total:
                                total=val
                        for namebest,valtotal in choix.items():
                                if valtotal==total:
                                        finalteam[Pos2]=namebest
        else:
                total=0
                for val in choix.values():  #la premiere boucle sert a determiner le meilleur total et la deuxime sert a trouver le nom du meilleur
                        if val>total:
                                total=val
                for namebest,valtotal in choix.items():
                        if valtotal==total:
                                finalteam[Pos]=namebest



def GK(equipe):   #parcour l equipe, donne un dictinnaire donnant les diff choix avec le total de chaqu un puis utilise une fonction pour donner le nom de ce meilleur
        choix={}
        for joueur in equipe:
                if joueur[-1]=="gk":
                        total=int(joueur[d["Goalkeeping Total"]])
                        name=joueur[d["Name"]]
                        choix[name]=total


        bestname(choix,"GK")
        return finalteam


def LB(equipe):
        choix={}
        for joueur in equipe:
                if joueur[d["Pos"]]=="LB":
                        total=int(joueur[d["Crossing"]])*2+int(joueur[d["Short Passing"]])*2+int(joueur[d["Dribbling"]])*2+int(joueur[d["Long Passing"]])*2+int(joueur[d["Ball Control"]])*2+int(joueur[d["Acceleration"]])*4+int(joueur[d["Sprint Speed"]])*4;
                        total+=int(joueur[d["Agility"]])*2+int(joueur[d["Reactions"]])*2+int(joueur[d["Balance"]])*2+int(joueur[d["Stamina"]])*3+int(joueur[d["Strength"]])*4+int(joueur[d["Aggression"]])*4+int(joueur[d["Interceptions"]])*4+int(joueur[d["Positioning"]])*2;
                        total+=int(joueur[d["Composure"]])+int(joueur[d["Marking"]])*4+int(joueur[d["Standing Tackle"]])*4+int(joueur[d["Sliding Tackle"]])*4+int(joueur[d["Jumping"]])*3+int(joueur[d["Heading Accuracy"]])*3
                        name=joueur[d["Name"]]

                        if joueur[d["Foot"]]=="L":
                                total=total+100

                        if int(joueur[d["WF"]])==4:
                                total=total+10

                        if int(joueur[d["SM"]])==4:
                                total=total+10

                        if int(joueur[d["WF"]])==5:
                                total=total+40

                        if int(joueur[d["SM"]])==5:
                                total=total+40

                        choix[name]=total
        bestname(choix,"LB")
        return finalteam


def RB(equipe):
        choix={}
        for joueur in equipe:
                if joueur[d["Pos"]]=="RB":
                        total=int(joueur[d["Crossing"]])*2+int(joueur[d["Short Passing"]])*2+int(joueur[d["Dribbling"]])*2+int(joueur[d["Long Passing"]])*2+int(joueur[d["Ball Control"]])*2+int(joueur[d["Acceleration"]])*4+int(joueur[d["Sprint Speed"]])*4;
                        total+=int(joueur[d["Agility"]])*2+int(joueur[d["Reactions"]])*2+int(joueur[d["Balance"]])*2+int(joueur[d["Stamina"]])*3+int(joueur[d["Strength"]])*4+int(joueur[d["Aggression"]])*4+int(joueur[d["Interceptions"]])*4+int(joueur[d["Positioning"]])*2;
                        total+=int(joueur[d["Composure"]])+int(joueur[d["Marking"]])*4+int(joueur[d["Standing Tackle"]])*4+int(joueur[d["Sliding Tackle"]])*4+int(joueur[d["Jumping"]])*3+int(joueur[d["Heading Accuracy"]])*3
                        name=joueur[d["Name"]]

                        if joueur[d["Foot"]]=="R":
                                total=total+100

                        if int(joueur[d["WF"]])==4:
                                total=total+10

                        if int(joueur[d["SM"]])==4:
                                total=total+10

                        if int(joueur[d["WF"]])==5:
                                total=total+40

                        if int(joueur[d["SM"]])==5:
                                total=total+40

                        choix[name]=total
        bestname(choix,"RB")
        return finalteam


def CB(equipe):
        choix={}
        for joueur in equipe:
                if joueur [d["Pos"]]=="CB":

                        total=int(joueur[d["Heading Accuracy"]])*3+int(joueur[d["Short Passing"]])+int(joueur[d["Dribbling"]])+int(joueur[d["Long Passing"]])+int(joueur[d["Acceleration"]])*4+int(joueur[d["Sprint Speed"]])*4;
                        total+=int(joueur[d["Agility"]])+int(joueur[d["Reactions"]])+int(joueur[d["Balance"]])+int(joueur[d["Jumping"]])*3+int(joueur[d["Stamina"]])*2+int(joueur[d["Strength"]])*4+int(joueur[d["Aggression"]])*4;
                        total+=int(joueur[d["Interceptions"]])*4+int(joueur[d["Composure"]])+int(joueur[d["Marking"]])*4+int(joueur[d["Standing Tackle"]])*4+int(joueur[d["Sliding Tackle"]])*4
                        name=joueur[d["Name"]]


                        if int(joueur[d["WF"]])==4:
                                total=total+20

                        if int(joueur[d["SM"]])==4:
                                total=total+20

                        if int(joueur[d["WF"]])==5:
                                total=total+30

                        if int(joueur[d["SM"]])==5:
                                total=total+30

                        if (int(joueur[d["Acceleration"]])+int(joueur[d["Sprint Speed"]]))/2>=74:
                                total=total+100
                        if (int(joueur[d["Acceleration"]])+int(joueur[d["Sprint Speed"]]))/2>=80:
                                total=total+100

                        if (int(joueur[d["Acceleration"]])+int(joueur[d["Sprint Speed"]]))/2>=85:
                                total=total+100

                        if (int(joueur[d["Acceleration"]])+int(joueur[d["Sprint Speed"]]))/2<=60:
                                total=total-101



                        choix[name]=total
        bestname(choix,"CB")
        return finalteam



def CAM(equipe):
        choix={}
        for joueur in equipe:
                if joueur [-1]=="midfielder" or joueur [-1]=="attacker" :

                        total=int(joueur[d["Crossing"]])*2+int(joueur[d["Finishing"]])*3+int(joueur[d["Short Passing"]])*4+int(joueur[d["Volleys"]])*3+int(joueur[d["Dribbling"]])*4+int(joueur[d["Curve"]])*3;
                        total=+int(joueur[d["Long Passing"]])*4+int(joueur[d["Ball Control"]])*4+int(joueur[d["Acceleration"]])*3+int(joueur[d["Sprint Speed"]])*3+int(joueur[d["Agility"]])*4+int(joueur[d["Reactions"]])*3;
                        total=+int(joueur[d["Balance"]])*4+int(joueur[d["Shot Power"]])*2+int(joueur[d["Long Shots"]])*3+int(joueur[d["Stamina"]])*3+int(joueur[d["Positioning"]])*3+int(joueur[d["Vision"]])*4+int(joueur[d["Composure"]])*3
                        name=joueur[d["Name"]]
                        if int(joueur[d["WF"]])==4:
                                total=total+50

                        if int(joueur[d["SM"]])==4:
                                total=total+50

                        if int(joueur[d["WF"]])==5:
                                total=total+150

                        if int(joueur[d["SM"]])==5:
                                total=total+100
                        if int(joueur[d["SM"]])<4:
                                total=total-200
                        if int(joueur[d["WF"]])<4:
                                total=total-200
                        if (int(joueur[d["Acceleration"]])+int(joueur[d["Sprint Speed"]]))/2 <80:
                                total=total-100
                        if (int(joueur[d["Acceleration"]])+int(joueur[d["Sprint Speed"]]))/2>=84:
                                total=total+100
                        if (int(joueur[d["Acceleration"]])+int(joueur[d["Sprint Speed"]]))/2>=90:
                                total=total+50

                        if (int(joueur[d["Acceleration"]])+int(joueur[d["Sprint Speed"]]))/2>=95:
                                total=total+100

                        if (int(joueur[d["Acceleration"]])+int(joueur[d["Sprint Speed"]]))/2<=80:
                                total=total-101
                        choix[name]=total
        bestname(choix,"CAM")
        return finalteam

def ST(equipe):
        choix={}
        for joueur in equipe:
                        if joueur[d["Pos"]]=="CAM" or joueur[-1]=="attacker" :
                                        total=int(joueur[d["Heading Accuracy"]])*3+int(joueur[d["Finishing"]])*4+int(joueur[d["Short Passing"]])*2+int(joueur[d["Volleys"]])*4+int(joueur[d["Dribbling"]])*3+int(joueur[d["Curve"]])*3;
                                        total=+int(joueur[d["Long Passing"]])*2+int(joueur[d["Ball Control"]])*3+int(joueur[d["Acceleration"]])*4+int(joueur[d["Sprint Speed"]])*4+int(joueur[d["Agility"]])*3+int(joueur[d["Reactions"]])*2;
                                        total=+int(joueur[d["Balance"]])*3+int(joueur[d["Shot Power"]])*4+int(joueur[d["Long Shots"]])*4+int(joueur[d["Stamina"]])*3+int(joueur[d["Positioning"]])*4+int(joueur[d["Vision"]])*2+int(joueur[d["Composure"]])*4
                                        total=+int(joueur[d["Jumping"]])*4+int(joueur[d["Strength"]])*4+int(joueur[d["Aggression"]])*4
                                        name=joueur[d["Name"]]
                                        if (int(joueur[d["Finishing"]])+int(joueur[d["Long Shots"]])+int(joueur[d["Shot Power"]]))/3<=80:
                                                total=total-300
                                        if int(joueur[d["WF"]])==4:
                                                total=total+50
                                        if int(joueur[d["SM"]])==4:
                                                total=total+50
                                        if int(joueur[d["WF"]])==5:
                                                total=total+150
                                        if int(joueur[d["SM"]])==5:
                                                total=total+150
                                        if int(joueur[d["SM"]])<4:
                                                total=total-100
                                        if int(joueur[d["WF"]])<4:
                                                total=total-100
                                        if (int(joueur[d["Acceleration"]])+int(joueur[d["Sprint Speed"]]))/2 <86:
                                                total=total-100
                                        if (int(joueur[d["Acceleration"]])+int(joueur[d["Sprint Speed"]]))/2>=87:
                                                total=total+100
                                        if (int(joueur[d["Acceleration"]])+int(joueur[d["Sprint Speed"]]))/2>=93:
                                                total=total+50
                                        if (int(joueur[d["Acceleration"]])+int(joueur[d["Sprint Speed"]]))/2>=95:
                                                total=total+100
                                        if (int(joueur[d["Acceleration"]])+int(joueur[d["Sprint Speed"]]))/2<=80:
                                                total=total-200
                                        choix[name]=total

        bestname(choix,"ST")
        return finalteam

def CM(equipe):
        choix={}
        for joueur in equipe:
                if joueur[-1]=="midfielder":
                        total=int(joueur[d["Crossing"]])*3+int(joueur[d["Short Passing"]])*4+int(joueur[d["Volleys"]])+int(joueur[d["Dribbling"]])*3+int(joueur[d["Curve"]])*2;
                        total=+int(joueur[d["Long Passing"]])*4+int(joueur[d["Ball Control"]])*3+int(joueur[d["Acceleration"]])*4+int(joueur[d["Sprint Speed"]])*4+int(joueur[d["Agility"]])*3+int(joueur[d["Reactions"]])*2;
                        total=+int(joueur[d["Balance"]])*3+int(joueur[d["Shot Power"]])*2+int(joueur[d["Long Shots"]])*3+int(joueur[d["Stamina"]])*4+int(joueur[d["Vision"]])*4+int(joueur[d["Composure"]])*3
                        total=+int(joueur[d["Jumping"]])+int(joueur[d["Strength"]])*2+int(joueur[d["Aggression"]])*3+int(joueur[d["Vision"]])*4+int(joueur[d["Interceptions"]])*3+int(joueur[d["Marking"]])*2+int(joueur[d["Standing Tackle"]])*3
                        total+=int(joueur[d["Sliding Tackle"]])
                        name=joueur[d["Name"]]
                        if int(joueur[d["WF"]])==4:
                                total=total+50
                        if int(joueur[d["SM"]])==4:
                                total=total+50
                        if int(joueur[d["WF"]])==5:
                                total=total+100
                        if int(joueur[d["SM"]])==5:
                                total=total+100
                        if int(joueur[d["SM"]])<4:
                                total=total-50
                        if int(joueur[d["WF"]])<4:
                                total=total-100
                        if (int(joueur[d["Acceleration"]])+int(joueur[d["Sprint Speed"]]))/2 <70:
                                total=total-200
                        if (int(joueur[d["Acceleration"]])+int(joueur[d["Sprint Speed"]]))/2>=75:
                                total=total+100
                        if (int(joueur[d["Acceleration"]])+int(joueur[d["Sprint Speed"]]))/2>=83:
                                total=total+100

                        if (int(joueur[d["Acceleration"]])+int(joueur[d["Sprint Speed"]]))/2>=89:
                                total=total+100
                        if (int(joueur[d["Sliding Tackle"]])+int(joueur[d["Standing Tackle"]])+int(joueur[d["Interceptions"]]))/3<=70:
                                total=total-100
                        if (int(joueur[d["Short Passing"]])+int(joueur[d["Long Passing"]])+int(joueur[d["Vision"]]))/3<=85:
                                total=total-100
                        if (int(joueur[d["Short Passing"]])+int(joueur[d["Long Passing"]])+int(joueur[d["Vision"]]))/3>85:
                                total=total+50
                        choix[name]=total
        bestname(choix,"CM")
        return finalteam


def CDM(equipe):
        choix={}
        for joueur in equipe:
                if joueur[-1]=="midfielder":
                        total=int(joueur[d["Short Passing"]])+int(joueur[d["Dribbling"]]);
                        total=+int(joueur[d["Long Passing"]])+int(joueur[d["Ball Control"]])*2+int(joueur[d["Acceleration"]])*4+int(joueur[d["Sprint Speed"]])*4+int(joueur[d["Agility"]])*2+int(joueur[d["Reactions"]])*2;
                        total=+int(joueur[d["Balance"]])*2+int(joueur[d["Shot Power"]])+int(joueur[d["Long Shots"]])+int(joueur[d["Stamina"]])*4+int(joueur[d["Vision"]])+int(joueur[d["Composure"]])
                        total=+int(joueur[d["Jumping"]])*4+int(joueur[d["Strength"]])*4+int(joueur[d["Aggression"]])*4+int(joueur[d["Interceptions"]])*5+int(joueur[d["Marking"]])*4+int(joueur[d["Standing Tackle"]])*4
                        total+=int(joueur[d["Sliding Tackle"]])*4
                        name=joueur[d["Name"]]
                        if int(joueur[d["WF"]])==4:
                                total=total+50
                        if int(joueur[d["SM"]])==4:
                                total=total+50
                        if int(joueur[d["WF"]])==5:
                                total=total+100
                        if int(joueur[d["SM"]])==5:
                                total=total+100
                        if int(joueur[d["SM"]])<4:
                                total=total-25
                        if int(joueur[d["WF"]])<4:
                                total=total-25
                        if (int(joueur[d["Acceleration"]])+int(joueur[d["Sprint Speed"]]))/2 <70:
                                total=total-200
                        if (int(joueur[d["Acceleration"]])+int(joueur[d["Sprint Speed"]]))/2>=75:
                                total=total+100
                        if (int(joueur[d["Acceleration"]])+int(joueur[d["Sprint Speed"]]))/2>=83:
                                total=total+200
                        if (int(joueur[d["Acceleration"]])+int(joueur[d["Sprint Speed"]]))/2>=89:
                                total=total+100
                        if (int(joueur[d["Sliding Tackle"]])+int(joueur[d["Standing Tackle"]])+int(joueur[d["Interceptions"]])+int(joueur[d["Strength"]])+int(joueur[d["Aggression"]]))/5<75:
                                total=total-300
                        if (int(joueur[d["Sliding Tackle"]])+int(joueur[d["Standing Tackle"]])+int(joueur[d["Interceptions"]])+int(joueur[d["Strength"]])+int(joueur[d["Aggression"]]))/5<80:
                                total=total-150
                        if (int(joueur[d["Sliding Tackle"]])+int(joueur[d["Standing Tackle"]])+int(joueur[d["Interceptions"]])+int(joueur[d["Strength"]])+int(joueur[d["Aggression"]]))/5>=80:
                                total=total+200
                        if (int(joueur[d["Sliding Tackle"]])+int(joueur[d["Standing Tackle"]])+int(joueur[d["Interceptions"]])+int(joueur[d["Strength"]])+int(joueur[d["Aggression"]]))/5>85:
                                total=total+100

                        choix[name]=total
        bestname(choix,"CDM")
        return finalteam

def RW(equipe):
        choix={}
        for joueur in equipe:
                if joueur[d["Pos"]]=="CAM" or joueur [-1]=="attacker" :
                        total=int(joueur[d["Finishing"]])*2+int(joueur[d["Short Passing"]])*2+int(joueur[d["Volleys"]])*3+int(joueur[d["Dribbling"]])*5+int(joueur[d["Curve"]])*1;
                        total=+int(joueur[d["Long Passing"]])*3+int(joueur[d["Ball Control"]])*5+int(joueur[d["Acceleration"]])*5+int(joueur[d["Sprint Speed"]])*5+int(joueur[d["Agility"]])*5+int(joueur[d["Reactions"]]);
                        total=+int(joueur[d["Balance"]])*4+int(joueur[d["Shot Power"]])*2+int(joueur[d["Long Shots"]])*2+int(joueur[d["Stamina"]])*2+int(joueur[d["Positioning"]])*2+int(joueur[d["Vision"]])*3+int(joueur[d["Composure"]])*2
                        name=joueur[d["Name"]]
                        if joueur[d["Foot"]]=="L" and int(joueur[d["WF"]])!=5:
                            total=total+150
                        if int(joueur[d["WF"]])==4:
                                total=total+50
                        if int(joueur[d["SM"]])==4:
                                total=total+50

                        if int(joueur[d["WF"]])==5:
                                total=total+150

                        if int(joueur[d["SM"]])==5:
                                total=total+50
                        if int(joueur[d["SM"]])<4:
                                total=total-200
                        if int(joueur[d["WF"]])<4:
                                total=total-100
                        if (int(joueur[d["Acceleration"]])+int(joueur[d["Sprint Speed"]]))/2 <80:
                                total=total-400
                        if (int(joueur[d["Acceleration"]])+int(joueur[d["Sprint Speed"]]))/2 <86:
                                total=total-100
                        if (int(joueur[d["Acceleration"]])+int(joueur[d["Sprint Speed"]]))/2>=87:
                                total=total+100
                        if (int(joueur[d["Acceleration"]])+int(joueur[d["Sprint Speed"]]))/2>=93:
                                total=total+200
                        choix[name]=total

        bestname(choix,"RW")
        return finalteam
def LW(equipe):
        choix={}
        for joueur in equipe:
                if joueur[d["Pos"]]=="CAM" or joueur [-1]=="attacker" :
                        total=int(joueur[d["Finishing"]])*2+int(joueur[d["Short Passing"]])*2+int(joueur[d["Volleys"]])*3+int(joueur[d["Dribbling"]])*5+int(joueur[d["Curve"]])*1;
                        total=+int(joueur[d["Long Passing"]])*3+int(joueur[d["Ball Control"]])*5+int(joueur[d["Acceleration"]])*5+int(joueur[d["Sprint Speed"]])*5+int(joueur[d["Agility"]])*5+int(joueur[d["Reactions"]]);
                        total=+int(joueur[d["Balance"]])*4+int(joueur[d["Shot Power"]])*2+int(joueur[d["Long Shots"]])*2+int(joueur[d["Stamina"]])*2+int(joueur[d["Positioning"]])*2+int(joueur[d["Vision"]])*3+int(joueur[d["Composure"]])*2
                        name=joueur[d["Name"]]
                        if joueur[d["Foot"]]=="R" and int(joueur[d["WF"]])!=5:
                                total=total+150
                        if int(joueur[d["WF"]])==4:
                                total=total+50
                        if int(joueur[d["SM"]])==4:
                                total=total+50

                        if int(joueur[d["WF"]])==5:
                                total=total+150

                        if int(joueur[d["SM"]])==5:
                                total=total+50
                        if int(joueur[d["SM"]])<4:
                                total=total-200
                        if int(joueur[d["WF"]])<4:
                                total=total-100
                        if (int(joueur[d["Acceleration"]])+int(joueur[d["Sprint Speed"]]))/2 <80:
                                total=total-400
                        if (int(joueur[d["Acceleration"]])+int(joueur[d["Sprint Speed"]]))/2 <86:
                                total=total-100
                        if (int(joueur[d["Acceleration"]])+int(joueur[d["Sprint Speed"]]))/2>=87:
                                total=total+100
                        if (int(joueur[d["Acceleration"]])+int(joueur[d["Sprint Speed"]]))/2>=93:
                                total=total+200
                        choix[name]=total
        bestname(choix,"LW")
        return finalteam

if args.Formation==4231:
        ST(equipe)
        LW(equipe)
        CAM(equipe)
        RW(equipe)
        CDM(equipe)
        CDM(equipe)
        CB(equipe)
        CB(equipe)
        LB(equipe)
        RB(equipe)
        GK(equipe)
        print(finalteam)


if args.Formation==433:
        ST(equipe)
        LW(equipe)
        CAM(equipe)
        RW(equipe)
        CM(equipe)
        CM(equipe)
        LB(equipe)
        CB(equipe)
        CB(equipe)
        RB(equipe)
        GK(equipe)
        print(finalteam)

if args.Formation==442:
        ST(equipe)
        ST(equipe)
        RW(equipe)
        CDM(equipe)
        CDM(equipe)
        LW(equipe)
        LB(equipe)
        CB(equipe)
        CB(equipe)
        RB(equipe)
        GK(equipe)
        print(finalteam)

if args.Formation==41212:
        ST(equipe)
        ST(equipe)
        RW(equipe)
        CAM(equipe)
        LW(equipe)
        CDM(equipe)
        RB(equipe)
        CB(equipe)
        CB(equipe)
        LB(equipe)
        GK(equipe)
        print(finalteam)









