from _typeshed import Self
import random

class Gene():
    thisGene = True

    def _init_(self,gene):
        #upon generation-there is a 50/50 chance the given value will 'mutate'
        #if we did mutate
        if(random.randint(0, 1)):
            if(gene==1):
                self.thisGene=0
            else:
                self.thisGene=1
        else:
            self.thisGene=gene

    def mutateGene(self):
        if(self.thisGene==1):
             self.thisGene=0
        else:
            self.thisGene=1



class Chromosome(Gene):
    thisChromo=[]

    # def _init_(self, gene0,gene1,gene2,gene3,gene4,gene5,gene6,gene7,gene8,gene9,):
    #     self.thisChromo=[gene0.thisGene,gene1.thisGene,gene2.thisGene,gene3.thisGene,gene4.thisGene,gene5.thisGene,
    #     gene6.thisGene,gene7.thisGene,gene8.thisGene,gene9.thisGene,]


    def _init_(self):
        #I will be generating the chromosomes randomly- if you wish to make it specific you can use the commented out constructor above
        #it is possible to generate a random "flip" here as well- but I see no point in repeating it-since we already generate it randomly 
        # AND generate each Gene with a random chance at mutation
        for i in range(10):
            temp=random.randint(0,1)
            temp2=Gene(temp)
            self.thisChromo.append(temp2)



class DNA():
    myDNA=[]
    def _init_(self, chromo):
        self.myDNA=chromo

    def dnaAdd(self, chromo):
        self.myDNA.append(chromo)