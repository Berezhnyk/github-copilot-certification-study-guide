// Exercise 3: String Manipulation
// Task: Create a function that validates and formats phone numbers

// Function to validate and format phone numbers
// Accepts various formats: (123) 456-7890, 123-456-7890, 1234567890
// Returns formatted as: (123) 456-7890
// Returns null for invalid numbers
function formatPhoneNumber(phoneNumber) {
    /**
     * Format and validate phone numbers
     * @param {string} phoneNumber - Phone number in various formats
     * @returns {string|null} - Formatted phone number or null if invalid
     */
    // TODO: Let Copilot complete this implementation
}

// Test cases
if (typeof module !== 'undefined' && module.exports) {
    module.exports = formatPhoneNumber;
} else {
    // Browser/Node.js testing
    console.log("Testing phone number formatter:");
    console.log(formatPhoneNumber("1234567890"));        // Expected: "(123) 456-7890"
    console.log(formatPhoneNumber("123-456-7890"));      // Expected: "(123) 456-7890"
    console.log(formatPhoneNumber("(123) 456-7890"));    // Expected: "(123) 456-7890"
    console.log(formatPhoneNumber("123.456.7890"));      // Expected: "(123) 456-7890"
    console.log(formatPhoneNumber("123"));                // Expected: null
    console.log(formatPhoneNumber("12345678901"));       // Expected: null
    console.log(formatPhoneNumber("abc-def-ghij"));      // Expected: null
}
