# Mission 7 — How computers communicate

## 1. Task / objective
The objective of Mission 7 is to explore computer networking fundamentals, examine network topologies and protocols, observe live network diagnostic utilities from the Terminal, and trace the end-to-end journey of web traffic when navigating to an internet domain. This involves:
1. Defining and illustrating eight foundational networking concepts (LAN, MAN, WAN, DNS, Router, Protocol, Packet Switching, Client-Server).
2. Performing live network connectivity (`ping`) and Domain Name System resolution (`nslookup`) queries against a public test host while sanitizing private network details.
3. Explaining the purpose of connectivity diagnostics and the critical function of DNS.
4. Documenting a comprehensive, 6-step end-to-end sequence tracing what happens from the moment a user types a URL into a browser until the rendered page appears.

---

## 2. Work completed
- **Task 7.1 (Network Concepts Table)**: Compiled definitions in original words and provided real-world examples for all eight core networking concepts.
- **Task 7.2 (Network Diagnostics & Privacy-Safe Observations)**:
  - Executed `ping -c 3 example.com` to verify round-trip network connectivity, latency, and packet integrity (0% packet loss, ~27.7 ms average latency).
  - Executed `nslookup example.com` to observe DNS resolution from domain name to IPv4 addresses (`104.20.23.154`, `172.66.147.243`).
  - Answered all three analytical questions regarding connectivity tests and DNS architecture.
  - Sanitized local private network IP addresses and ISP routing identifiers to preserve privacy.
- **Task 7.3 (Website Lifecycle Trace)**: Authored a detailed 6-step walkthrough demonstrating the interaction between the client, DNS resolvers, intermediate routers, transport protocols, and web server software.
- **Documentation**: Completed this `README.md` following the required 8-section template.

---

## 3. Commands / tools used
| Tool / Utility | Invocation | Purpose |
| :--- | :--- | :--- |
| `ping` | `ping -c 3 example.com` | Transmitted ICMP ECHO_REQUEST packets to measure round-trip reachability and packet loss. |
| `nslookup` | `nslookup example.com` | Queried internet Domain Name System servers for domain A-records. |
| Text Editor | Markdown editing | Formatted tables and structured networking explanations. |

---

## 4. My understanding

### Task 7.1 — Explain network concepts

#### Network Concepts Table
| Concept | Explain it in your own words | Example |
| :--- | :--- | :--- |
| **LAN (Local Area Network)** | A privately owned high-speed network confined to a limited geographical area such as a single home, computer laboratory, or office suite. | A home Wi-Fi network interconnecting a laptop, smartphone, wireless printer, and smart TV. |
| **MAN (Metropolitan Area Network)** | A high-bandwidth network infrastructure spanning an entire town, municipality, or large multi-building educational campus. | A university campus network connecting all academic department buildings and student libraries via underground fiber optics. |
| **WAN (Wide Area Network)** | A telecommunications network spanning vast geographic distances across regions, entire countries, or the entire globe. | The global Internet, linking thousands of autonomous commercial, educational, and governmental networks worldwide. |
| **DNS (Domain Name System)** | The distributed naming directory of the internet that translates human-friendly textual hostnames into computer-routable numerical IP addresses. | Translating `example.com` into the target web server IPv4 address `104.20.23.154`. |
| **Router** | A specialized network layer (Layer 3) hardware device that inspects packet headers and forwards data packets between different IP subnets along optimal routes. | A home broadband gateway router directing outbound traffic from a home LAN to an Internet Service Provider (ISP) WAN connection. |
| **Protocol** | An established, standardized set of technical rules, formatting conventions, and error-handling procedures that allow dissimilar electronic devices to communicate reliably. | Hypertext Transfer Protocol Secure (HTTPS), which defines how encrypted web resources are requested and served over port 443. |
| **Packet switching** | A communication methodology where large digital messages are fragmented into discrete chunks (packets), independently routed across dynamic network links, and reassembled at the destination. | TCP/IP packet transmission across internet routers, allowing multiple users to share physical bandwidth dynamically without dedicated circuits. |
| **Client-server** | A distributed computing architecture in which service consumers (clients) initiate requests over a network, and centralized providers (servers) process requests and return responses. | A desktop web browser (client) requesting an HTML document from a remote cloud web server (server). |

---

### Task 7.2 — Observe network information

#### 1. Live Connectivity Observation (`ping`)
```text
$ ping -c 3 example.com
PING example.com (104.20.23.154): 56 data bytes
64 bytes from 104.20.23.154: icmp_seq=0 ttl=55 time=30.199 ms
64 bytes from 104.20.23.154: icmp_seq=1 ttl=55 time=32.603 ms
64 bytes from 104.20.23.154: icmp_seq=2 ttl=55 time=20.483 ms

--- example.com ping statistics ---
3 packets transmitted, 3 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 20.483/27.762/32.603/5.240 ms
```

