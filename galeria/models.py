from django.db import models

#Classe banco de dados models 
#python manage.py makemigrations
#python manage.py migrate

class Fotografia(models.Model):
    nome = models.CharField(max_length= 50, null= False, blank= False)   #Campo de caracteres
    legenda = models.CharField(max_length=150, null= False, blank= False)  #Campo de caracteres
    descricao = models.TextField(null=False, blank=False)     #Campo de texto
    foto = models.CharField(max_length=50, blank= False, null= False) # nome da foto


#nome do objeto no terminal
    def __str__(self):
        return f"Fotografia [nome={self.nome}]"
