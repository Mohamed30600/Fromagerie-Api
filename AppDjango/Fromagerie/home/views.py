from django.shortcuts import render
from django.http import HttpResponseRedirect
from apimanager.services.UtilisateurServices import getUsers, getUserFromLogin

def home(request):
    #Si la page home reçoit une requête http POST après qu'un utilisateur ait remplit formulaire de connexion :
    if request.method == 'POST':
        
        #Récupération des variables POST
        login = request.POST.get('login','')
        password = request.POST.get('password','')
        
        #Récupération d'un utilisateur via ses logs
        user = getUserFromLogin(login, password)
        
        #Si l'utilisateur existe
        if not user == None:
            #S'il est admin
            if user.isAdmin():
                #Instanciation de deux "cookie" django. On garde les identifiants stockés pour ne pas avoir à se reconnecter si on se rend plus tard sur la page.
                request.session['login'] = user.login
                request.session['password'] = user.pwd
                
                #Changement de vue
                return gestion(request)
            else:
                #Si l'utilisateur n'est pas admin, rendu de la page "login.html" avec le message d'erreur "Vous n'avez pas accès à cet outil"
                return render(request, template_name="login.html", context={
                'message' : "Vous n'avez pas accès à cet outil"
                })
        else:
            #Si les identifiants rentrés sont faux, rendu de la page "login.html" avec le message d'erreur "Login ou Mot de passe incorect"
            return render(request, template_name="login.html", context={
            'message' : "Login ou Mot de passe incorect"
            })
    
    #Si les "cookie" django sont déjà instanciés. 
    elif 'login' in request.session:
        #Récupération des identifiants dans les cookie
        login = request.session['login']
        password = request.session['password']
        
        #Récupération de l'utilisateur
        user = getUserFromLogin(login, password)
        
        #Vérification de son rôle
        if user.isAdmin():
            return gestion(request)
        else:
            return render(request, template_name="login.html")
        
    #Rendu par défaut
    else:
        return render(request, template_name="login.html")
    
def gestion(request):
    #Récupération de la liste des utlisateurs
    users = getUsers()
    
    #Rendu de la vue "gestion.html"
    return render(request, template_name="gestion.html", context={
        'users' : users
    })
    
#Vue appelée lors de la déconnexion
def logout(request):
    #suppression des cookie de connexion.
    if 'login' in request.session:
        del request.session['login']
        del request.session['password']
    #Redirection à la page home
    return HttpResponseRedirect('/home')
