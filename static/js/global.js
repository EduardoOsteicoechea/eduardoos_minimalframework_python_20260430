/**
 * Retrieves a setting from localStorage.
 * @param {string} key - The name of the setting.
 * @returns {any} The parsed value or null if not found.
 */
export function getSetting(key) {
    try {
        const value = localStorage.getItem(key);
        if (value === null) return null;
        // Try to parse JSON (for objects), otherwise return the string
        try { return JSON.parse(value); } catch { return value; }
    } catch (error) {
        console.error("Error reading setting from localStorage:", error);
        return null;
    }
}

/**
 * Saves any setting to localStorage.
 * @param {string} key - The name of the setting.
 * @param {any} value - The value to save.
 */
export function saveSetting(key, value) {
    try {
        const valueToSave = typeof value === 'object' ? JSON.stringify(value) : String(value);
        localStorage.setItem(key, valueToSave);
    } catch (error) {
        console.error("Error saving setting:", error);
    }

/**
 * Checks for a saved theme and applies it to the document.
 * If no saved theme exists, it defaults to the system preference.
 */
export function initializeTheme() {
    let current_theme = getSetting("theme_preference");
    
    // If the user hasn't saved a preference yet, check their OS preference
    if (!current_theme) {
        const systemPrefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
        current_theme = systemPrefersDark ? "dark" : "light";
    }
    
    // Force the data-theme attribute on load so the CSS kicks in immediately
    document.documentElement.setAttribute("data-theme", current_theme);
}

// Run this immediately when the script loads so the page doesn't flash the wrong colors
initializeTheme();