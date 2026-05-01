export default function toggle_theme_button_action(button) {
    button.addEventListener("pointerup", () => {
        const current_theme = document.documentElement.getAttribute("data-theme");
        console.log(current_theme);
        
        // Determine the new theme based on the current one
        const new_theme = current_theme === "dark" ? "light" : "dark";
        
        // Apply the new theme to the DOM
        document.documentElement.setAttribute("data-theme", new_theme);
        
        // Call the generic save method to store the preference
        saveSetting("theme_preference", new_theme);
    });
}