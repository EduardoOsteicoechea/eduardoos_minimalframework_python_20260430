import toggle_theme_button_action from "./toggle_theme_button.js"
import display_biblical_references_button_action from "./display_biblical_references_button.js"

const page_actions_button = document.getElementById("page_actions_button");
const page_actions_main_container = document.getElementById("page_actions_main_container");
const toggle_theme_button = document.getElementById("toggle_theme_button");
const display_biblical_references_button = document.getElementById("display_biblical_references_button");

toggle_theme_button_action(toggle_theme_button)
display_biblical_references_button_action(display_biblical_references_button)

page_actions_button.addEventListener("pointerup", () => {
    toggle_action_buttons_container(page_actions_main_container);
    toggle_page_actions_menu_button_style(page_actions_button);
});

function toggle_action_buttons_container(container) {
    const container_display_value = container.style.display;
    if (container_display_value === "none" || container_display_value === "") {
        container.style.display = "flex";
    } else {
        container.style.display = "none";
    }
}

function toggle_page_actions_menu_button_style(button) {
    const unactive = "page_actions_button_unactive";
    const active = "page_actions_button_active";
    button.classList.toggle(active);
    button.classList.toggle(unactive);
}