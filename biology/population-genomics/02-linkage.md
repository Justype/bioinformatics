# Linkage and Recombination

Linkage Disequilibrium: The nonrandom association of alleles at two loci in a population.

## Gametic Phase

*Phase*: alleles at sites of a chromosome

*Gametes*: haploid allele combinations at two-loci that could be found in the egg or sperm

Example [Week3 P3](slides/03.pdf#page=3)

## Linkage

Two loci on the same chromosome are "linked" 

But due to recombination, the loci can cross-link

So conventionally,

- linkage: < 50cM
- free recombination: > 50cM

## Linkage Disequilibrium (LD)

LD is a nonrandom association between genotypes at two loci inferred from population data

    Consider two biallelic loci
    
    - A is an allele at locus A with frequency pA
    - B is an allele at locus B with frequency pB
    - If locus A and locus B are independent, then expect frequency of AB gamete of pA*pB
    
    If the observed frequency of AB gamete in a sample from a population differs from expectation, then there is linkage disequilibrium between the two loci

### Pairwise Measure of LD

Consider two bi-allelic loci with allele frequencies p1, p2 and q1 and q2 and observed gamete frequencies of gij, where i is the allele from p and j is the allele from locus j

- g11 = p1q1 + D
- g12 = p1q2 - D
- g21 = p2q1 - D
- g22 = p2q2 + D
- $D = g_{ij} - p_iq_j \in [-1, 1]$
- g11 and g22 are in "coupling phase"
- By convention g11 consists of two most common alleles, g22 the two rare

https://doc.goldenhelix.com/SVS/latest/svsmanual/ftParts/computing_ld.html

The more linkage is, the higher D is.

The centimorgan (cM) is a measure of the frequency of recombination where 1 cM corresponds to a 1% frequency of two markers (e.g., SNPs) will recombine during meiosis.

## The population recombination parameter ⍴

how much recombination has occurred in the history of a sample of sequences?

$\rho = 4N_e c$

- c: per site recombination rate
- Ne: effective population size

