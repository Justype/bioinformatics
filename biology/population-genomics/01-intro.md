Focus:

1. [Wright-Fisher Model](#wright-fisher-model)
2. [Ne (Effective Size)](#effective-size-of-a-population)


# Intro to Population Genetics

Molecular population genetics is the study of **mutations** as they **rise and fall in frequency** in a population.

mainly focus on the *effects of evolutionary process* on natural populations

1. genetic drift
2. recombination
3. natural selection

Evolutionary forces can 

- **accelerate** or **impede** mutation.
- be inferred from pattern of molecular variation.
- includes: mutation, recombination, natural selection

## Terminology

[Books P21](molecular-population-genetics.pdf#page=21)

- *sequence* or *chromosome* : homologous DNA stand
- *genes* : sequences at a single locus 
- *allele*: individual nucleotides (or amino acids) at a single position in the alignment
- *sample*
- *cistron* 顺反子
- *allele copy*
- *polymorphism* = *segregating site* = *mutation* = *SNP (single nucleotide polymorphism)*
- *haplotype*: set of alleles found on a single sequence (see example below)
- *mutation*: process of generating variation
- *substitution* DNA differences **between** species
- *variation* DNA differences **in** species

Example:

```
     |1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
seq1 |T T A C A A T C C G  A  T  C  G  T
seq2 |T T A C G A T G C G  C  T  C  G  T
seq3 |T C A C A A T G C G  A  T  G  G  A
seq4 |T T A C G A T G C G  C  T  C  G  T

- sample size n = 4 chromosome
- length L = 15
- six sites with nucleotide differences (2,5,8,11,13,15) S = 6
- There are 3 haplotypes. seq2 and seq4 are the same. 
```

- *indel*: insertion / deletion

## Model of Population

### Wright-Fisher Model

Model of Populations

- constant size
- 2N
- hermaphrodite (雌雄同体)
- wholesale replacement
- mate at random, chromosomes sampled uniformly with replacement
- no mutation and selection

#### Drift and Selection

- *genetic drift*: by chance
- *natural selection*: by natural force

*fixed*: allele frequency drifts to 1

- Once fixation occurs, no more change.
- genetic variation is expected to decline when drift is the only force.

*heterozygosity*

### Moran Model

- haploid
- no wholesale replacement

change in allele frequency:

- reproduction of individuals carrying this allele 
- death of individuals carrying another allele

[Books P24](molecular-population-genetics.pdf#page=24)

twice as much as drift in the Moran model

### Effective Size of a Population

the amount of drift expected in an idealized Wright-Fisher population.

4 ways to find effects of drifts (different ways, the value will be the same)

1. variance
2. inbreeding
3. eigenvalue
4. coalescent (molecular seq data)

## Model of Mutation

- mutation is random
- probability not equal
  - type
    - transition (more often, between purines or pyrimidines)
    - transaction (purine to pyrimidine, or vice versa)
  - loci
- advantageous or deleterious is different in different environments

Generally, neutral mutations are only considered.



## Phylogenetic Tree

Try to answer: Where and when did our species originate?

[Definition](molecular-population-genetics.pdf#page=20)

- Sorting Tolerant from Intolerant (SIFT)
- Genomic evolutionary rate profiling (GERP)

## 

MSA Mul

# 英中

词根|意思
:--|:--
iso-|同
bi-|双

英文|中文
:--|:--
haploid|单倍体
inbred|近交的
biallelic | 双等位基因的
mono

locus

allelo

haplotype