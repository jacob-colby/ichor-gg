// Mirror data/_assets/icons -> viewer/public/icons.
//
// Icons are stored once, in data/. public/icons is generated and gitignored so
// the repo doesn't carry ~35MB of duplicated PNGs (and can't drift between the
// two copies). The Python pipeline does this same copy at index-build time, but
// the static host only runs `npm run build` — so this Node prebuild step keeps
// the deployed site's images working without needing Python on the build box.
import { cp, mkdir, readdir } from "node:fs/promises";
import { existsSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const src = join(here, "..", "..", "data", "_assets", "icons");
const dest = join(here, "..", "public", "icons");

if (!existsSync(src)) {
  // A viewer-only checkout (or a host that shallow-clones just this folder)
  // has no data/ — fail loudly rather than silently deploying without art.
  console.error(`copy-icons: source not found: ${src}`);
  process.exit(1);
}

await mkdir(dest, { recursive: true });
await cp(src, dest, { recursive: true });
const n = (await readdir(dest)).length;
console.log(`copy-icons: ${n} files -> public/icons`);
