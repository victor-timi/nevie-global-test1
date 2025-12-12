/**
 * n8n Function/Code Node - Recommendation Generator
 *
 * This code should be placed in the Function/Code node in your n8n workflow.
 * It generates a recommendation based on the summary from the API response.
 *
 * Configuration:
 * - Language: JavaScript
 * - Mode: Run Once for All Items
 *
 * Input: Summary from HTTP Request node (API response)
 * Output: Recommendation object
 */

const summary = $input.first().json.summary;

// Clean double quotes to avoid JSON parsing issues
const cleanSummary = summary.replace(/"/g, "'");

// Generate recommendation based on summary
const recommendation = `Based on the summary '${cleanSummary}', I recommend reviewing the key points and taking appropriate action.`;

return { recommendation };
