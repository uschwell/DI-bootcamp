
import random

class Gene:
    thisGene=(-1)
    def __init__(self,gene):
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


    def __init__(self):
        #I will be generating the chromosomes randomly- if you wish to make it specific you can use the commented out constructor above
        #it is possible to generate a random "flip" here as well- but I see no point in repeating it-since we already generate it randomly 
        # AND generate each Gene with a random chance at mutation
        for i in range(10):
            temp=random.randint(0,1)

            temp2=Gene(temp)
            self.thisChromo.append(temp2)

    def mutateChromo(self, mutations):
        counter=0
        while(counter<mutations):
            #we pick a random gene in the chromosome
            pick=random.randint(0,9)
            #once we pick the gene-we have a 50/50 chance of it mutating
            if(random.randint(0,1)):
                self.thisChromo[pick].mutateGene()

            counter+=1



class DNA(Chromosome):
    myDNA=[]
    def __init__(self, chromo):
        self.myDNA=chromo

    def dnaAdd(self, chromo):
        (myDNA).append(chromo)

        def mutateDNA(self, mutations):
            counter=0
            #pick a random Chromosome to mutate
            picker=random.randint(0,(len(self.myDNA)-1))
            #there is a 50/50 chance that the chromosome will mutate at all
            if(random.randint(0, 1)):
                #we send the chromosome to go mutate (as defined by the earlier class)
                (self.myDNA[picker]).mutateChromo(mutations)


class Organism(DNA):
    def __init__(self, dna, environment):
        self.dna=dna
        self.environment=environment

    def lets_mutate(self):
        for chrom in self.dna:
            chrom.mutateDNA(self.environment)

#Note: I don't know if this is what you want- but each time I create a chromosome- I automatically generate 10 random genes
#if that is not what's wanted- switch to the commented out code in the Chromosome class

# chrom1=Chromosome()
# print("output")

# #print out the chromosome
# toPrint=(chrom1.thisChromo)
# for chrom in toPrint:
#     print(str(chrom.thisGene)+" ", end="")

# chrom1.mutateChromo(10)
# print("")

# #print out the mutated chromosome
# toPrint=(chrom1.thisChromo)
# for chrom in toPrint:
#     print(str(chrom.thisGene)+" ", end="")


#Note: I deliberatley did NOT automate this- wasn't sure what was required- this shows the other optional way
chrom1=Chromosome()
chrom2=Chromosome()
chrom3=Chromosome()
chrom4=Chromosome()
chrom5=Chromosome()
myDNA=DNA(chrom1)


# myDNA.dnaAdd(chrom2)
# myDNA.dnaAdd(chrom3)
# myDNA.dnaAdd(chrom4)
# myDNA.dnaAdd(chrom5)
#create an organism
org1=Organism(myDNA, 5)
flag=1
counter=0
while(flag):
    counter+=1
    org1.lets_mutate()
    for dn in org1:
        for chrom in dn:
            flag=10
            for gen in chrom:
                flag-=(gen.thisGene)
            if(flag==0):
                break

print("It took "+str(counter)+" generations")