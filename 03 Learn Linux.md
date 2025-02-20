<h2 align="center">Learn Linux</h2>
<p align="center"><img src="./src/Filesystem Hierarchy Standard.png"></p>

- - - - - - - - - - - - - - - - - - - - - -

### Filesystem Hierarchy Standard (FHS)

| Path   | Description |
| :---:  | :---: |
| `/`    | The top-level directory, root filesystem containing files required to boot the OS and mount other filesystems. |
| `/bin` | Essential command binaries. |
| `/boot` | Static bootloader, kernel executable, and boot files for Linux OS. |
| `/dev` | Device files for accessing hardware devices. |
| `/etc` | Local system configuration files and app configurations. |
| `/home` | User subdirectories for personal storage. |
| `/lib` | Shared library files required for system boot. |
| `/media` | Mount point for removable media devices like USB drives. |
| `/mnt` | Temporary mount point for regular filesystems. |
| `/opt` | Optional files like third-party tools. |
| `/root` | Home directory for the root user. |
| `/sbin` | System administration binaries. |
| `/tmp` | Temporary storage for system and app files, often cleared on boot. |
| `/usr` | Contains executables, libraries, and documentation. |
| `/var` | Variable data files such as logs, emails, and web files. |

### Shell Job Control
---
| Command | Description |
| :---: | :---: |
| `jobs` | List your jobs |
| `&` | Run a job in the background |
| `^Z` | Suspend the current (foreground) job |
| `suspend` | Suspend a shell |
| `fg` | Unsuspend a job: bring it into the foreground |
| `bg` | Make a suspended job run in the background |

### Basic File Operations
---
| Command | Description |
| :---: | :---: |
| `ls` | List files in a directory |
| `cp` | Copy a file |
| `mv` | Rename (“move”) a file |
| `rm` | Delete (“remove”) a file |
| `ln` | Create links (alternative names) to a file |
| `shred` | Completely erase a file when the file is deleted |

### Directory Operations
---
| Command | Description |
| :---: | :---: |
| `cd` | Change your current directory |
| `pwd` | Print the name of your current directory, i.e., “where you are now” in the filesystem |
| `basename` | Print the final part of a file path |
| `dirname` | Print a file path without its final part |
| `mkdir` | Create (make) a directory |
| `rmdir` | Delete (remove) an empty directory |
| `rm -r` | Delete a non-empty directory and its contents |

### File Opening
---
| Command | Description |
| :---: | :---: |
| `cat` | View files in their entirety |
| `less` | View text files one page at a time |
| `head` | View the first lines of a text file |
| `tail` | View the last lines of a text file |
| `nl` | View text files with their lines numbered |
| `strings` | Display text embedded in a binary file |
| `od` | View data in octal (or other formats) |
| `xxd` | View data in hexadecimal |
| `acroread` | View PDF files |
| `gv` | View PostScript or PDF files |
| `xdvi` | View TeX DVI files |

### File Creation and Editing
---
| Command | Description |
| :---: | :---: |
| `emacs` | Text editor from Free Software Foundation |
| `vim` | Text editor, extension of Unix vi |
| `soffice` | Office suite for editing Microsoft Word, Excel, and PowerPoint documents |
| `abiword` | Edit Microsoft Word documents |
| `gnumeric` | Edit Excel spreadsheets |

### File Properties
---
| Command | Description |
| :---: | :---: |
| `stat` | Display attributes of files and directories |
| `wc` | Count bytes, words, lines in a file |
| `du` | Measure disk usage of files and directories |
| `file` | Identify (guess) the type of a file |
| `touch` | Change timestamps of files and directories |
| `chown` | Change owner of files and directories |
| `chgrp` | Change group ownership of files and directories |
| `chmod` | Change protection mode of files and directories |
| `umask` | Set a default mode for new files and directories |
| `chattr` | Change extended attributes of files and directories |
| `lsattr` | List extended attributes of files and directories |

### File Location
---
| Command | Description |
| :---: | :---: |
| `find` | Locate files in a directory hierarchy |
| `xargs` | Process a list of located files (and much more) |
| `locate` | Create an index of files, and search the index for string |
| `which` | Locate executables in your search path (command) |
| `type` | Locate executables in your search path (bash built-in) |
| `whereis` | Locate executables, documentation, and source files |

### File Text Manipulation
---
| Command | Description |
| :---: | :---: |
| `grep` | Find lines in a file that match a regular expression |
| `cut` | Extract columns from a file |
| `paste` | Append columns |
| `tr` | Translate characters into other characters |
| `sort` | Sort lines of text by various criteria |
| `uniq` | Locate identical lines in a file |
| `tee` | Copy a file and print it on standard output, simultaneously |

