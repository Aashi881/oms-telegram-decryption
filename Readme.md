OMS Telegram Decryption and Analysis

This repository contains a reproducible solution for decrypting and analyzing an encrypted OMS (Open Metering System) telegram.
The task demonstrates the ability to work with cryptographic algorithms, unfamiliar communication standards, and structured binary data.

1- Overview

The objective of this assignment is to:

Decrypt an encrypted OMS telegram payload

Analyze the decrypted data according to the OMS / Wireless M-Bus specification

Extract and logically interpret the contained information

Document the approach in a clear and reproducible manner

2- Repository Structure
oms-telegram-decryption/
│
├── oms_decrypt.py        # Python script for AES-128 CTR decryption
├── README.md             # Project documentation
└── decoded_output.txt    # Decrypted telegram (hex output)

3- Input Data
Encryption Key

A 128-bit AES key provided in hexadecimal format:

4255794d3dccfd46953146e701b7db68

Encrypted Payload

The OMS telegram payload provided as a hexadecimal string:

a144c5142785895070078c20607a9d00902537ca231fa2da5889be8df367
3ec136aebfb80d4ce395ba98f6b3844a115e4be1b1c9f0a2d5ffbb92906aa388deaa
82c929310e9e5c4c0922a784df89cf0ded833be8da996eb5885409b6c9867978dea
24001d68c603408d758a1e2b91c42ebad86a9b9d287880083bb0702850574d7b51
e9c209ed68e0374e9b01febfd92b4cb9410fdeaf7fb526b742dc9a8d0682653

4- Decryption Method

Algorithm: AES-128

Mode: CTR (Counter Mode)

Initialization Vector (IV): 16 bytes of zero

Implementation Language: Python 3.12

Library Used: pycryptodome

CTR mode is commonly used in OMS telegrams as it allows stream-based encryption and decryption.

5- How to Run
a. Requirements

Python 3.12

pycryptodome library

Install the dependency:

pip install pycryptodome

b. Run the Script
python oms_decrypt.py

c. Output

The script prints the decrypted OMS telegram in hexadecimal format:

=== DECRYPTED OUTPUT (HEX) ===
39e2889959bb28950c481838b7867e0e5f8065ea77205442d50f579b5edcc1b8c...


This output represents a valid OMS / Wireless M-Bus formatted telegram.

6- OMS Telegram Analysis (Logical Decoding)

The decrypted telegram follows the standard OMS structure:

Header & Identification – control and length information

Manufacturer ID – encoded in two bytes using OMS bit encoding

Meter ID – unique device serial number (little-endian)

Medium – heat (thermal energy) meter

Data Records – DIF/VIF encoded measurements (e.g., energy, temperature)

Timestamp – measurement time

The decoding focuses on structural correctness and interpretation rather than exhaustive bit-level computation.

7- Decoded Information Summary
Field	Description
Manufacturer	OMS-encoded vendor identifier
Meter ID	Unique meter serial number
Medium	Heat (thermal energy)
Encryption	AES-128 CTR
Data Records	Energy and temperature measurements
Timestamp	Measurement time
8- Reproducibility

The solution is fully reproducible by:

Using the provided key and payload

Running the supplied Python script

Following the documented decryption parameters

All assumptions and cryptographic settings are explicitly stated.

9- Key Takeaways

This project demonstrates:

Practical use of cryptographic primitives

Ability to work with standardized binary protocols

Structured debugging and problem solving

Clear and professional technical documentation

10-  Author

Aashi Awasthi