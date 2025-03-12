# PyFetch 🚀
```
                            XXXXXX
                 XXXXXXXXXXXXX   XX XX                                       
           XXXXXX       XX XX     X   X                                     
        XXX             XXXX XXXXXX  XX
      XX XXXXXXXX           XXX XXXXXXX                                     
    XX  XX XX    X     X              XX                                    
   XX   X   XXXXXX     X             XX                                    
   X     X  X   X X XXXX        X XXXXX                       XXX          
   X      XXXXXXXXXX     X XXX X      XXX                     X XXX
   X         XXX             XXX        XX                    X  XX
   X              X            XX        XX                 XXXX X  XXXX
   X               XX            XX       X               X    X   XX  XX
    X                X            X        X            X          XXXXX
     X                XX                  XX           X            XX X
     X                  X                X           X                X XXX
      X                   X           X XX        X                   XX  XX
       XX                  X X      XX   X      X                   XXXXXXX
     XXXXXX                    X XX      X    X                   XXX
   XXX   XXXX X                          X X                   XXX
  XXX    X      XX X  XX X  X      XX  X                     XXX
  X XX   X                   X  X                          XXX
 X  XXX XX                                               XX
XXXXX   X                                              XXX
XX  XX  XX                                           XXX
```
PyFetch - a simple tool to fetch system information. 🖥️

---

## Installation 📥

1️⃣ Clone the repository:
   ```sh
   git clone https://github.com/ganyaowl/pyfetch.git
   cd pyfetch
   ```

2️⃣ Create and activate a virtual environment:
   ```sh
   python -m venv .venv
   .venv\Scripts\Activate  # On Linux use: source .venv/bin/activate  
   ```

3️⃣ Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

---

## Usage ▶️

Run the script with:
```sh
python pyfetch.py
```

---

## ⚡ PyFetch PowerShell Script ⚡
A PowerShell script `pyfetch.ps1` is included to automate the setup and execution of PyFetch.

### ▶️ Running the script
To run the script, open PowerShell in the project directory and use:
```sh
./pyfetch.ps1
```

### 🐞 Debug Mode
To enable debug mode, which provides additional logs, run:
```sh
./pyfetch.ps1 -a
```

### 🌍 Making the script accessible everywhere
To run `pyfetch.ps1` from any directory:

1️⃣ Copy `pyfetch.ps1` to a directory that is in your system's `PATH`, or

2️⃣ Add the script's directory to the `PATH` environment variable:
   ```sh
   [System.Environment]::SetEnvironmentVariable("Path", "$env:Path;C:\path\to\script", [System.EnvironmentVariableTarget]::User)
   ```
   - Replace `C:\path\to\script` with the actual path to `pyfetch.ps1`.
   - Restart PowerShell for changes to take effect.

---

## 🎨 Custom Logo
You can customize the ASCII logo by modifying the `logo.txt` file. 📝 Simply replace its contents with any ASCII art you like. However, make sure to avoid using special symbols or Unicode characters, as they may not be properly displayed.

---

## 📸 Screenshot
![PyFetch Screenshot](https://i.imgur.com/QHYAiZ9.png)

---

## 📜 License
This project is licensed under the MIT License.
