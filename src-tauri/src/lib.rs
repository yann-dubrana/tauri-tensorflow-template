use tauri::WindowEvent;
use server::ServerMode;

mod server;

#[tauri::command]
fn greet(name: &str) -> String {
    format!("Hello, {}! You've been greeted from Rust!", name)
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_window_state::Builder::new().build())
        .setup(|app| {
            app.handle().plugin(tauri_plugin_shell::init())?;
            app.handle()
                .plugin(tauri_plugin_log::Builder::new().build())?;
            app.handle()
                .plugin(tauri_plugin_window_state::Builder::default().build())?;
            app.handle().plugin(tauri_plugin_updater::Builder::new().build())?;
            tauri::async_runtime::block_on(server::run(app, ServerMode::MultiFile))?;
            Ok(())
        })
        .on_window_event(|_window, event| match event {
            WindowEvent::Destroyed => {
                let _ = tauri::async_runtime::block_on(server::shutdown());
            }
            _ => {}
        })
        .invoke_handler(tauri::generate_handler![greet])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
