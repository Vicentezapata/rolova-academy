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
// Using gemini-flash-latest
const URL = `https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent?key=${API_KEY}`;
const REFS_DIR = path.join('C:', 'Users', 'vicen', 'OneDrive', 'Escritorio', 'EVA IPSS', '.agents', 'skills', 'eva-presentation-generator', 'references');

const systemInstruction = `Translate the following markdown text from Chinese to Spanish. 
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

const delay = ms => new Promise(res => setTimeout(res, ms));

async function translateFile(filePath, attempt = 1) {
  if (!filePath.endsWith('.md')) return true;
  
  const content = await fs.promises.readFile(filePath, 'utf-8');
  // Skip if it doesn't contain Chinese characters
  if (!/[\u4e00-\u9fa5]/.test(content)) {
      console.log(`⏭️ Skipped (no Chinese detected): ${path.basename(filePath)}`);
      return true;
  }
  
  const payload = {
    contents: [{ role: "user", parts: [{ text: systemInstruction + "\n\n" + content }] }],
    generationConfig: { temperature: 0.1 }
  };

  try {
    const res = await fetch(URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    
    if (!res.ok) {
        if (res.status === 429 || res.status === 503) {
            console.warn(`⚠️ Rate limit (${res.status}) on ${path.basename(filePath)}. Retrying in 10s (attempt ${attempt})...`);
            await delay(10000);
            if (attempt < 5) return translateFile(filePath, attempt + 1);
        }
        console.error(`❌ API error ${res.status} for ${path.basename(filePath)}`);
        return false;
    }
    
    const data = await res.json();
    if (data.error) {
       console.error(`❌ Failed to translate ${path.basename(filePath)}:`, data.error.message);
       return false;
    }

    if (data.candidates && data.candidates[0].content && data.candidates[0].content.parts[0].text) {
        let translatedText = data.candidates[0].content.parts[0].text;
        if (translatedText.startsWith('```markdown')) {
            translatedText = translatedText.replace(/^```markdown\n/, '').replace(/\n```$/, '');
        }
        await fs.promises.writeFile(filePath, translatedText, 'utf-8');
        console.log(`✅ Translated: ${path.basename(filePath)}`);
        return true;
    } else {
        console.error(`❌ No valid response for ${path.basename(filePath)}`);
        return false;
    }
  } catch (error) {
    console.error(`❌ Network/parse error on ${path.basename(filePath)}:`, error.message);
    if (attempt < 3) {
        await delay(5000);
        return translateFile(filePath, attempt + 1);
    }
    return false;
  }
}

async function main() {
  console.log("Fetching files from:", REFS_DIR);
  const files = await getFiles(REFS_DIR);
  const mdFiles = files.filter(f => f.endsWith('.md'));
  console.log(`Found ${mdFiles.length} markdown files.`);
  
  // Execute sequentially with 4s delay to stay under 15 RPM
  let successCount = 0;
  for (let i = 0; i < mdFiles.length; i++) {
      console.log(`[${i+1}/${mdFiles.length}] Processing ${path.basename(mdFiles[i])}...`);
      const ok = await translateFile(mdFiles[i]);
      if (ok) successCount++;
      await delay(4500); // 4.5 seconds per request
  }
  console.log(`Translation complete! Successfully processed ${successCount} out of ${mdFiles.length} files.`);
}

main();
