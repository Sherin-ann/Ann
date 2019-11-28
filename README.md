<h2>Spoken english to written english</h2>

<i>spokentowritten</i> is a python module or a reusable library which can be used to convert a paragraph of spoken english to written english. 

This module converts spoken currencies like dollars, rupees, euros to their respective symbols. <br>
For example, dollars to $, rupees to ₹,  percent to % and euros to € is incorporated in this module.

The other features include:<br>
Abbreviations spoken as C M are converted to CM. Similarly abbreviations like P M and A M are converted to their proper forms.<br>
Tuples used in the paragraph are read in a way that the corresponding quantity is multiplied said-fold. For example, triple A is converted to AAA and so on.<br>
Numbers used before currencies and percent are converted to their corresponding figures. For example, five dollars is converted to $5, and so on.<br>

<h2>Download:</h2>
Download <i>spokentowritten.py</i> and save it in the same directory as your python program. Follow the steps mentioned in the usage below to use this module in your program.

<h2>Usage:</h2>
You can import this module in your python program as:

```python3
import spokentowritten as stw
stw.para_convert()
```
<h2>Features to be implemented in future versions include:</h2>
Handling punctuation marks and spaces in the paragraph<br>
Handling case conversions (uppercase/lowercase sensitive) for the attributes to be converted<br>
Including other symbols like alpha, beta, gamma etc.,<br>
Handling date and time<br>
Handling other denominations of currency and money-figures in the paragraph<br><hr>
