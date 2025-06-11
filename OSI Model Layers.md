<h2 align="center">OSI Model Layers with Data Flow & Applications</h2>

<p align="center"><img src="./src/OSI Model Layers/OSI Model Layers with Data Flow and Applications.png"></p>

#### 7️⃣ Layer 7 – Application :
Interface for software to access network services, handling user interaction and application-specific functions. Sends data to **Layer 6**.

Examples: Web browsers, email clients, FTP, HTTP, SMTP.

#### Key Protocols :
+ `HTTP` (Hypertext Transfer Protocol), `HTTPS` (Hypertext Transfer Protocol Secure) → Web communication, `API`s (Application Programming Interface).
+ `SMTP`  (Simple Mail Transfer Protocol), `IMAP` (Internet Message Access Protocol), `POP3` (Post Office Protocol version 3) → (Email Protocols) Sending & receiving emails.
+ `FTP` (File Transfer Protocol) → Transfers files over networks.
+ `DNS` (Domain Name System) → Converts domain names to IP addresses.

#### 6️⃣ Layer 6 – Presentation :
Converts data into a standardized format, handles encryption & compression. Ensures data is readable across different systems. Passes data to **Layer 5**.

Examples: SSL/TLS (encryption), JPEG/MP3 (compression), ASCII, Unicode.

#### 5️⃣Layer 5 – Session :
Establishes, maintains, and synchronizes communication sessions, ensuring multiple sessions don’t mix. Sends data to **Layer 4**.

Examples: Logging into websites, video calls, managing multiple browser tabs.

#### 4️⃣ Layer 4 – Transport :
Selects transmission protocol and ensures reliable or fast data transfer. Breaks data into smaller units before sending it to **Layer 3**.

#### Key Concepts :
+ `TCP` (Transmission Control Protocol) → Reliable, error-checked, connection-based, ordered delivery.
    + Used for web browsing, file transfer, emails
+ `UDP` (User Datagram Protocol) → Faster, no error-checking, connectionless, unordered delivery.
    + Used for Video streaming, online gaming, VoIP.
+ `Ports` (e.g., `80` for HTTP, `443` for HTTPS, `25` for SMTP).
+ `Data Units` : Data becomes `Segments` (TCP) or `Datagrams` (UDP).
+ `Three-Way Handshake` (TCP Connection Setup) :
    <p align="center"><img src="./src/OSI Model Layers/Three-Way Handshake.png" width="35%"></p>

    + 1️⃣ `SYN` (Synchronize) → Sender/Client requests a connection.
    + 2️⃣ `SYN-ACK` (Synchronize-Acknowledge) → Receiver/Server acknowledges.
    + 3️⃣ `ACK` (Acknowledge) → Sender/Client confirms, connection established.

#### 3️⃣ Layer 3 – Network :
Determines the best route for data using IP addresses (logical addressing). Encapsulates segments/datagrams into packets and sends them to **Layer 2**.

Examples: Routing web requests, determining network paths.

#### Key Protocols :

+ `IP` (Internet Protocol) → Identifies source/destination addresses.

    + `Public` address is used to identify the device on the Internet.
        + Public IP addresses are given by your `ISP` (Internet Service Provider)
    + `Private` address is used to identify a device amongst other devices.

    + `IPv4` for `TCP` (Transmission Control Protocol)

        <p align="center"><img src="./src/OSI Model Layers/IPv4.png" width="50%"></p>

        + An `Octet` is a group of 8 bits (1 byte) used to represent a portion of an IP address.
        + In IPv4, the address is divided into 4 octets (32 bits in total)
        + Each octet is written in decimal separated by dots `.`
        + Each octet ranges from 0 to 255 ( since 8 bits can represent values from 0 to 255 )
        + Example : 192.168.10.15

            | Decimal | Binary Representation | Octet Number |
            |  :--:   |          :--:         |     :--:     |
            |   192   |        11000000       |   1st Octet  |
            |   168   |        10101000       |   2nd Octet  |
            |    10   |        00001010       |   3rd Octet  |
            |    15   |        00001111       |   4th Octet  |

    + `IPv6` for `UDP` (User Datagram Protocol)

        <p align="center"><img src="./src/OSI Model Layers/IPv6.png" width="50%"></p>
        
        + In IPv6, the address is 128 bits long, divided into 16-bit blocks called `hextets` or `segments`, not octets.
        + However, each 16-bit block is further divided into 2 octets (2 bytes).
        + Each block is written in hexadecimal and separated by colons `:`
        + Each block like 2001 or 0db8 represents 16 bits (2 bytes).
        + Example : 2001:0db8:85a3:0000:0000:8a2e:0370:7334</br>

            | Block | Binary Representation |  Octets  |
            | :--:  |         :--:          |   :--:   |
            | 2001  |  0010 0000 0000 0001  | 2 Octets |
            | 0db8  |  0000 1101 1011 1000  | 2 Octets |
            | 85a3  |  1000 0101 1010 0011  | 2 Octets |
            | 0000  |  0000 0000 0000 0000  | 2 Octets |
            | 0000  |  0000 0000 0000 0000  | 2 Octets |
            | 8a2e  |  1000 1010 0010 1110  | 2 Octets |
            | 0370  |  0000 0011 0111 0000  | 2 Octets |
            | 7334  |  0111 0011 0011 0100  | 2 Octets |

