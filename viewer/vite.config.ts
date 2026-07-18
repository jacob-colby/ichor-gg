import { defineConfig, type Plugin } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'
import { spawn } from 'node:child_process'
import { fileURLToPath } from 'node:url'

// Local-only write endpoint: shells the Python save_build CLI (fixed argv, body
// piped via stdin — no shell interpolation), then rebuilds index.json. Dev
// server only; a production build is read-only.
function saveBuildApi(): Plugin {
  const toolsDir = fileURLToPath(new URL('../tools', import.meta.url))
  const run = (mod: string, input: string | null) =>
    new Promise<void>((resolve, reject) => {
      const p = spawn('python', ['-m', mod], { cwd: toolsDir })
      let err = ''
      p.stderr.on('data', (d) => (err += d))
      if (input !== null) {
        p.stdin.write(input)
        p.stdin.end()
      }
      p.on('close', (code) =>
        code === 0 ? resolve() : reject(new Error(err || `${mod} exit ${code}`)),
      )
    })
  return {
    name: 'save-build-api',
    configureServer(server) {
      server.middlewares.use('/api/build', (req, res) => {
        if (req.method !== 'POST') {
          res.statusCode = 405
          res.end()
          return
        }
        let body = ''
        req.on('data', (c) => (body += c))
        req.on('end', () => {
          run('smite.save_build', body)
            .then(() => run('smite.build_index', null))
            .then(() => {
              res.setHeader('Content-Type', 'application/json')
              res.end(JSON.stringify({ ok: true }))
            })
            .catch((e) => {
              res.statusCode = 500
              res.setHeader('Content-Type', 'application/json')
              res.end(JSON.stringify({ ok: false, error: String(e) }))
            })
        })
      })
    },
  }
}

// https://vite.dev/config/
export default defineConfig({
  plugins: [react(), tailwindcss(), saveBuildApi()],
})
