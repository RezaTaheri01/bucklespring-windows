# Bucklespring-Windows

Windows version of [Bucklespring](https://github.com/zevv/bucklespring) repository, with great help from **ChatGPT**.

## 📦 Installation

### Option 1: Without Installation

1. Run `Bucklespring.exe` from the **App** directory and enjoy! 😊

### Option 2: Manual Installation

1. Install **Python** (if not already installed).
2. Open the terminal in the root of the project directory.
3. Install and create a virtual environment:

    ```bash
    python -m pip install virtualenv
    ```

    ```bash
    python -m virtualenv venv
    ```

4. Activate the virtual environment:

    ```bash
    cd venv/Scripts/
    activate
    ```

5. Go back to the project root:

    ```bash
    cd ../..
    ```

6. Upgrade **pip**:

    ```bash
    python.exe -m pip install --upgrade pip
    ```

7. Install the required packages from `req.txt`:

    ```bash
    pip install -r req.txt
    ```

8. Run the project file:

    ```bash
    python Bucklespring.py
    ```

## ⚠️ Attention

- To **exit** the app, press `Ctrl + Esc`.
- To **mute** the app, press `Alt + M`.

## ✅ Todo

- [x] ~~Stereo sound~~ (Check out `Stereo.py`)
- [x] ~~Mute feature~~
- [X] ~~Improve sounds map~~

## 📚 More Information

For more info, visit [Bucklespring GitHub Repository](https://github.com/zevv/bucklespring).
