import fs from 'fs';
import path from 'path';

// Parse .env.local manually
const envPath = path.join('C:', 'Users', 'vicen', 'OneDrive', 'Escritorio', 'EVA IPSS', 'academy-portal', '.env.local');
const envContent = fs.readFileSync(envPath, 'utf8');
for (const line of envContent.split('\n')) {
  const match = line.match(/^([^=]+)=(.*)$/);
  if (match) process.env[match[1].trim()] = match[2].trim();
}

const API_KEY = process.env.GEMINI_API_KEY;

async function checkModels() {
  const url = `https://generativelanguage.googleapis.com/v1beta/models?key=${API_KEY}`;
  try {
    const res = await fetch(url);
    const data = await res.json();
    if (data.models) {
        data.models.filter(m => m.supportedGenerationMethods.includes('generateContent')).forEach(m => console.log(m.name));
    }
  } catch(e) {
    console.error("Fetch failed:", e);
  }
}

checkModels();
