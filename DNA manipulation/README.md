<h2 align="center"> Programs for basic DNA manipulation </h2><br>
<h3><dl>
<dt>Transcription</dt>
  <h5><dd>The process of converting DNA sequence to RNA sequence. The program <p style="color:blue"><i>transcription.py</p></i> replaces all instances of T (thymine) to U (uracil).</h5></dd>

<dt>Translation</dt>
<h5><dd>The process of converting RNA/DNA sequence to protein sequence. The program <p style="color:blue"><i>translation.py</p></i> stores all the codons (3 consecutive bases) as keys and corresponding amino acid as values in a dictionary. It then creates a sliding window of 3 (using counter i) and replaces the codon with amino acid value.</h5></dd>

<dt>Complement</dt>
<h5><dd>Complementary base pairing is seen in DNA, where A (adenine) pairs with T (thymine) or U (uracil) and vice versa, and G (guanine) pairs with C (cytosine) and vice versa. The program <p style="color:blue"><i>complement.py</i></p> stores the base and its complement as key value pairs in a dictionary. It then iterates over the sequence and replaces the instances of a base with its corresponding complement base. </h5></dd>

<dt>GC Content</dt>
<h5><dd>The program <p style="color:blue"><i>gc_count.py</i></p> calculates the total GC content of the input sequence using the basic count function.</h5></dd>
</h3></dl>
