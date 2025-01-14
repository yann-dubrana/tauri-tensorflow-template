# Tauri TensorFlow Starter

A template project combining **Tauri**, **Python (TensorFlow)**, **FastAPI**, and **Svelte** to create lightweight
desktop applications with integrated machine learning capabilities.

## Features

- 🖝 **Tauri**: Lightweight desktop application framework.
- 🧠 **TensorFlow**: Use Python to handle machine learning and AI tasks.
- 📡 **TensorFlow-GPU**: Using a version of TensorFlow with GPU capabilities for Windows.
- 🚀 **FastAPI**: High-performance API for backend communication.
- 📦 **PyInstaller**: Package Python applications into standalone executables.
- 🌟 **Svelte**: Build reactive and user-friendly UIs.
- 🔛 **TypeScript Client**: Auto-generated frontend client using `hey-api`.

---

## Project Structure

```
🗂 tauri-tensorflow-template
├── 🗁 server          # Python TensorFlow + FastAPI backend
├── 🗁 src             # Svelte frontend
├── 🗁 src-tauri       # Rust-based Tauri application
└── 📄 README.md       # Documentation
```

---

## Installation

### 1. **Prerequisites: GPU Capabilities**

To enable GPU capabilities for TensorFlow, you must install the following NVIDIA components and add their paths to the
system environment variables:
Maybe try with only 12.6 and cudnn 9.6 first and if it doesn't work try with 11.8 and cudnn 8.9

#### **Install CUDA and cuDNN**

- [CUDA 11.8](https://developer.nvidia.com/cuda-11-8-0-download-archive)
- [CUDA 12.6](https://developer.nvidia.com/cuda-12-6-2-download-archive)
- [cuDNN 8.9](https://developer.nvidia.com/rdp/cudnn-archive#a-collapse897-120)
- [cuDNN 9.6](https://developer.nvidia.com/cudnn-downloads) (Requires an NVIDIA account to download.)

#### **Add to `PATH`**

After installation, ensure the following directories are added to your system's `PATH` environment variable:

```plaintext
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\8.9.7\bin
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\bin
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\bin
C:\Program Files\NVIDIA\CUDNN\v9.6\bin
```

---

### 2. **Clone the Repository**

```bash
git clone https://github.com/ydubrana/tauri-tensorflow-template.git
cd tauri-tensorflow-template
```

---

### 3. **Set Up the Backend**

#### Install Python Dependencies:

Use Conda to create the required environment from the `environment.yml` file:

```bash
cd src-python
conda create --file environment.yml
conda activate tauri-tensorflow
```

#### **Verify Installation**

To confirm the installation:

1. Open a terminal and run:
   ```bash
   nvcc --version
   ```
   This will display the version of CUDA installed.

2. Check that TensorFlow detects the GPU:
   ```python
   python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
   ```

#### Package the Backend:

Use the provided PowerShell script to bundle the server into an executable using PyInstaller:

```bash
pnpm run build-src-python
```

This will generate the server executable along with the required Python runtime.

---

### 4. **Set Up the Frontend**

#### Install Node.js Dependencies:

Navigate to the `frontend` directory and install the required packages:

```bash
cd frontend
pnpm install
```

#### Generate the TypeScript Client:

Start the backend server and build the API client for the frontend:

```bash
pnpm run launch-server
pnpm run build-server-client
```

---

### 5. **Run the Application**

1. Start the Tauri application in development mode:

   ```bash
   pnpm run tauri dev
   ```

2. The backend server will automatically start and stop with the Tauri application.

3. Interact with the TensorFlow model via the Svelte-based UI.

---

### 6. **Package the Application**

To package the application for distribution, i have created a github actions that will build the application for
windows.
This is compatible with Tauri updater and public realease in private repository.
Feel free to open an issue if you want to know more about it.


### Notes:

- Ensure all required dependencies are installed correctly for both the backend and frontend.
- I'll be more than happy if someone can help me to make this project work on WSL, Linux, MacOS.
- On windows, WSL we'll be a great addition to use more modern tensorflow versions.
- Contributions are welcome! Feel free to open issues and submit pull requests.

--- 

## License

This project is licensed under the MIT License.