### File Compression and Packaging
---
| Command | Description |
| :---: | :---: |
| `tar` | Package multiple files into a single file |
| `gzip` | Compress files with GNU Zip |
| `gunzip` | Uncompress GNU Zip files |
| `bzip2` | Compress files in BZip format |
| `bunzip2` | Uncompress BZip files |
| `bzcat` | Compress/uncompress BZip files via standard input/output |
| `compress` | Compress files with traditional Unix compression |
| `uncompress` | Uncompress files with traditional Unix compression |
| `zcat` | Compress/uncompress files via standard input/output (gzip or compress) |
| `zip` | Compress files in Windows Zip format |
| `unzip` | Uncompress Windows Zip files |
| `metamail` | Extract MIME data to files |

### File Comparison
---
| Command | Description |
| :---: | :---: |
| `diff` | Line-by-line comparison of two files or directories |
| `comm` | Line-by-line comparison of two sorted files |
| `cmp` | Byte-by-byte comparison of two files |
| `md5sum` | Compute a checksum of the given files (MD5) |

### Printing
---
| Command | Description |
| :---: | :---: |
| `lpr` | Print a file |
| `lpq` | View the print queue |
| `lprm` | Remove a print job from the queue |

### Spell Checking
---
| Command | Description |
| :---: | :---: |
| `look` | Look up the spelling of a word quickly |
| `aspell` | Interactive spelling checker |
| `spell` | Batch spelling checker |

### Disks and Filesystems
---
| Command | Description |
| :---: | :---: |
| `df` | Display available space on mounted filesystems |
| `mount` | Make a disk partition accessible |
| `umount` | Unmount a disk partition (make it inaccessible) |
| `fsck` | Check a disk partition for errors |
| `sync` | Flush all disk caches to disk |
| `lshw` | (List Hardware) list detailed information about hardware configuration |
| `inxi` | System information script with readable output</br>`-F` for full info</br>`-S` for system</br>`-C` for CPU |
| `lsblk` | (List Hardware) shows information about block devices, except RAM disks |

### Backups and Remote Storage
---
| Command | Description |
| :---: | :---: |
| `dump` | Write a disk partition to a backup medium |
| `restore` | Restore the results of a dump |
| `cdrecord` | Burn a CD, DVD, or Blu-ray disc |
| `rsync` | Mirror a set of files onto another device or host |
| `mt` | Control a tape drive |

### Viewing Processes
---
| Command | Description |
| :---: | :---: |
| `ps` | List processes |
| `uptime` | View the system load |
| `w` | List active processes for all users |
| `top` | Monitor resource-intensive processes interactively |
| `htop` | A user-friendly, interactive process viewer for Unix systems |
| `iotop` | A disk I/O usage monitor, showing processes using the most disk I/O (Input/Output) |
| `powertop` | Power consumption monitoring tool, identifying power-consuming processes |
| `gnome-system-monitor` | Graphical system load and process monitor |
| `xload` | Graphical monitor of system load |
| `free` | Display free memory |
| `pidof` | Find the PID of a process by name |
| `nmon` | Performance monitoring tool with detailed system metrics |

### Check
---
| Command | Description |
| :---: | :---: |
| `ssh` | Securely connect to remote servers over an unsecured network |
| `munin` | Monitor networked resources and present system performance data in graphs |

### Controlling Processes
---
| Command | Description |
| :---: | :---: |
| `kill` | Terminate a process or send it a signal |
| `killall` | Terminate all processes matching a given name</br>Usage: killall [process-name]</br>`-s` allows you to specify a signal (e.g., killall -s SIGKILL firefox)</br>`-i` prompts for confirmation before killing each process</br>`-u` lets you kill processes belonging to a specific user |
| `nice` | Run a program with a specified priority |
| `renice` | Change a process’s priority while running |
| `cpulimit` | Limit CPU usage for a process by specifying allowed CPU percentage</br>Usage: cpulimit -p [PID] -l [percentage]</br>Example: cpulimit -p 1234 -l 50</br>`-e` can be used instead of</br>`-p` to limit a process by its executable name.</br>`-b` runs cpulimit in the background |

### Scheduling Jobs
---
| Command | Description |
| :---: | :---: |
| `sleep` | Pause execution for a set number of seconds |
| `watch` | Run a program at regular intervals |
| `at` | Schedule a job for a single future time |
| `crontab` | Schedule recurring jobs |

### Logins, Logouts, and Shutdowns
---
| Command | Description |
| :---: | :---: |
| `shutdown` | Halt or reboot a Linux system |

### Users and Their Environment
---
| Command | Description |
| :---: | :---: |
| `logname` | Print the login name |
| `whoami` | Print the current effective username |
| `id` | Print user ID and group memberships |
| `who` | List logged-in users (detailed) |
| `users` | List logged-in users (short) |
| `finger` | Show information about users |
| `last` | Show when users last logged in |
| `printenv` | Print environment variables |

