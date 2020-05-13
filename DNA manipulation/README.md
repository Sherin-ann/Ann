<h2> Programs for basic DNA manipulation </h2>
<h4><dl>
<dt>Transcription</dt>
<dd>The process of converting DNA sequence to RNA sequence. The program replaces all instances of T (thymine) to U (uracil).</dd>
<dt>Translation</dt>
<dd>The process of converting RNA/DNA sequence to protein sequence. The program stores all the codons (3 consecutive bases) as keys and corresponding amino acid as values in a dictionary. It then creates a sliding window of 3 (using counter i) and replaces the codon with amino acid value. </dd.<br>
<dt>Complement</dt>
<dd>Complementary base pairing is seen in DNA, where A (adenine) pairs with T (thymine) or U (uracil) and vice versa, and G (guanine) pairs with C (cytosine) and vice versa. The program stores the base and its complement as key value pairs in a dictionary. It then iterates over the sequence and replaces the instances of a base with its corresponding complement base. </dd>
<dt>GC Content</dt>
<dd>The program calculates the total GC content of the input sequence using the basic count function.</dd>
