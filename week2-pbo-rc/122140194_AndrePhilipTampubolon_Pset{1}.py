import random 

class Father:
    def __init__(self, bloodType):
        self.bloodType = bloodType
    
    def get_allele_from_father(self):
        self.bloodType = list(self.bloodType)
        fatherAlleleSelected = random.choice(self.bloodType)
        
        return fatherAlleleSelected
    
class Mother:
    def __init__(self, bloodType):
        self.bloodType = bloodType
    
    def get_allele_from_mother(self):
        self.bloodType = list(self.bloodType)
        motherAlleleSelected = random.choice(self.bloodType)
        
        return motherAlleleSelected
        
class Child(Father, Mother):
    def __init__(self, father, mother):
        self.father = father
        self.mother = mother
        
    def get_child_allele(self):
        father_allele = self.father.get_allele_from_father()
        mother_allele = self.mother.get_allele_from_mother()
        
        self.child_allele = father_allele + mother_allele
        print(f"Child's Allele: {self.child_allele}")
        
    def get_child_bloodType(self):
        possible_bloodType = {'AA' : 'A', 'AO' : 'A', 'AB' : 'AB', 'BB' : 'B', 'BO' : 'B', 'OO' : 'O'}
        
        print(f"Child's blood type : {possible_bloodType.get(self.child_allele, 'Unknown')}")
    

if __name__ == "__main__":
    
    fatherAllele = input("Enter the father's allele: ").upper()
    motherAllele = input("Enter the mother's allele: ").upper()
    
    father = Father(fatherAllele)
    mother = Mother(motherAllele)
    child = Child(father, mother)
    child.get_child_allele()
    child.get_child_bloodType()
