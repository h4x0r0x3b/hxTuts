<h2 align="center">Create an executable script</h2>
<p align="center"><img width="350" height="350" src="./src/banner_cnph.gif"></p>

- - - - - - - - - - - - - - - - - - - - - -
Script files should be named in a **file_name.extension** format such as **script.sh** 

To create, modify, change file details such as the date, etc. Use **touch** command :
```bash
$ touch script.sh
```
> Alternative :

Use `cat` command to create a file with a **redirect** (denoted with the **>** symbol) :
```bash
$ cat > script.sh
#!/bin/bash
echo 'Hello World'
```
press **CTRL + D** while under **cat** command to exit and return to the prompt.

To see what’s in the script.sh file :
```bash
$ cat script.sh
```
- - - - - - - - - - - - - - - - - - - - - -
_*Note*_ : `-switch`, `--option=value` or `-flag | --flag` refers to parameters that modify the behavior of the command,</br>
often starting with a dash `-` or double-dash `--`.

##### Key Differences :

| _*Aspect*_ | _*-Switch*_ | _*--Options*_ | _*-f, --Flag*_ |
| :--: | :--: | :--: | :--: |
| Syntax	| Single hyphen, short (-v)	| Double hyphen, descriptive (--verbose)	| Single or double hyphen (-d, --debug) |
| Arguments	| Typically no arguments	| Often requires a value	| No arguments |

`ls` command stands for Lists, to see the contents of a directory (the files and subdirectories)

| **Switch** | **Explanation** |
| :---: | :---: |
| `-l` | for long list format (also contains the permission) |
| `-a` | --all, to show all contents (includes hidden files) |
| `-h` | --human-readable, print sizes (with -l switch) |

Some commands let you supply multiple arguments by listing them separately or joining them together

Use **-switch** with **ls** command :
```bash
# Multiple separate switch
$ ls -l -a -h 
# Single-lined multiple switch
$ ls -lah
total 8K
drwx------ 14 0x3b 0x3b 4.0K Aug 16 13:22 .
drwxrwx--x  4 0x3b 0x3b 4.0K Jul 17 09:42 ..
-rw-------  1 0x3b 0x3b   31 Aug 16 11:16 script.sh
```
| **File** | **Meaning** |
| :---: | :---: |
| **Single dot (.)** | the current directory |
| **Double dot (..)** | the parent directory |

Use the `ls` command with the `–l (long)` switch to display the contents of a directory in long format—this list will contain the permissions

```bash
1┎───2───┒ 3 ┎───4───┒   5  ┎────6────┒    7
drwxrw­xrw­x 5 root root 4020 Nov 1 12:07 h4ck1ng
drwxrw­xrw­x 2 root root 4020 Nov 1 12:07 isN3v3r
drwxr­wxrw­x 2 0x3b 0x3b 4020 Nov 1 12:07 Th4t
drwxr­wxrw­x 3 0x3b 0x3b 4020 Nov 1 12:07 E4Sy
```

`1` The file type

Following are the possible file type options in the **1st character** of the `ls -l` output.

| **File** | **Type** |
| :---: | :---: |
| `-` | normal |
| `d` | directory |
| `s` | socket |
| `l` | link |

`2` The permissions on the file for owner, groups, and users, respectively<br>
`3` The number of links<br>
`4` The owner of the file<br>
`5` The size of the file in bytes<br>
`6` When the file was created or last modified<br>
`7` The name of the file

Every file and directory are allocated with a level of permission

| **Level** | **Permission** | **Description** |
| :--: | :--: | :--: |
| `r` | ***r***ead | grants permission only to open and view a file |
| `w` | ***w***rite | allows users to view and edit a file |
| `x` | e***x***ecute | allows users to run a file (but not view or edit it) |

Grant executable permission with **chmod** command :
```bash
$ chmod +x script.sh
```
The **mark \*** is known as a glob and used to match any character(s) in the filename :
```bash
# Will grant permission to 'script' named files
$ chmod +x script.*
# Will grant permission to files with .sh extension
$ chmod +x *.sh
# Will grant permission to all files within the current directory
$ chmod +x *
```

Check the permission again with **ls** :
```bash
$ ls -la
-rwx------  1 0x3b 0x3b   31 Aug 16 11:11 script.sh
```

Use a shortcut to refer to permissions by using a single number to represent **one rwx set** of permissions.

| **Binary** | **Octal** | **rwx** |
| :---: | :---: | :---: |
| 000 | 0 | --- |
| 001 | 1 | --x |
| 010 | 2 | -w- |
| 011 | 3 | -wx |
| 100 | 4 | r-- |
| 101 | 5 | r-x |
| 110 | 6 | rw- |
| 111 | 7 | rwx |

`chmod`’s symbolic method is often referred to as the **UGO syntax** which stands `u` for **U**ser (owner), `g` for **G**roup, and `o` for **O**thers;

Lastly, `a` syntax for **A**ll which represents the entire UGO syntax.