### User Account Management
---
| Command | Description |
| :---: | :---: |
| `useradd` | Create a user account |
| `userdel` | Delete a user account |
| `usermod` | Modify a user account |
| `passwd` | Change a user’s password |
| `chfn` | Change a user’s personal information |
| `chsh` | Change a user’s shell |

### Group Management
---
| Command | Description |
| :---: | :---: |
| `groups` | Show group memberships |
| `groupadd` | Create a group |
| `groupdel` | Delete a group |
| `groupmod` | Modify a group |

### Host Information
---
| Command | Description |
| :---: | :---: |
| `uname` | Display basic system information |
| `hostname` | Display the system hostname |
| `dnsdomainname` | Display the DNS domain name (Same as `hostname -d`) |
| `domainname` | Display the NIS domain name (Same as `hostname -y`) |
| `ip` | Configure and display network interfaces |
| `ifconfig` | (Deprecated) Older command to configure and display network interfaces |

### Host Location
---
| Command | Description |
| :---: | :---: |
| `host` | Lookup hostnames, IP addresses, and DNS information |
| `whois` | Lookup Internet domain registrants |
| `ping` | Test reachability of a remote host |
| `traceroute` | Show the network path to a remote host |
| `dig` | Query DNS servers for detailed information |

### Network Connections
---
| Command | Description |
| :---: | :---: |
| `ssh` | Securely connect to a remote host or run commands |
| `telnet` | Insecurely connect to a remote host |
| `scp` | Securely copy files to/from a remote host (batch mode) |
| `sftp` | Securely transfer files interactively |
| `ftp` | Transfer files interactively (insecure) |

### Email
---
| Command | Description |
| :---: | :---: |
| `thunderbird` | Graphical mail client |
| `evolution` | Graphical mail client |
| `mutt` | Text-based mail client |
| `mail` | Minimal text-based mail client |
| `mailq` | View the outgoing mail queue |

### Web Browsing
---
| Command | Description |
| :---: | :---: |
| `firefox` | Full-featured web browser |
| `lynx` | Text-only web browser |
| `wget` | Download web pages and files |

### Usenet News
---
| Command | Description |
| :---: | :---: |
| `slrn` | Usenet newsreader |

### Instant Messaging
---
| Command | Description |
| :---: | :---: |
| `gaim` | Instant messaging and IRC client |
| `talk` | Unix/Linux chat program |
| `write` | Send messages to a terminal |
| `mesg` | Block or allow messages from `talk` or `write` |

### Screen Output
---
| Command | Description |
| :---: | :---: |
| `echo` | Print text to standard output |
| `printf` | Print formatted text to standard output |
| `yes` | Repeat text until stopped |
| `seq` | Print a sequence of numbers |
| `clear` | Clear the terminal screen |

### Math and Calculations
---
| Command | Description |
| :---: | :---: |
| `xcalc` | Display a graphical calculator |
| `expr` | Perform simple math on the command line |
| `dc` | Command-line calculator |

### Dates and Times
---
| Command | Description |
| :---: | :---: |
| `xclock` | Display a graphical clock |
| `cal` | Print a calendar |
| `date` | Display or set the system date/time |
| `ntpdate` | Sync system time with a remote time server |

### Graphics and Screensavers
---
| Command | Description |
| :---: | :---: |
| `eog` | View graphics files |
| `geeqie` | View graphics files and slideshows |
| `ksnapshot` | Capture screenshots |
| `gimp` | Edit graphics files |
| `dia` | Create structured diagrams |
| `gnuplot` | Create graphs and plots |
| `xscreensaver` | Run a screensaver |

### Audio
---
| Command | Description |
| :---: | :---: |
| `amarok`, `rhythmbox`, `xmms` | Audio players (MP3, WAV, OGG) |
| `grip` | CD player, ripper, and encoder |
| `cdparanoia` | Rip audio from CDs |
| `lame` | Convert WAV to MP3 |
| `id3tag` | Edit ID3 tags |
| `audacity` | Edit audio files |
| `k3b` | Burn CDs and DVDs |

### Video
---
| Command | Description |
| :---: | :---: |
| `mplayer` | Play video files |
| `gxine` | DVD player |
| `kino` | Edit video files |
| `HandBrake` | Rip and convert videos |

### Network
---
| Command | Description |
| :---: | :---: |
| `traceroute` | Show the network path to a remote host |
| `ifconfig` | (Deprecated) Manage network interfaces |
| `netstat` | Show network connections |
| `tcpdump` | Analyze network packets</br>Example: tcpdump -i eth0 captures all network traffic on the interface eth0 |
| `ping` | Test connectivity to a host |
| `ifup/ifdown` | Activate/deactivate network interfaces</br>Example:</br>ifup eth0 brings the eth0 interface up.</br>ifdown eth0 brings it down. |
| `nslookup` | Query DNS servers |
| `dig` | (Domain Information Groper) Query DNS records |
| `mtr` | Combines `traceroute` and `ping` for network diagnostics |
