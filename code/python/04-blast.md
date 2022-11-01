# Similarity of Sequences

identity: same seq / total length
similarity: similar seq / total length

## Substitution Matrix

### DNA Substitution Matrix

1. identity matrix: same 1, different 0
2. transition-transversion matrix
   - same 1
   - transition -1 (A->G, C->T)
   - transversion -5 (A->C, T->G)
3. BLAST matrix: same 5, different -4
   - Wildly used

```
BLAST Matrix
    A   T   C   G
A   5  -4  -4  -4
T  -4   5  -4  -4
C  -4  -4   5  -4
G  -4  -4  -4   5
```

### Protein Substitution Matrix

1. identity matrix: same 1, different 0
2. PAM (point accepted mutation)
   - observed substitutions are considered to **be accepted by natural selection**.
   - PAM-1 (1% of the amino acid positions that have been changed, based on closely related sequences)
   - $\text{PAM-2} = \text{PAM-1}^2$
   - PAM 30 and the PAM70 are usually used.
3. BLOSUM (BLOck SUbstitution Matrix)
   - based similarity of real data
   - **BLOSUM-62** 

| Dif  | PAM     | BLOSUM    |
| :--- | :------ | :-------- |
| 1    | PAM-1   | BLOSUM-99 |
| 10   | PAM-11  | BLOSUM-90 |
| 20   | PAM-23  | BLOSUM-80 |
| 30   | PAM-38  | BLOSUM-70 |
| 40   | PAM-56  | BLOSUM-60 |
| 50   | PAM-80  | BLOSUM-50 |
| 60   | PAM-112 | BLOSUM-40 |
| 70   | PAM-159 | BLOSUM-30 |
| 80   | PAM-246 | BLOSUM-20 |

dif for difference.

- For comparing related proteins: both fine
- for not related: BLOSUM

## Different Length

### Dotlet

- different len: diagonal dots
- self: find repetitive sequences

https://dotlet.vital-it.ch/

### Alignment

insert gaps to let most similar sequences get together

#### Pairwise Alignment

- Global: Needleman-Wunsch
- Local: Smith-Waterman

##### Global Alignment

1. Set gap penalty (Gap penalty matters!)
2. compute all scores
3. Start from the last element, find the largest number, Go back.

$$
Score(0,0) = 0 \\
Score(i,j) = max \begin{cases}
    (i-1, j-1) + match/mismatch (diagonal\ move)\\
    (i-1, j) - gap penalty (horizontal\ move)\\
    (i, j-1) - gap penalty (vertical\ move)
\end{cases}
$$

Example

Gap penalty = 5

Substitution Matrix

|     | A   | G   | C   | T   |
| --- | --- | --- | --- | --- |
| A   | 10  | -1  | -3  | -4  |
| G   | -1  | 7   | -5  | -3  |
| C   | -3  | -5  | 9   | 0   |
| T   | -4  | -3  | 0   | 8   |

Score


| nt  |     | 0   | 1      | 2     | 3     | 4      | 5      |
| --- | --- | --- | ------ | ----- | ----- | ------ | ------ |
|     |     |     | A      | C     | G     | T      | C      |
| 0   |     | 0   | -5     | -10   | -15   | -20    | -25    |
| 1   | A   | -5  | **10** | **5** | 0     | -5     | -10    |
| 2   | A   | -10 | 5      | 7     | **4** | -1     | -6     |
| 3   | T   | -15 | 0      | 5     | 4     | **12** | 7      |
| 4   | C   | -20 | -5     | 9     | 4     | 7      | **21** |

So the alignment is:

```
ACGTC
| |||
A-ATC
```
##### Local Alignment