+ `ICMP` (Internet Control Message Protocol) → Error reporting (e.g., ping).
+ `ARP` (Address Resolution Protocol) → Maps IP to MAC addresses.
+ `NAT` (Network Address Translation) → Converts private IPs to public IPs.

#### 2️⃣ Layer 2 – Data Link :
Adds MAC addresses (physical addressing) to packets for network device identification. Ensures error-free transmission. Converts packets into frames and sends them to **Layer 1**.

Examples : Ethernet, Wi-Fi, MAC addresses, `NIC` (Network Interface Cards).

#### Key Components :
<p align="center"><img src="./src/OSI Model Layers/MAC.png" width="50%"></p>

+ `MAC` (Media Access Control) Address → Unique identifier for network devices.
    + A twelve-character hexadecimal number (a base sixteen numbering system used in computing to represent numbers) split into two's and separated by a colon.
    + These colons `:` are considered separators.
    + The first six characters represent the company that made the network interface, and the last six is a unique number.
+ Ethernet, Wi-Fi → Physical transmission methods.

#### 1️⃣ Layer 1 – Physical :
Converts binary data into signals for transmission via hardware. Sends signals through physical media (cables, radio waves, fiber optics).

Examples : Cables, radio waves, fiber optics, network adapters.

#### Key Components :
+ Frames & Bits → Data is converted into binary for transmission.

<h2 align="center">Encapsulation and De-Encapsulation in OSI Model</h2>

#### Encapsulation : Adding Headers and Trailers

As data moves down the OSI model layers before transmission, each layer adds a header (and sometimes a trailer) to provide necessary transmission details. This process is called **encapsulation**.

<p align="center"><img src="./src/OSI Model Layers/Encapsulation.jpg" width="75%"></p>

#### Layers 7-5 (7️⃣ Application, 6️⃣ Presentation, 5️⃣ Session)

Has *application*, *presentation*, or *session* header depends on which layer

Data remains as *raw data* for applications (e.g., web pages, emails, files).

#### 4️⃣ Layer 4 (Transport)

Adds *transport* header (contains protocol type, source & destination port numbers, sequencing, and error control).

Data becomes `Segment` (TCP) or `Datagram` (UDP).

#### 3️⃣ Layer 3 (Network)

Adds *network* header (contains source/destination IP addresses to determine routing).

Data becomes a `Packet`.
* a piece of data when it does have IP addressing information

#### 2️⃣ Layer 2 (Data Link)

Adds `MAC` (Media Access Control) addresses in a *frame* header for device identification.

Adds an `FCS` (Frame Check Sequence) error-checking trailer for data integrity and security.

Data becomes a `Frame`.
* a piece of data when it does not have IP addressing information

#### 1️⃣ Layer 1 (Physical)

Converts the Frame into `Bits` (binary data, signals) for transmission.

---
#### De-Encapsulation : Removing Headers and Trailers

When the receiving device gets the data, it reverses the process :
<p align="center"><img src="./src/OSI Model Layers/De-Encapsulation.jpg" width="75%"></p>

#### 1️⃣ Layer 1 (Physical)
→ Converts `Bits` into a `Frame`.

