from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUsuario

#CRIAÇÃO DO USUARIO
class CustomUsuarioCreateForm(UserCreationForm):

    class Meta:
        model = CustomUsuario
        fields = ('first_name', 'last_name', 'fone')
        labels = {'username':'Username/E-mail'}

    def save(self, commit=True):
        user = super(). save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.email = self.cleaned_data['username']
        if commit:
            user.save()
        return user


# ALTERAÇÃO DO USUARIO
class CustomUsuarioChangeForm(UserChangeForm):

    class Meta:
        model = CustomUsuario
        fields = ('first_name', 'last_name', 'fone')
