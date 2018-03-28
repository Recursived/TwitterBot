import tweepy
import time
import glob
import random 


#Variables globales 

dic = { 
    "consumer_key"        : "*****************************************",
    "consumer_secret"     : "*****************************************",
    "access_token"        : "************************************************",
    "access_token_secret" : "***********************************" 
    }

tweets = ["Vous souhaitez découvrir l'Ile de la Cité, n'attendez plus et venez la découvrir en cliquant sur le lien suivant : http://perso-etudiant.u-pem.fr/~mszeles/index.php?theme=0 #Paris #paris #Iledelacite #îledelacité",
          "Le berceau de Paris et ses monuments sur : http://perso-etudiant.u-pem.fr/~mszeles/index.php?theme=0 #Paris #paris #Iledelacite #îledelacité",
          "L'ile de la cité, un lieu INCONTOURNABLE à Paris : http://perso-etudiant.u-pem.fr/~mszeles/index.php?theme=0 #Paris #paris #Iledelacite #îledelacité",
          "Renseignez vous sur l'histoire de l'Ile de la Cité en visitant : http://perso-etudiant.u-pem.fr/~mszeles/index.php?theme=0 #Paris #paris #Iledelacite #îledelacité",
          "L'ile de la Cité à portée de main sur : http://perso-etudiant.u-pem.fr/~mszeles/index.php?theme=0 #Paris #Iledelacite #îledelacité",
          "Vous souhaitez avoir des informations sur les monuments de l'Ile de la Cité. Rendez-vous sur http://perso-etudiant.u-pem.fr/~mszeles/index.php?theme=0 #Paris #paris #Iledelacite #îledelacité ",
          "Venez vous amuser tout en apprenant sur : http://perso-etudiant.u-pem.fr/~mszeles/index.php?theme=0 #Paris #paris #Iledelacite #îledelacité",
          "Des informations utiles sur : http://perso-etudiant.u-pem.fr/~mszeles/index.php?theme=0 #Paris #paris #Iledelacite #îledelacité",
          "L'ile de la Cité accessible à tous et pour tous : http://perso-etudiant.u-pem.fr/~mszeles/index.php?theme=0 #Paris #paris #Iledelacite #îledelacité",
          "Venez vous informer sur la Mission Ile de la Cité --> un projet IMPORTANT : http://perso-etudiant.u-pem.fr/~mszeles/index.php?theme=0 #Paris #paris #Iledelacite #îledelacité"       
         ]

tweetsEN = ["Do you want to discover Ile de la Cité, don't wait and click on the link http://perso-etudiant.u-pem.fr/~mszeles/index.php?theme=0 #Paris #paris #Iledelacite #îledelacité",
           "The cradle of Paris and his monument on : http://perso-etudiant.u-pem.fr/~mszeles/index.php?theme=0 #Paris #paris #Iledelacite #îledelacité",
           "L'ile de la Cité, UNAVOIDABLE place in Paris : http://perso-etudiant.u-pem.fr/~mszeles/index.php?theme=0 #Paris #paris #Iledelacite #îledelacité",
           "Get informations on the history of Ile de la Cité : http://perso-etudiant.u-pem.fr/~mszeles/index.php?theme=0 #Paris #paris #Iledelacite #îledelacité",
           "L'ile de la Cité at your fingertips on http://perso-etudiant.u-pem.fr/~mszeles/index.php?theme=0 #Paris #paris #Iledelacite #îledelacité",
           "You want to get informations on the monuments of Ile de la Cité, visit : http://perso-etudiant.u-pem.fr/~mszeles/index.php?theme=0 #Paris #paris #Iledelacite #îledelacité",
           "Do you want to learn and play at the same time : http://perso-etudiant.u-pem.fr/~mszeles/index.php?theme=0 #Paris #paris #Iledelacite #îledelacité",
           "Get usefull information on : http://perso-etudiant.u-pem.fr/~mszeles/index.php?theme=0 #Paris #paris #Iledelacite #îledelacité",
           "L'ile de la Cité to all and for all : http://perso-etudiant.u-pem.fr/~mszeles/index.php?theme=0 #Paris #paris #Iledelacite #îledelacité",
           "Get informations on 'Mission Ile de la Cité : http://perso-etudiant.u-pem.fr/~mszeles/index.php?theme=0 #Paris #paris #Iledelacite #îledelacité"
]


#---------------------- Getting the path---------------------
path = "./img"+"/"+"*.jpg"
lst_jpg = glob.glob(path)
#On clean les paths
for i in range(len(lst_jpg)):
        lst_jpg[i] = lst_jpg[i].replace("\\",'/')
#-------------------------------------------






# Connection à l'api de twitter
def get_api(dic):
    print("connection to twitter")
    auth = tweepy.OAuthHandler(dic['consumer_key'], dic['consumer_secret'])
    auth.set_access_token(dic['access_token'], dic['access_token_secret'])
    print("connected")
    return tweepy.API(auth)

def main():
    i = 0
    j = 0
    twitter = get_api(dic)
    print(lst_jpg)
    while True:
        # Bot tweeting in french and english
        cinq = random.randint(1,7)
        if cinq == 5:
            twitter.update_with_media(lst_jpg[j], "site web/website: http://perso-etudiant.u-pem.fr/~mszeles/index.php?theme=0 #Paris #Iledelacite")
            if j > len(lst_jpg) - 1:
                j = 0
            j+=1
        else:
            print("tweeting in french")
            twitter.update_status(status=tweets[i])
            time.sleep(10)
            print("tweeting in english")
            twitter.update_status(status=tweetsEN[i])
            print("the Bot tweeted on the account and is now sleeping for 20m")
            i+=1
        if i > len(tweets)-1:
            i = 0
        time.sleep(60*20)





if __name__ == '__main__':
    main()
