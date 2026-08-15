import { GoogleGenAI } from '@google/genai';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

// Parse .env.local manually
const envPath = path.join('C:', 'Users', 'vicen', 'OneDrive', 'Escritorio', 'EVA IPSS', 'academy-portal', '.env.local');
const envContent = fs.readFileSync(envPath, 'utf8');
const envLines = envContent.split('\n');
for (const line of envLines) {
  const match = line.match(/^([^=]+)=(.*)$/);
  if (match) {
    process.env[match[1].trim()] = match[2].trim();
  }
}

const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });
const REFS_DIR = path.join('C:', 'Users', 'vicen', 'OneDrive', 'Escritorio', 'EVA IPSS', '.agents', 'skills', 'eva-presentation-generator', 'references');

const prompt = `Translate the following markdown text from Chinese to Spanish. 
Preserve all markdown formatting exactly as it is, including frontmatter, code blocks, tables, bold text, links, and HTML placeholders (like {{ variable }}). 
Do NOT translate any code, file paths, or CSS class names. Only translate the human-readable documentation.
Output ONLY the translated markdown, no preamble or explanation.`;

async function getFiles(dir) {
  const dirents = await fs.promises.readdir(dir, { withFileTypes: true });
  const files = await Promise.all(dirents.map((dirent) => {
    const res = path.resolve(dir, dirent.name);
    return dirent.isDirectory() ? getFiles(res) : res;
  }));
  return Array.prototype.concat(...files);
}

async function translateFile(filePath) {
  if (!filePath.endsWith('.md')) return;
  
  console.log(`Translating: ${filePath}`);
  const content = await fs.promises.readFile(filePath, 'utf-8');
  
  // If the file does not have chinese characters (or is very short), we could skip, but let's translate all
  
  try {
    const response = await ai.models.generateContent({
        model: 'gemini-1.5-flash',
        contents: prompt + "\n\n" + content,
        config: {
            temperature: 0.1
        }
    });
    
    let translatedText = response.text;
    if (translatedText.startsWith('```markdown')) {
        translatedText = translatedText.replace(/^```markdown\n/, '').replace(/\n```$/, '');
    }

    await fs.promises.writeFile(filePath, translatedText, 'utf-8');
    console.log(`✅ Translated: ${filePath}`);
  } catch (error) {
    console.error(`❌ Failed to translate ${filePath}:`, error.message);
  }
}

async function main() {
  console.log("Fetching files from:", REFS_DIR);
  const files = await getFiles(REFS_DIR);
  const mdFiles = files.filter(f => f.endsWith('.md'));
  console.log(`Found ${mdFiles.length} markdown files.`);
  
  for (let i = 0; i < mdFiles.length; i++) {
      console.log(`[${i+1}/${mdFiles.length}]`);
      await translateFile(mdFiles[i]);
      // add delay to avoid rate limit
      await new Promise(r => setTimeout(r, 2000));
  }
  console.log("Translation complete!");
}

main();
