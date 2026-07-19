import { defineConfig, type Plugin } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'
import { spawn } from 'node:child_process'
import { fileURLToPath } from 'node:url'

// Owner-only, dev-server-only god management: shells `python -m smite.manage_gods
// <action> "<name>"` (fixed argv — no shell interpolation), which scrapes/moves
// notes and rebuilds index.json. Not present in a production build (friends host
// a static site; mine builds live in their browser via localStorage).
function manageGodsApi(): Plugin {
  const toolsDir = fileURLToPath(new URL('../tools', import.meta.url))
  return {
    name: 'manage-gods-api',
    configureServer(server) {
      server.middlewares.use('/api/gods', (req, res) => {
        if (req.method !== 'POST') {
          res.statusCode = 405
          res.end()
          return
        }
        let body = ''
        req.on('data', (c) => (body += c))
        req.on('end', () => {
          let payload: { action?: string; name?: string } = {}
          try {
            payload = JSON.parse(body)
          } catch {
            /* leave payload empty -> 400 below */
          }
          const action =
            payload.action === 'add' || payload.action === 'remove' ? payload.action : null
          const name = typeof payload.name === 'string' ? payload.name : ''
          if (!action || !name) {
            res.statusCode = 400
            res.setHeader('Content-Type', 'application/json')
            res.end(JSON.stringify({ ok: false, error: 'bad request' }))
            return
          }
          const p = spawn('python', ['-m', 'smite.manage_gods', action, name], { cwd: toolsDir })
          let err = ''
          p.stderr.on('data', (d) => (err += d))
          p.on('close', (code) => {
            res.setHeader('Content-Type', 'application/json')
            if (code === 0) {
              res.end(JSON.stringify({ ok: true }))
            } else {
              res.statusCode = 500
              res.end(JSON.stringify({ ok: false, error: err || `exit ${code}` }))
            }
          })
        })
      })
    },
  }
}

// https://vite.dev/config/
export default defineConfig({
  plugins: [react(), tailwindcss(), manageGodsApi()],
  // Adding/removing a god rewrites public/index.json + re-copies public/icons.
  // Left watched, Vite full-reloads the page and drops React state (the selected
  // god). Ignore public/ — the app refreshes data via its own fetch in reload().
  server: {
    watch: { ignored: ['**/public/index.json', '**/public/icons/**'] },
  },
})
