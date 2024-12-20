# Tauri TensorFlow Starter

A template project combining **Tauri**, **Python (TensorFlow)**, **FastAPI**, and **Svelte** to create lightweight
desktop applications with integrated machine learning capabilities.

## Features

- 🖥 **Tauri**: Lightweight desktop application framework.
- 🧠 **TensorFlow**: Use Python to handle machine learning and AI tasks.
- 🚀 **FastAPI**: High-performance API for backend communication.
- 📦 **PyInstaller**: Package Python applications into standalone executables.
- 🌟 **Svelte**: Build reactive and user-friendly UIs.
- 📜 **TypeScript Client**: Auto-generated frontend client using `hey-api`.

---

## Project Structure

```
📂 tauri-tensorflow-template
├── 📁 server          # Python TensorFlow + FastAPI backend
├── 📁 src             # Svelte frontend
├── 📁 src-tauri       # Rust-based Tauri application
└── 📄 README.md       # Documentation
```

---

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/ydubrana/tauri-tensorflow-template.git
   cd tauri-tensorflow-template
   ```

2. **Set Up Backend**

    - Install Python dependencies:

      ```bash
      cd server
      conda create --file environment.yml
      ```

    - Package the backend with PyInstaller using powershell script:

      ```bash
      pnpm run buid-server
      ```

      This will generate an executable with _internals directory for the Python server. Onefile work but it start
      slowest.

3. **Set Up Frontend**

    - Install Node.js dependencies:

      ```bash
      cd frontend
      pnpm install
      ```

    - Generate the TypeScript client:

      ```bash
      pnpm run launch-server
      pnpm run build-server-client
      ```
---

## Usage

1. Launch the app:

   ```bash
      pnpm run tauri dev
   ```

2. The backend server is automatically started and stopped by the Tauri app.

3. Interact with the machine learning model through the Svelte UI.

---

## Contributions

Contributions are welcome! Feel free to open issues and submit pull requests.

---

## License

This project is licensed under the MIT License.
