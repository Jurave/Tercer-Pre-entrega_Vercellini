from django import forms

class UsuarioForm(forms.Form):
    nombre = forms.CharField(label="Nombre de usuario", max_length=50, required=True)
    email = forms.EmailField(label="Email", required=True)
    SEXO = (
        (1, "Femenino"),
        (2, "Masculino"),
        (3, "Prefiere no declarar"),
        )
    
    sexo = forms.ChoiceField(label="Sexo", choices=SEXO, required=True)

class CategoriaForm(forms.Form):
    nombre = forms.CharField(label = "Nombre de Posteo", max_length=50, required=True)
    redsocial= forms.CharField(label = "Nombre de Red Social", max_length=50, required=True)
    autorpublica = forms.CharField(label = "Autor", max_length=50, required=True)
    CATEGORIA = (
        (1, "Turismo"),
        (2, "Cocina"),
        (3, "Fitness"),
        (4, "Entretenimientos"),
        (5, "Kids"),
        (6, "Manualidades"),
        )

    categoria = forms.ChoiceField(label = "Categoría elegida", choices= CATEGORIA, required=True)


class PosteosForm(forms.Form):
    nombre = forms.CharField(label = "Nombre de Posteo", max_length=50, required=True)
    categoria = forms.CharField(label = "Nombre de la Categoría", max_length=50, required=True)
    redsocial = forms.CharField(label = "Red Social", max_length=50, required=50)
