import { readdir, stat } from 'node:fs/promises';

const ISU = '563212';

let files = 0;
let directories = 0;
let size = 0;

async function analyzeDirectory(path) {
    const entries = await readdir(path);

    for (const entry of entries) {
        const fullPath = `${path}/${entry}`;
        const info = await stat(fullPath);

        if (info.isFile()) {
            files++;
            size += info.size;
        } else if (info.isDirectory()) {
            directories++;
            await analyzeDirectory(fullPath);
        }
    }
}

await analyzeDirectory('/data');

console.log(`${ISU}-${files}-${directories}-${size}`);