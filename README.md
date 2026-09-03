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

git clone https://github.com/MahamedDev/SharePY.git
cd SharePY

No external dependencies are required.

Run:

python3 sharepy.py

📤 Sending a File

On the device that will receive the file:

1- send
2- receive
Enter Num : 2

The receiver starts listening on TCP port "4444".

Then, on the sending device:

1- send
2- receive
Enter Num : 1
Enter Path file : /path/to/file

The file will be transferred to:

/sdcard/SharePY/

🌐 Network Configuration

The current sender configuration connects to:

192.168.43.1:4444

This address is commonly associated with Android HotSpot configurations, but it may be different depending on the device and network.

If your network uses another address, change:

soc.connect(("192.168.43.1", 4444))

to the receiver's local IP address.

The receiver listens on:

0.0.0.0:4444

which allows connections through available network interfaces.

📊 Transfer Progress

During a transfer, SharePY displays the approximate progress:

File sent : 25 %
File received : 25 %

and after completion:

[+] File has been sent

or:

[+] File saved in /sdcard/SharePY/example.zip

⚠️ Security Notice

SharePY is designed for trusted local networks.

The current implementation does not provide:

- Encryption
- Authentication
- User verification
- File integrity verification
- Access control

Anyone who can reach the listening port may potentially connect to the receiver.

Do not expose port "4444" to an untrusted network or the public internet.

🔧 Technical Details

SharePY uses:

- "socket" for TCP networking.
- "os" for file and path operations.
- TCP port "4444".
- A "1 MB" buffer for file data.
- A simple metadata header containing:

filename§filesize§

The receiver uses the declared file size to determine transfer information and writes the received bytes to the output file.

📌 Limitations

- Only one client is accepted at a time.
- Both devices must have network connectivity to each other.
- The sender currently uses a fixed receiver IP address.
- File names are not sanitized.
- There is no encryption or authentication.
- The current protocol is intended for simple local file transfers.

📜 License

This project is licensed under the MIT License.

See ""LICENSE"" (LICENSE) for more information.

👨‍💻 Author

MahamedDev

---

⭐ If you find SharePY useful, consider giving the repository a star.
