from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

class CardAuthenticateBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        my_user_model = get_user_model()
        try:
            #Demande d'authentification et mot de passe de l'utilisateur
            print(username, password)
            user = my_user_model.objects.get(Q(username=username)|Q(cardid=username))
            print(user)
           
            if user.check_password(password):  #Si l'utuilisateur existe et que le mot de passe est valide, alors il est reconnu
                return user # return user on valid credentials
        except my_user_model.DoesNotExist: #Si l'utilisateur nexiste pas, on lui renvoie rien
            return None # return None if custom user model does not exist
        except: #Si aucun des cas en haut est reconnu, on lui renvoie rien
            return None # return None in case of other exceptions

    def get_user(self, user_id):
        my_user_model = get_user_model()
        try: #L'utilisateur est reconnu, il est identifié dans le système
            return my_user_model.objects.get(pk=user_id)
        except my_user_model.DoesNotExist: #Si l'utilisateur n'est pas reconnu, on lui renvoie rien
            return None
