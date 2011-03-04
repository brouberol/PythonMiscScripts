# Fonction decoratrice
# Permet de formater la sortie d'une fonction, quelque soit la fonction et son resultat

def return_result(fonction):
    def decorator(*args, **kwargs):
        resultat = fonction(*args, **kwargs)
        # *args : arguments de fonction d'entree, ex: (a,b)
        print "Appel de '{0}' avec parametres = {1} : resultat = {2}".format(fonction.__name__, args, resultat)
        return resultat    
    return decorator


@return_result
def addition(a,b):
    return a+b

@return_result
def multiplication(a,b):
    return a*b

@return_result
def Identity(name):
    name=name.capitalize()
    return name

addition(2,4)        
multiplication(2,4)
Identity("joe")

# a = 2 + addition(2,4)
# print a
# Ne fonctionne pas si on commente la ligne 'return resultat de la fonction decorator(*args, **kwargs)


