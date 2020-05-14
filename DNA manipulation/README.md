<h2 align="center"> Programs for basic DNA manipulation </h2><br>
<dl>
  <h3><dt>Transcription</dt></h3>
  <dd>The process of converting DNA sequence to RNA sequence. The program <i>transcription.py</i> replaces all instances of T (thymine) to U (uracil).</dd>

<h3><dt>Translation</dt></h3>
<dd>The process of converting RNA/DNA sequence to protein sequence. The program <i>translation.py</i> stores all the codons (3 consecutive bases) as keys and corresponding amino acid as values in a dictionary. It then creates a sliding window of 3 (using counter i) and replaces the codon with amino acid value.</dd>

<h3><dt>Complement</dt></h3>
<dd>Complementary base pairing is seen in DNA, where A (adenine) pairs with T (thymine) or U (uracil) and vice versa, and G (guanine) pairs with C (cytosine) and vice versa. The program <i>complement.py</i> stores the base and its complement as key value pairs in a dictionary. It then iterates over the sequence and replaces the instances of a base with its corresponding complement base. </dd>

<h3><dt>GC Content</dt>
<dd>The program <i>gc_count.py</i> calculates the total GC content of the input sequence using the basic count function.</dd>
</dl>
