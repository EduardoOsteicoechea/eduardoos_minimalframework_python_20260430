export default function toggle_theme_button_action(button) {
    button.addEventListener("pointerup", () => {
        const current_theme = document.documentElement.getAttribute("data-theme");
        console.log(current_theme)
        if (current_theme === "dark") {
            document.documentElement.setAttribute("data-theme", "light");
        } else {
            document.documentElement.setAttribute("data-theme", "dark");
        }
    });
}