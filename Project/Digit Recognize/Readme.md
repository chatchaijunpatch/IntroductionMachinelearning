# Digit Rec.

<p> Create on 19/05/22 - 23/05/22

<h2>List of Folder</h2>
<ol>
<li>dataset : contain of digit dataset</li>
<li>images : contain images that use for testing</li>
<li>own_dataset : dataset that collect from digitcv2.py </li>
</ol>

-----
<h2>List of Files</h2>
<ul>
<li>digit_1.ipynb : paper for testing model but dataset is import from opencv</li>
<li>digit_2.ipynb : similar digit_1 but dataset is from "dataset" folder</li>
<li> predict.py : model from digit_2. use in digitcv2.py</li>
</ul>

---
<h2>Explaination in digitcv2</h2>

<p>First, Draw digit 1-10. The line must be blue and heavy. The font of digit that draw should big.

***color can customize on "digitcv2.py" in line 40,41***

<p style=" font-weight: 400;"> Example</p>

![readme](/images/readme.png)

Second, press "q" to quit program, and press "w" to capture the digit (this can use for collecting data).

Third, picture will in font of program. you have to put in to "own_dataset" and create folder for collect digit picture inside.

***Note that folder name is important. It effect in program too, So I suggest you have to create folder name follow on this list***

***zero = ['0_0','0_1','0_2','0_3']</br>
    one = ['1_0','1_1','1_2','1_3']</br>
    two = ['2_0','2_1','2_2','2_3']</br>
    three = ['3_0','3_1','3_2','3_3']</br>
    four = ['4_0','4_1','4_2','4_3']</br>
    five = ['5_0','5_1','5_2','5_3']</br>
    six = ['6_0','6_1','6_2','6_3']</br>
    seven = ['7_0','7_1','7_2','7_3']</br>
    eight = ['8_0','8_1','8_2','8_3']</br>
    nine = ['9_0','9_1','9_2','9_3']</br>
This can customize in "predict.py" on Train function***

Fourth, range in closeup can customize in line 49 "digitcv2.py"

Fifth, you can change the video width and height, but
***don't forget to change width and height in line 57 "digitcv2.py"***

Finally, This program can detect contour only 3, So if you want to detect more, you can change in line 46 on "digitcv2.py"

----
# Hope you like it
# ʕ•́ᴥ•̀ʔっ ʕ•́ᴥ•̀ʔっ ʕ•́ᴥ•̀ʔっ ʕ•́ᴥ•̀ʔっ ʕ•́ᴥ•̀ʔっ