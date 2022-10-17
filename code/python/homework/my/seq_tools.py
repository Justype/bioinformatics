import re

def reverse_complement(seq: str) -> str:
    """
    return reverse complement of the input DNA sequence
    """
    nt_pair = {"A": "T", "C": "G", "G": "C", "T": "A"}
    return "".join([nt_pair[nt] for nt in seq[::-1]]) # just put things below together

    seq_reverse = seq[::-1] # reverse the sequence
    seq_rc = [nt_pair[nt] for nt in seq_reverse] # get the complement of reversed sequence
    seq_rc = "".join(seq_rc) # make it into a string
    return seq_rc

def translate(seq: str) -> str:
    """
    translate the DNA sequence.
    """
    assert len(seq) % 3 == 0, "length {} is not divisible by 3".format(len(seq))

    genetic_code = {'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M', 'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T', 'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K', 'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R', 'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L', 'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P', 'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGA': 'R', 'CGC': 'R', 'CGG': 'R',
               'CGT': 'R', 'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V', 'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A', 'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E', 'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G', 'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S', 'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L', 'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_', 'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W'}

    return "".join([genetic_code[seq[i:i+3]] for i in range(0, len(seq), 3)]) # just put things below together
    codons = [seq[i:i+3] for i in range(0, len(seq), 3)] # split the sequence of every 3 letters
    aas = [genetic_code[codon] for codon in codons] # get a list of amino acids translated
    aas = "".join(aas) # make it into a string
    return aas

def get_orf(seq: str) -> list:
    """
    return a list of all open reading frames as amino acids
    """
    orf = []

    frames = [seq[i:] for i in range(3)] # add 3 frames of forward sequence
    seq_rc = reverse_complement(seq) # get reverse complete strand
    frames.extend([seq_rc[i:] for i in range(3)]) # add 3 frames of reverse complete strand

    for frame in frames:
        orf.extend(translate(frame[:len(frame) - len(frame) % 3]).split("_")) # translate the frame and split the amino acids by _(stop codon)
    return [o for o in orf if o != ""] # remove the empty string

def process_seq_indices(seq: str, start: int, end: int, direction: str = "") -> dict:
    """
    end is not include

    Return a dict:
        - `"ORF"`   nucleotide sequence
        - `"START"` index of first nucleotide
        - `"END"`  index of last nucleotide 
        - `"AA"`    amino acids translated
    
    Parameters:
        - end: not include
        - direction:
            - ` ` default
            - `+` forward
            - `-` reverse complete
    """
    return {
        "ORF": seq[start:end],
        "START": "{}{}".format(direction, start + 1),
        "END": "{}{}".format(direction, end),
        "AA": translate(seq[start:end])
    }

def get_stop_codons(seq: str) -> tuple:
    """
    return a tuple of lists of indices of stop codon from the DNA sequence given

    grouped by the remainder of index divided by 3

    - `0` remainder = 0
    - `1` remainder = 1
    - `2` remainder = 2
    """

    possible_stop_codons = [match.start() for match in re.finditer(r"(TAA|TAG|TGA)", seq)]
    # divided into 3 groups:  index % 3 == 0 or 1 or 2 
    group1 = []
    group2 = []
    group3 = []

    for codon in possible_stop_codons:
        if codon % 3 == 0:
            group1.append(codon)
        elif codon % 3 == 1:
            group2.append(codon)
        else: # it must be i % 3 == 2
            group3.append(codon)

    return group1, group2, group3 # return a tuple with three different groups

def get_3_frames_orf(seq: str, direction = "") -> list:
    """
    return a list of orf of the 3 frames
    """
    orf = []

    stop_codons = get_stop_codons(seq)
    seq_len = len(seq)
    for i in range(3):
        last_index = seq_len - seq_len % 3 + i # make sure last_index - i is divisible by 3
        last_index = last_index if last_index <= len(seq) else last_index - 3 # make sure it is less than the length
        # print(stop_codons[i])
        # print(last_index)

        # group together to generate a list like
        # 0               index1 of stop_codons[i]
        # index1 + 3      index2
        # ...             ...
        # index_last + 3  last possible index
        start_indices = [i] + [index + 3 for index in stop_codons[i]]
        end_indices = stop_codons[i] + [last_index]

        # if len(stop_codons[i]) == 0, it would be (0, last_index)
        for start, end in zip(start_indices, end_indices):
            if start == end:
                continue
            data = process_seq_indices(seq, start, end, direction)
            if not re.search("^_*?$", data["AA"]):
                orf.append(data)

    return orf

def get_orf_info(seq: str) -> list:
    """
    return a list of dicts of all open reading frames

    - `"ORF"`   nucleotide sequence
    - `"START"` index of first nucleotide
    - `"END"`   index of last nucleotide 
    - `"AA"`    amino acids translated
    """
    return get_3_frames_orf(seq, "+") + get_3_frames_orf(reverse_complement(seq), "-")

def get_orf_another_way(seq: str) -> list:
    """
    return a list of all open reading frames as amino acids
    """
    return [o["AA"] for o in get_orf_info(seq)]