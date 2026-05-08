class Profile:
    def __init__(self,name,email,language):
        self.name=name
        self.email=email
        self.language=language
first_profile= Profile("eman","emanmostafa@888.com","python")
second_profile= Profile("safa","safasaad@977.com","english")
third_profile= Profile("aya","ayamohamed@444.com","java")
print(f"the first profile name is:{first_profile.name}")
print(f"the third profile language is:{third_profile.email}")


class Message:
     def __init__(self,name_s,name_r,contant,data):
         self.name_s=name_s
         self.name_r=name_r
         self.contant=contant
         self.data=data
pess=Message("mohamed","eslam","hello eslam",'12/3/1016')
dess=Message("sara","shahd","i love you shahd",'27/1/2026')
ress=Message("sama","mona"," i miss you so much",'23/1/2026')
print(ress.name_s)
print(pess.contant)
print(dess.data)

