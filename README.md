# CS515 Project-1

## Author Information
Sumedh Badnore 
sbadnore@stevens.edu

[Github Repository](https://github.com/sumedhbadnore/CS515_Project_1.git)

## Estimation of Hours Spent on the project
I have put approximately 17 hours into this project 

## Testing of the code
1. Initial Local Testing: The code has been tested on the local machine using the provided test cases in the examples.
2. Test Harness: Wrote test cases in the specified format and utilized test harness to execute the test cases, capturing the output and comparing it with expected output during each run.

## Unresolved Bugs or Issues
1. The code is designed to function with input data provided through a file path and does not support direct inputs from a PIPE. I attempted to address this limitation by utilizing the 'sys.stdin.isatty()' method. While it was successfully triggered in Git Actions, unfortunately, it did not produce the expected results when tested on a local machine.
2. 'sumcsv.py' program does not capture arguments dynamically. As a workaround, the required arguments had to be hard-coded within the 'test.py'. It works fine if the arguments are passed on command line.


## Examples of bugs resolved
1. I encountered a problem with the sumcsv.py program when attempting to use the Pandas library, which resulted in improper output. To solve this issue, I used the csv library and specifically utilized csv.DictReader() for reading the contents of file.
2. While initially testing all the code on a Windows machine, I encountered an issue as the GitHub Actions test harness executed in a Ubuntu environment.To solve this I had to alter backslashs'\' to front slash'/' in file paths, and expected output files.
3. In test.py program I couldn't provide different arguments for each program to be tested, so as a work around I had to hard-code the arguments so that the program could be tested.


## Extensions Implemented
1. **More advanced wc: multple files** : I have implemented the extension for wc where one can input multiple files and get the total count of characters, words, and lines. The following example shows the sample input and output for this.

```
$ python3 prog/wc.py test/wc.test_1.in test/wc.test_2.in
 10   19  102   test/wc.test_1.in  
 25  532  3276  test/wc.test_2.in
 35  551  3378  total
```

2. **More advanced wc: flags to control output**: I extended the functionality of wc to offer flags to control the information shown in the output. wc -l counts only lines; wc -w counts only words; wc -c counts only characters. The following example shows the sample input and output for this.
```
$ python3 prog/wc.py test/wc.test_1.in -l -w
10 19 test/wc.test_1.in
$ python3 prog/wc.py test/wc.test_1.in -c
102 test/wc.basic.in
```

3. **Extension: More advanced gron: control the base-object name** :I've implemented an extension to update the primary object name for gron using --obj flag. The following shows sample input and the sample output for the same.
```
$ python3 prog/gron.py --obj oi gron.test_1.in 
oi = {};
oi.menu = {};
oi.menu.id = "file"
oi.menu.value = "File"
oi.menu.popup = {};
oi.menu.popup.menuitem = [];
oi.menu.popup.menuitem[0] = {};
oi.menu.popup.menuitem[0].value = "New"
oi.menu.popup.menuitem[0].onclick = "CreateNewDoc()"
oi.menu.popup.menuitem[1] = {};
oi.menu.popup.menuitem[1].value = "Open"
oi.menu.popup.menuitem[1].onclick = "OpenDoc()"
oi.menu.popup.menuitem[2] = {};
oi.menu.popup.menuitem[2].value = "Close"
oi.menu.popup.menuitem[2].onclick = "CloseDoc()"
```
## Program 3: sumcsv.py
I have implemented sumscv.py a program that loads a comma-separated values (CSV) file and sums particular columns and returns the sum.
```
$ python3 prog/sumcsv.py sumcsv.test_1.in Population, GDP
Sum Of Column 'Population': 4095.0
Sum Of Column 'GDP': 44.699999999999996
```

## Extensions for **sumcsv**
I have added functionality to sum elements only in the specified range of column using --colrange flag. 

2. **--colrange** : The --colrange flag serves as an extension to the sumcsv.py program, allowing users to specify a range of columns to be added. The following shows sample input and the sample output for the same.
```
$ python3 prog/sumcsv.py sumcsv.test_1.in --colrange 1:3                           
Sum Of Column 'GDP': 26.3
```
