export function saveSetting(key, value) {
    try {
        // Convert objects/arrays to JSON strings, leave primitives as they are
        const valueToSave = typeof value === 'object' ? JSON.stringify(value) : String(value);
        localStorage.setItem(key, valueToSave);
    } catch (error) {
        console.error("Error saving setting to localStorage:", error);
    }
}