Bash reference manual: https://www.gnu.org/software/bash/manual/html_node/index.html#SEC_Contents

### To print all the system variables of UBUNTU use the command 

```
> printenv
```

### To print the system variables in bash scripting

```
#!/bin/bash
echo $BASH
echo $BASH_VERSION
echo $HOME
echo $PWD
```

### How to create variables in bash scripting

```
#!/bin/bash
name=Mark
echo $name 
echo The name is $name
```

### To retrieve values from user

```
#!/bin/bash
echo "Enter names:"
read name1 name2 name3
echo "Names: $name1, $name2, $name3
```

### If loop in bash script

-eq is called a binary operator. Full list of binary operators here. https://www.gnu.org/software/bash/manual/html_node/Bash-Conditional-Expressions.html

```
#!/bin/bash
MYNUM=100
if [[ $MYNUM -eq 200 ]]
then
    echo "testing123"
fi
```

If then else statement

```
#!/bin/bash
MYNUM=100
if [[ $MYNUM -eq 200 ]]
then
    echo "testing123"
else
    echo "My number is not equal to 200"
fi
```

### For loop in bash script

Example 1:

```
#!/bin/bash
for i in 1 2 3 4 5
do
  echo $i
done
```

Example 2: 

// {1..10} -> denotes 1,2,3,4,5,6,7,8,9,10
// {1..10..2} -> increment the value by 2
{START..END..INCREMENT}

```
#!/bin/bash
for i  in {1..10}
do
  echo $i
done
```

Example 3:

```
#!/bin/bash
for ((i=0; i<5; i++))
do
  echo $i
done
```

Example 4: comparing variable in files

```
#!/bin/bash
for VARIABLE in file1 file2 file 3
do
 ...
 ...
done
```

Example 5: Giving linux command as an input

```
#!/bin/bash
for OUTPUT in $(Linux-command-here)
do
 ...
 ...
done
```

### Using PIPES in bash scripting

PIPES takes the output of one command and uses it as input of another command

Syntax: command1 | command2

Example:
```
ls -lt - (-l means long listing, t means based on the newest directory created)
```
```
head - displays only the first 10 lines
```
so 
```
ls -lt | head (displays 10 directories and the newest directory created will be on the top)
```

### Using functions in bash scripting

There are two ways to write functions as shown below

```
#!/bin/bash
function name(){
  commands
}
```

```
#!/bin/bash
name () {
  commands
}
```

Example

```
#!/bin/bash

function Hello(){
  echo "hello"
}

quit () {
  exit
}

Hello            #Calling the Hello function
echo "foo"       #Printing the word foo
quit             #Calling the quit function 

```
