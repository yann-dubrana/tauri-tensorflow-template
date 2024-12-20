use anyhow::Result;
use command_group::{CommandGroup, GroupChild};
use lazy_static::lazy_static;
use std::process::Command;
use std::sync::Mutex;
use tauri_plugin_shell::process::Command as TauriCommand;
use tauri_plugin_shell::ShellExt;

/// Represents the state of the Python server
#[derive(Debug)]
struct PythonServer {
    processes: Option<GroupChild>,
}

impl PythonServer {
    fn new() -> Self {
        Self { processes: None }
    }

    fn start(&mut self, app: &tauri::App) {
        //https://github.com/tauri-apps/tauri/discussions/3273

        let sidecar: TauriCommand = app
            .shell()
            .sidecar("tensorflow-server")
            .expect("Failed to get SIDECAR");

        self.processes = Option::from(
            Command::from(sidecar)
                .group_spawn()
                .expect("Failed to spawn process"),
        )
    }

    fn shutdown(&mut self) -> Result<()> {
        if let Some(mut processes) = self.processes.take() {
            processes.kill()?;
        }
        Ok(())
    }
}

// Create a global static instance wrapped in a Mutex
lazy_static! {
    static ref SERVER: Mutex<PythonServer> = Mutex::new(PythonServer::new());
}

/// Initialize and run the server with proper error handling
pub async fn run(app: &tauri::App) -> Result<()> {
    // Lock the mutex and start the server
    let mut server = SERVER
        .lock()
        .map_err(|e| anyhow::anyhow!("Failed to lock server: {}", e))?;
    server.start(app);
    Ok(())
}

/// Shutdown the server with proper error handling
pub async fn shutdown() -> Result<()> {
    // Lock the mutex and shutdown the server
    let mut server = SERVER
        .lock()
        .map_err(|e| anyhow::anyhow!("Failed to lock server: {}", e))?;
    server.shutdown()
}