#### 2. Live DNS Lookup Observation (`nslookup`)
```text
$ nslookup example.com
Server:		[redacted-local-dns]
Address:	[redacted]#53

Non-authoritative answer:
Name:	example.com
Address: 104.20.23.154
Name:	example.com
Address: 172.66.147.243
```
*(Note: Local DNS resolver and private IP metadata have been redacted for privacy.)*

#### 3. Analytical Answers:
- **What a connectivity test helps you check**:
  A connectivity utility (like `ping`, which uses ICMP Echo Request and Echo Reply messages) tests whether a remote network device is reachable across the intervening network path. It provides three critical diagnostics: (1) whether the remote server is online and responding, (2) the round-trip latency time in milliseconds required for a signal to reach the destination and return, and (3) network link stability, measured by the percentage of dropped packets (packet loss).
- **What information a DNS lookup displays**:
  A DNS lookup utility (like `nslookup` or `dig`) reveals the address records associated with a given domain name. It displays the identity and port of the local DNS resolver contacted (typically on port 53), whether the response is authoritative or cached, the canonical hostname (`Name`), and the corresponding IPv4 (`A` records) or IPv6 (`AAAA` records) assigned to that host.
- **The role of DNS when you enter a website name in a browser**:
  When a user types a human-readable URL (such as `example.com`) into a browser, the browser cannot directly send network packets using text characters because internet routing operates purely on numerical IP addresses. DNS acts as the essential translation service: the browser queries the DNS subsystem to resolve the textual domain name into its binary/decimal IP address (`104.20.23.154`). Only once this address is obtained can the client construct and route IP packets to the correct physical destination server.

---

### Task 7.3 — What happens when you open a website?
Here is the step-by-step lifecycle tracing a web transaction using proper terminology (**client**, **server**, **DNS**, and **protocol**):

1. **Step 1: User Request & Client URL Parsing**
   The user enters a URL (e.g., `https://example.com`) into the web browser (**client**). The browser parses the string to identify the transfer **protocol** (`https`), the destination domain name (`example.com`), and the default destination port (port 443 for HTTPS).
2. **Step 2: DNS Resolution**
   The **client** checks its local browser cache and operating system resolver cache to see if the IP address for `example.com` is already known. If not, it dispatches a recursive **DNS** query to the configured local resolver. The **DNS** resolver navigates the root, TLD (`.com`), and authoritative nameservers, ultimately returning the IP address (`104.20.23.154`) to the **client**.
3. **Step 3: Establishing the Transport Protocol Connection (TCP & TLS)**
   Armed with the destination IP address, the **client** initiates a connection using the Transmission Control **Protocol** (TCP). It conducts a three-way handshake (`SYN`, `SYN-ACK`, `ACK`) with the destination **server**. For secure HTTPS, the client and server then perform a Transport Layer Security (TLS) cryptographic handshake to negotiate cipher suites and establish an encrypted session.
4. **Step 4: Packet Switching & Router Forwarding**
   The client's network layer encapsulates the HTTP request into discrete IP packets. These packets are transmitted through the local home gateway **router**, which directs them through a series of intermediate ISP and transit routers across the Wide Area Network using packet switching. Each router inspects the packet destination IP and forwards it along the optimal path.
5. **Step 5: Server Processing & HTTP Response**
   The packets arrive at the destination web **server**'s network interface and are reassembled into the complete HTTP GET request. The web server daemon processes the request, locates the requested HTML, CSS, or API assets, and transmits an HTTP 200 OK response containing the payload data back across the network to the **client**.
6. **Step 6: Client Rendering & Display**
   The **client** browser receives the incoming response stream, parses the HTML into a Document Object Model (DOM), parses CSS into the CSSOM, executes any client-side JavaScript, and paints the formatted web page onto the user's screen.

---

## 5. Difficulties faced
- **Sandbox Network Constraints**: In restricted terminal environments, network queries can fail or hang if outbound sockets are blocked. Recognizing that network commands must be tested with appropriate permissions was essential.
- **Privacy Masking**: Public commands like `nslookup` display the active local router IPv6 address and Wi-Fi interface by default, requiring deliberate sanitation to avoid publishing home network topology.

---

## 6. How I resolved them
- **Validated Network Reachability**: Executed diagnostic commands with network permissions, confirming clean ICMP packet transmission and instantaneous DNS resolution.
- **Redaction of Sensitive Identifiers**: Replaced local gateway addresses with `[redacted-local-dns]` while retaining public test host IP records (`104.20.23.154`) for technical accuracy.

---

## 7. Evidence / files
- Mission 7 Documentation: [mission-07-networking/README.md](README.md)
- Root Overview: [README.md](../README.md)

---

## 8. Commit details
- **Commit Message**: `Explain networking concepts and website communication`
- **Target Branch**: `main`
- **Remote Visibility**: Staged, committed locally, and pushed to remote GitHub repository `https://github.com/Harshit-2208/digital-detective-8450`.