```bash
PERMISSION      EXAMPLE
┎────A────┒
 U   G   O
rwx rwx rwx     chmod 777 filename
rwx rwx r-x     chmod 775 filename
rwx r-x r-x     chmod 755 filename
rw- rw- r--     chmod 664 filename
r-- r-- r--     chmod 444 filename
```

Use **rwx** permission to a specific UGO syntax :
```bash
# Will grant rwx permissions to UGO (User, Group, Others)
$ chmod u+rwx,g+r,o+r script.sh
# Check the permission again with ls
$ ls -la
-rwxr--r--  1 0x3b 0x3b   31 Aug 16 11:17 script.sh
```

Use **a** syntax instead to apply permission for all of UGO syntax :
```bash
# Will grant rwx permissions to ALL of UGO syntax
$ chmod a+x script.sh
# Check the permission again with ls
$ ls -la
-rwxr-xr-x  1 0x3b 0x3b   31 Aug 16 11:21 script.sh
```

Use **Octal** permission (shortcut) :
```bash
# Will grant rwx permissions to UGO (User, Group, Others)
$ chmod 777 script.sh
# Check the permission again with ls
$ ls -la
-rwxrwxrwx  1 0x3b 0x3b   31 Aug 16 11:27 script.sh
```
- - - - - - - - - - - - - - - - - - - - - -
Use **nano** command to modify the script :
```bash
$ nano script.sh
```
While under **nano** command :<br>
press **CTRL + O** to **Overwrite** the script.<br>
press **CTRL + X** to **Exit** and return to the prompt.<br>
- - - - - - - - - - - - - - - - - - - - - -
Scripts all begin with the same line, a character sequence that starts with the hash `#` and exclamation mark `!` called the _**shebang**_  `#!`

This tells the operating system that whatever follows the _*shebang*_ is the full path to the script interpreter.

We then follow the _*shebang*_ with `/bin/bash` indicating that we want the operating system to use the BASH shell interpreter.

**Bourne Again SHell (BASH) :**
> Script :
```bash
#!/bin/bash
```
> Command Line :
```bash
$ bash script.sh
```
We can also run the script by using dot-slash notation `./` followed by the script’s name.

> Command Line :
```bash
$ ./script.sh
```

The dot `.` represents the current directory, so we’re essentially telling bash to run **script.sh** from the current working directory.

Use **-switch** with **BASH** :

| **Switch** | **Explanation** |
| :---: | :---: |
| **-x** | displays commands and their results. Useful for debugging. |
| **-v** | Verbose, displays everything even comments and spaces. |
| **-e** | Error Exit, causing the script to immediately exit on the first error. |
| **-f** | checks if the file exists and is a regular file. |
| **-r** | creates a restricted bash shell,</br>which restricts certain potentially dangerous commands. |
| **-n** | will read the commands but won’t execute them,</br>any syntax errors will be shown onscreen. |

> Script :
```bash
#!/bin/bash -x -v -e
```

Specifying an argument within the shebang line requires modifying the script, but you can also pass arguments to the bash interpreter.

> Command Line :
```bash
# Multiple separate switch
$ bash -x -v -e script.sh
# Single-lined multiple switch
$ bash -xve script.sh
```

Whether you pass arguments to the bash interpreter on the command line or on the shebang line won’t make a difference

**SHELL (SH) :**
> Script :
```bash
#!/bin/sh
```
> Command Line :
```bash
$ sh script.sh
```

**PYTHON (PY) :**
> Script :
```python
#!/usr/bin/python
```
> Alternative :
```python
#!/usr/bin/env python
```
> Command Line :
```bash
$ python script.py
```
**JAVA :**
> Script :
```java
// Can run script without #!shebang
public class script {
    public static void main(String args[]) {
    }
}
```
> Command Line :
```bash
# create a .class of script.java
$ javac script.java
# run generated script.class
$ java script
```
- - - - - - - - - - - - - - - - - - - - - -
Pass an **Argument** to a script from a Command Line</br>
_*Note*_ : Argument refers to any input passed to a command.

Use "0x3b" as command line argument

**BASH :**
> Script :
```bash
#!/bin/bash
echo "Hello $1"
```
> Command Line :
```bash
$ ./script.sh 0x3b
OUTPUT: Hello 0x3b
```
**PYTHON :**
> Script :
```python
#!/usr/bin/python
print("Hello", __import__('sys').argv[1])
```
> Command Line :
```python
$ ./script.py 0x3b
OUTPUT: Hello 0x3b
```
> Alternative :
```python
# Can run script without #!shebang
import sys
print("Hello %s" % sys.argv[1])
```
> Command Line :
```python
$ python script.py 0x3b
OUTPUT: Hello 0x3b
```
**JAVA :**
> Script :
```java
// Can run script without #!shebang
public class script {
    public static void main(String args[]) {
        System.out.print("Hello " + args[0]);
    }
}
```
> Command Line :
```bash
# create a .class of script.java
$ javac script.java
# run generated script.class with argument
$ java script 0x3b
OUTPUT: Hello 0x3b
```
