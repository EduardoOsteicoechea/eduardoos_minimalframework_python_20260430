// Add this to the VERY TOP of toggle_theme_button.js
import { saveSetting } from '/static/js/global.js'; 

export default function toggle_theme_button_action(button) {
    button.addEventListener("pointerup", () => {
        const current_theme = document.documentElement.getAttribute("data-theme");
        
        // Determine the new theme based on the current one
        const new_theme = current_theme === "dark" ? "light" : "dark";
        
        // Apply the new theme to the DOM
        document.documentElement.setAttribute("data-theme", new_theme);
        
        // Call the save method (now it knows what this is!)
        saveSetting("theme_preference", new_theme);
    });
}