# PYTHON ABBREVIATIONS 

task: read file with names and generate 3 letters abbreviation. 

## Rules: 
* Abbreviations - UPPER CASE LETTERS 
* Ignore: Apostrophes ('), non-letter characters -> split texts,  
* Abbreviation = 1 letter of the name + 2 further letters 
* Any abbreviation which can be formed from more than one name on the list - excluded 
* Each abbreviation => Score => Lower score the better is the Ab. <br>
    * score = sum 2 and 3 letter 
    * if letter = first letter of a word => score = 0
    * if letter = last letter of a word => score = 2; except E=>score = 15
    * else => sum of index in the word + value based on how common/uncommon this iletter is in EN
* main function= names()
* output = names_abbrevs.txt => name - abbreviation 
* if not acceptable translation = blank line 
* if same score - both abbreviations 
* trees.txt 

## Examples: 
Object-Oriented programming => OBJECT ORIENTED PROGRAMMING <br>
Moore's Law => MOORES LAW <br>
Data Engineering = (OK) DTA DEG; (BAD) DEA ATA; DAN(13)<br>

OBJECT ORIENTED PROGRAMMING = OOP (0); OAN (44= 0+(5+20)+(9+10)); <br>
Cold     = COL(28), COD(18), CLD(14)<br>
Cool     = COO(33), COL(18)<br>
C++ Code = CCO(16), CCD(11), CCE(15), COD(27), COE(31), CDE(26)<br>