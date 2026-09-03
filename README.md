📱 SharePY

SharePY is a lightweight Python command-line tool for transferring files between devices over a local Wi-Fi/HotSpot network using a direct TCP connection.

It does not require an internet connection. One device acts as the sender, while the other acts as the receiver.

✨ Features

- 📤 Send files over a local network.
- 📥 Receive files and save them automatically.
- ⚡ Uses TCP sockets for reliable file transfer.
- 📊 Displays transfer progress.
- 📦 Uses a 1 MB transfer buffer.
- 🌐 Works over Wi-Fi or a mobile HotSpot.
- 🐍 Built with Python's standard library.
- 🔌 No external Python packages required.

📋 Requirements

- Python 3.x
- Two devices connected to the same Wi-Fi network or HotSpot.
- Permission to read/write the selected files and destination directory.

🚀 Installation

Clone the repository:
```text
git clone https://github.com/MahamedDev/SharePY.git
cd SharePY
```
No external dependencies are required.

Run the program:

python3 sharepy.py

📤 Sending a File

First, run SharePY on the device that will receive the file.

```text
1- send
2- receive
Enter Num : 2
```
The receiver will start listening on TCP port "4444".

Then, run SharePY on the device that will send the file.

```text
1- send
2- receive
Enter Num : 1
Enter Path file : /path/to/file
```
The received file will be saved in:

/sdcard/SharePY/

🌐 Network Configuration

The sender currently connects to:
```text
192.168.43.1:4444
```
This IP address is commonly used by some Android HotSpot configurations, but it may be different depending on your device or network.

If the receiver uses a different IP address, change:
```text
soc.connect(("192.168.43.1", 4444))
```
to the receiver's local IP address.

The receiver listens on:
```text
0.0.0.0:4444
```
which allows incoming connections through the available network interfaces.

📊 Transfer Progress

During a file transfer, SharePY displays the approximate progress.
```text
Sender:

File sent : 25 %

Receiver:

File received : 25 %
```
When the transfer is complete, the sender displays:
```text
[+] File has been sent
```
The receiver displays:
```text
[+] File saved in /sdcard/SharePY/example.zip
```
⚠️ Security Notice

SharePY is designed for use on trusted local networks.

The current implementation does not provide:

- Encryption
- Authentication
- User verification
- File integrity verification
- Access control

Anyone who can reach the receiver's listening port may potentially connect to it.

Do not expose port "4444" to an untrusted network or the public internet.

🔧 Technical Details

SharePY uses only Python's standard library.

Main components include:

- "socket" for TCP networking.
- "os" for file and path operations.
- TCP port "4444".
- A "1 MB" buffer for file transfer.
- A simple metadata header containing the file name and file size.

The metadata format is:
```text
filename§filesize§
```
The receiver extracts the file name and size from the metadata and writes the received data to the output file.

📌 Limitations

- Only one client is accepted at a time.
- Both devices must be able to communicate over the local network.
- The sender currently uses a fixed receiver IP address.
- File names are not sanitized.
- There is no encryption or authentication.
- There is no file integrity verification.
- The current protocol is intended for simple local file transfers.

📜 License

This project is licensed under the MIT License.

See ""LICENSE"" (LICENSE) for more information.

👨‍💻 Author

MahamedDev

---

⭐ If you find SharePY useful, consider giving the repository a star.
which allows incoming connections through the available network interfaces.
