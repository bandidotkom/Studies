# 6.00 Problem Set 12
#
# Name:
# Collaborators:
# Time:

import numpy
import random
import pylab

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """    

#
# PROBLEM 1
#

class SimpleVirus(object):
    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        
        clearProb: Maximum clearance probability (a float between 0-1).
        """
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb
        
    def doesClear(self):
        """
        Stochastically determines whether this virus is cleared from the
        patient's body at a time step. 

        returns: Using a random number generator (random.random()), this method
        returns True with probability self.clearProb and otherwise returns
        False.
        """
        r = random.random()
        if r <= self.clearProb:
            return True
        else: return False
    
    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the SimplePatient and
        Patient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """
        r = random.random()
        if r <= self.maxBirthProb * (1 - popDensity):
            return SimpleVirus(self.maxBirthProb, self.clearProb)
        else: raise NoChildException("no child")

class SimplePatient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """
    
    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)
        
        maxPop: the  maximum virus population for this patient (an integer)
        """
        self.viruses = viruses
        self.maxPop = maxPop

    def getTotalPop(self):
        """
        Gets the current total virus population. 

        returns: The total virus population (an integer)
        """
        return len(self.viruses)        

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:

        - Determine whether each virus particle survives and update the list
          of virus particles accordingly.

        - The current population density is calculated. This population density
          value is used until the next call to update() 

        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient.                    

        returns: the total virus population at the end of the update (an
        integer)
        """
        res = []
        for virus in self.viruses:
            if not virus.doesClear():
                res.append(virus)
        self.viruses = res
        popDensity = float(len(res)/(self.maxPop))
        for v in res:
            try:
                repro = v.reproduce(popDensity)
                self.viruses.append(repro)
            except:
                continue
        return len(self.viruses)
                

#
# PROBLEM 2
#

def problem2():
    """
    Run the simulation and plot the graph for problem 2 (no drugs are used,
    viruses do not have any drug resistance).    

    Instantiates a patient, runs a simulation for 300 timesteps, and plots the
    total virus population as a function of time.    
    """
    viruses = []
    for i in range(99):
        maxBirthProb = 0.1
        clearProb = 0.05
        viruses.append(SimpleVirus(maxBirthProb, clearProb))
    sp = SimplePatient(viruses, 1000)
    res = []
    for j in range(299):
        res.append(sp.update())
    pylab.plot(res)
    pylab.ylabel('population')
    pylab.xlabel('timesteps')
    pylab.title('Virus population')
    pylab.show()

#problem2()   
#
# PROBLEM 3
#

class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """    
    
    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.
        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        
        clearProb: Maximum clearance probability (a float between 0-1).
        
        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'grimpex':False}, means that this virus
        particle is resistant to neither guttagonol nor grimpex.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.        
        """
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb
        self.resistances = resistances
        self.mutProb = mutProb
        
    def getResistance(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in Patient to determine how many virus
        particles have resistance to a drug.        

        drug: the drug (a string).

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        if drug not in self.resistances.keys():
            return True
        else: return self.resistances[drug]
        
    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient class.

        If the virus particle is not resistant to any drug in activeDrugs,
        then it does not reproduce. Otherwise, the virus particle reproduces
        with probability:       
        
        self.maxBirthProb * (1 - popDensity).                       
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). 

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.        

        For example, if a virus particle is resistant to guttagonol but not
        grimpex, and `self.mutProb` is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90% 
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        grimpex and a 90% chance that the offspring will not be resistant to
        grimpex.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population        

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings). 
        
        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.         
        """
        resistant=True
        if activeDrugs == []:
            resistant=True
        else:
            for drug in activeDrugs:
                if not self.getResistance(drug):
                    resistant = False
        if resistant:
            r1 = random.random()
            if r1 <= self.maxBirthProb*(1 - popDensity):
                r2 = random.random()
                newresistances = {}
                for resistance in self.resistances.keys():
                    if r2 <= 1-self.mutProb:
                        newresistances[resistance] = self.resistances[resistance]
                    else:
                        newresistances[resistance] = not(self.resistances[resistance])
                return ResistantVirus(self.maxBirthProb, self.clearProb, newresistances, self.mutProb)
            else:
                raise NoChildException("no child")
        else:
            raise NoChildException("no child")
    
            
class Patient(SimplePatient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """
    
    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).               

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)
        
        maxPop: the  maximum virus population for this patient (an integer)
        """
        self.viruses = viruses
        self.maxPop = maxPop
        self.drugsList = []
        
    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the 
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: list of drugs being administered to a patient is updated
        """
        self.drugsList.append(newDrug)

    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """
        return self.drugsList
        
    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in 
        drugResist.        

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'grimpex'])

        returns: the population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        ctr += 0
        for virus in self.viruses:
            for drug in drugResist:
                if not virus.getResistance(drug):
                    break
                else:
                    ctr += 1
        return ctr          

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of 
          virus particles accordingly
          
        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient. 
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces. 

        returns: the total virus population at the end of the update (an
        integer)
        """
        res = []
        for virus in self.viruses:
            if not virus.doesClear():
                res.append(virus)
        self.viruses = res
        popDensity = float(len(res)/(self.maxPop))
        for v in res:
            try:
                repro = v.reproduce(popDensity, self.drugsList)
                self.viruses.append(repro)
            except:
                continue
        return len(self.viruses)

#
# PROBLEM 4
#

