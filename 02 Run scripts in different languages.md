<h2 align="center">Run scripts in different languages</h2>
<p align="center"><img src="./src/hacking.gif"></p>

- - - - - - - - - - - - - - - - - - - - - -

| **Execution** | **Script** |
| :---: | :--- |
| `bash script.sh` <br> `sh script.sh` <br> `./script.sh` | #!/bin/bash <br> echo "Hello World" |
| `bash scriptArg.sh World!` <br> `sh scriptArg.sh World!` <br> `./scriptArg.sh World!` |  #!/bin/bash <br> if [ $# -eq 0 ]; then <br> &nbsp; echo "Usage: $0 [name]" <br> else <br> &nbsp; echo "Hello $1" <br> fi |

| **Execution** | **Script** |
| :---: | :--- |
| `pwsh script.ps1` <br> `powershell script.ps1` | Write-Output "Hello World" |
| `pwsh scriptArg.ps1` <br> `powershell scriptArg.ps1 -name World!` | param( <br> &nbsp; [string]$name <br> ) <br> if ($name -eq "") { <br> &nbsp; Write-Host "Usage: scriptArg.ps1 [name]" <br> } else { <br> &nbsp; Write-Host "Hello $name" <br> } |

| **Execution** | **Script** |
| :---: | :--- |
| `javac script.java` <br> `java script` | public class script { <br> &nbsp; public static void main(String args[]) <br> &nbsp; { <br> &nbsp; &nbsp; System.out.print("Hello World"); <br> &nbsp; } <br> } |
| `javac scriptArg.java` <br> `java scriptArg World!` | public class scriptArg { <br> &nbsp; public static void main(String args[]) <br> &nbsp; { <br> &nbsp; &nbsp; System.out.print("Hello " + args[0]); <br> &nbsp; } <br> } |

| **Execution** | **Script** |
| :---: | :--- |
| `python script.py` | print("Hello World") |
| `python scriptArg.py World!` | import sys <br> def main(): <br> &nbsp; if len(sys.argv) > 1:  <br> &nbsp; &nbsp; print("Hello", sys.argv[1]) <br> &nbsp; else: <br> &nbsp; &nbsp; print("Usage: python script.py [name]") <br> &nbsp; <br> if __name__ == "__main__": <br> &nbsp; main() |

| **Execution** | **Script** |
| :---: | :--- |
| `ruby script.rb` | puts "Hello World" |
| `ruby scriptArg.rb World!` | if ARGV.empty? <br> &nbsp; puts "Usage: ruby script.rb [name]" <br> else <br> &nbsp; puts "Hello #{ARGV[0]}" <br> end |
