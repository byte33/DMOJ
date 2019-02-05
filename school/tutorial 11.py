class Particle:

    def __init__(self, prot, neut, elec):
        self.p = prot
        self.n = neut
        self.e = elec

    def getP(self):
        return self.p

    def getN(self):
        return self.n

    def getE(self):
        return self.e

    def betaDecay(self):
        self.p += 1
        self.n -= 1
        self.e += 1

    def smash(self, otherParticle):
        part1 = Particle(self.p, self.n, self.e)
        part2 = otherParticle

        finalP = part1.p + part2.p
        finalN = part1.n + part2.n
        finalE = part1.e + part2.e

        return Particle(finalP, finalN, finalE)


hi = Particle(6, 2, 2)
particle2 = Particle(2, 4, 7)
help_me = hi.smash(particle2)

print(help_me.getP(), help_me.getN(), help_me.getE())