def problem4():
    """
    Runs simulations and plots graphs for problem 4.

    Instantiates a patient, runs a simulation for 150 timesteps, adds
    guttagonol, and runs the simulation for an additional 150 timesteps.

    total virus population vs. time  and guttagonol-resistant virus population
    vs. time are plotted
    """
    viruses = []
    for i in range(99):
        maxBirthProb = 0.1
        clearProb = 0.05
        resistances = {'guttagonol':False}
        mutProb = 0.005
        viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
    p = Patient(viruses, 1000)
    res = []
    for j in range(150):
        res.append(p.update())

    p2 = Patient(viruses, 1000)
    p2.addPrescription('guttagonol')
    res2 = []
    for j in range(150):
        res2.append(p2.update())
    pylab.plot(res, label="without treatment")
    pylab.plot(res2, label="with treatment")
    pylab.legend(loc='upper left')
    pylab.ylabel('population')
    pylab.xlabel('timesteps')
    pylab.title('Virus population')
    pylab.show()
#problem4()

#
# PROBLEM 5
#
        
def problem5():
    """
    Runs simulations and make histograms for problem 5.

    Runs multiple simulations to show the relationship between delayed treatment
    and patient outcome.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).    
    """
    viruses = []
    for i in range(99):
        maxBirthProb = 0.1
        clearProb = 0.05
        resistances = {'guttagonol':False, 'grimpex':False}
        mutProb = 0.005
        viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
    p = Patient(viruses, 1000)
    finres = []
    for i in range(29):
        res = []
        for j in range(149):
            res.append(p.update())
        p.addPrescription('guttagonol')
        for j in range(149):
            res.append(p.update())
        finres.append(len(res))
    pylab.hist(finres)
    pylab.show()
    p2 = Patient(viruses, 1000)
    finres = []
    for i in range(29):
        res = []
        for j in range(149):
            res.append(p2.update())
        p.addPrescription('guttagonol')
        for j in range(149):
            res.append(p2.update())
        finres.append(len(res))
    pylab.hist(finres)
    pylab.show()
#problem5()
    
#
# PROBLEM 6
#

def problem6():
    """
    Runs simulations and make histograms for problem 6.

    Runs multiple simulations to show the relationship between administration
    of multiple drugs and patient outcome.
    
    Histograms of final total virus populations are displayed for lag times of
    150, 75, 0 timesteps between adding drugs (followed by an additional 150
    timesteps of simulation).
    """
    viruses = []
    for i in range(99):
        maxBirthProb = 0.1
        clearProb = 0.05
        resistances = {'guttagonol':False, 'grimpex':False}
        mutProb = 0.005
        viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
    p = Patient(viruses, 1000)
    finres = []
    for i in range(29):
        res = []
        for j in range(149):
            res.append(p.update())
        p.addPrescription('guttagonol')
        for j in range(74):
            res.append(p.update())
        p.addPrescription('grimpex')
        for j in range(149):
            res.append(p.update())
        finres.append(len(res))
    pylab.hist(finres)
    pylab.show()
  
#problem6()
#
# PROBLEM 7
#
     
def problem7():
    """
    Run simulations and plot graphs examining the relationship between
    administration of multiple drugs and patient outcome.

    Plots of total and drug-resistant viruses vs. time are made for a
    simulation with a 300 time step delay between administering the 2 drugs and
    a simulations for which drugs are administered simultaneously.        
    """
    viruses = []
    for i in range(99):
        maxBirthProb = 0.1
        clearProb = 0.05
        resistances = {'guttagonol':False, 'grimpex':False}
        mutProb = 0.005
        viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
    p = Patient(viruses, 1000)
    res = []
    resgu= []
    resgr= []
    resgrgu= []
    finresgu= []
    finresgr= []
    finresgrgu= []
    for j in range(149):
        res.append(p.update())
        for v in p.viruses:
            if v.resistances['guttagonol'] == True:
                resgu.append(v)
            if v.resistances['grimpex'] == True:
                resgr.append(v)
            if v.resistances['guttagonol'] == True and v.resistances['grimpex'] == True:
                resgrgu.append(v)
        finresgu.append(len(resgu))
        finresgr.append(len(resgr))
        finresgrgu.append(len(resgrgu))
    p.addPrescription('guttagonol')
    for j in range(299):
        res.append(p.update())
        for v in p.viruses:
            if v.resistances['guttagonol'] == True:
                resgu.append(v)
            if v.resistances['grimpex'] == True:
                resgr.append(v)
            if v.resistances['guttagonol'] == True and v.resistances['grimpex'] == True:
                resgrgu.append(v)
        finresgu.append(len(resgu))
        finresgr.append(len(resgr))
        finresgrgu.append(len(resgrgu))
    p.addPrescription('grimpex')
    for j in range(149):
        res.append(p.update())
        for v in p.viruses:
            if v.resistances['guttagonol'] == True:
                resgu.append(v)
            if v.resistances['grimpex'] == True:
                resgr.append(v)
            if v.resistances['guttagonol'] == True and v.resistances['grimpex'] == True:
                resgrgu.append(v)
        finresgu.append(len(resgu))
        finresgr.append(len(resgr))
        finresgrgu.append(len(resgrgu))
    pylab.plot(res, label="total population")
    pylab.plot(finresgu, label="guttagonol-resistant")
    pylab.plot(res, label="grimpex-resistant")
    pylab.plot(res, label="resistant to both")
    pylab.legend(loc='upper right')
    pylab.ylabel('population')
    pylab.xlabel('timesteps')
    pylab.title('Virus population')
    pylab.show()
    
    #second simulation
    #almost identical
#problem7()