#### 2️⃣ Layer 2 (Data Link)
→ Reads and removes `MAC` addresses, `FCS` error-checking trailer, passes the `Packet` to **Layer 3**.

#### 3️⃣ Layer 3 (Network)
→ Reads and removes IP header, passes the `segment/datagram` to **Layer 4**.

#### 4️⃣ Layer 4 (Transport)
→ Reads port numbers, protocol, reassembles the data.

#### Layers 5-7 (5️⃣ Session, 6️⃣ Presentation, 7️⃣ Application)
→ Finally, data is delivered to the application (e.g., web browser, email client).

#### Key Takeaways

`Encapsulation` : Each layer adds a header (and sometimes a trailer).

Data (Layers 7-5) → Segment/Datagram (Layer 4) → Packet (Layer 3) → Frame (Layer 2) → Bits (Layer 1).

`De-Encapsulation` : The receiving device removes headers to extract the original data.

Bits (Layer 1) → Frame (Layer 2) → Packet (Layer 3) → Segment/Datagram (Layer 4) → Data (Layers 7-5).

#### Terminology :

Security & Integrity: The Data Link layer trailer (FCS) ensures the data hasn’t been corrupted during transmission.

Standardized Communication: Ensures all network-enabled devices, regardless of manufacturer or OS, can communicate reliably using the same process.

<h2 align="center">TCP/IP Model: The Foundation of Modern Networking</h2>

The TCP/IP model is the real-world networking standard. It consists of **four layers**, each handling specific functions :
<p align="center"><img src="./src/OSI Model Layers/TCP_IP Model.png"></p>

#### 4️⃣ Application Layer (End-User Interaction & Services)
Provides network services for applications (e.g., web browsing, email, file transfers).

🔹 Equivalent OSI Layers: Application (7), Presentation (6), Session (5).
#### 3️⃣ Transport Layer (Reliable/Unreliable Data Delivery)
Ensures correct delivery between devices via TCP (reliable, ordered) or UDP (fast, connectionless).

🔹 Equivalent OSI Layer: Transport (4).
    
✅ Ensures lossless, reliable transmission with retransmission of lost data.
#### 2️⃣ Internet Layer (IP Addressing & Routing)
Routes packets across networks using IP addresses (IPv4 / IPv6).

🔹 Equivalent OSI Layer: Network (3).
#### 1️⃣ Network Interface Layer (Physical Data Transmission)
Handles MAC addressing, Ethernet/Wi-Fi communication, and physical media.

🔹 Equivalent OSI Layer: Physical (1), Data Link (2).
#### 🔹 Alternative 5-Layer Model – Some sources split the Network Interface Layer into two :
+ Data Link Layer → Manages error checking (Frames, MAC addresses).
+ Physical Layer → Converts data into electrical signals (Bits, Fiber Optics, Wireless).

#### Data Naming at Each Stage :

+ Application Layer → Data
+ Transport Layer → Segment (TCP) / Datagram (UDP) (adds ports, sequence numbers)
+ Internet Layer → Packet (adds source/destination IP addresses)
+ Network Interface Layer → Frame (adds MAC addresses, error-checking trailer)
+ Physical Transmission → Bits (converted into electrical/light/wireless signals)

✅ Why is encapsulation important?

Standardizes communication across all devices.
Ensures security & integrity (error-checking prevents tampering).
Allows different networks & devices to communicate efficiently.

#### 💡 Why OSI if TCP/IP is Used ?
<p align="center"><img src="./src/OSI Model Layers/OSI vs TCP_IP.png"></p>

+ **OSI Model** (7 Layers) = Learning Tool 📚
– A more detailed, structured breakdown of networking concepts.</br>
+ **TCP/IP** (4 Layers) = Practical Networking 🌍
– A protocol suite defining how data moves across networks.

#### History & Purpose: Why These Models Were Created
Before standardization, different manufacturers had incompatible networking methods.

📅 1982 → TCP/IP introduced by U.S. DoD as a universal networking standard.

📅 Later → OSI model introduced by ISO as a structured guide, but TCP/IP remains the real-world standard.

✅ Standardization allows any device, regardless of OS or manufacturer, to communicate using the same networking rules.