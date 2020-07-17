

class Contacts(forms.Contacts):
    class Meta:
        model = Contact
        fields = ['package','plan',]
        name = models.CharField(max_length=128)
        email = models.EmailField()
        subject = models.CharField(max_length=256)
        message = models.TextField()
        def str(self):
            return self.name
