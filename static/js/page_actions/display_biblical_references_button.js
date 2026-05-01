export default function display_biblical_references_button_action(button){    
    button.addEventListener("pointerup", () => {
        const biblical_references = document.querySelectorAll(".bible_quote_reference");
        biblical_references.forEach(element => {
            element.classList.toggle("hidden");
        });
    });
}