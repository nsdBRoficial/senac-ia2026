/**
 * Pixel Agents Live Activity Simulator & Bridge
 * Simula ações contínuas de digitação, leitura de código e pensamento dos agentes
 * no Pixel Agents (tanto no VS Code quanto no navegador local).
 */

const http = require('http');
const fs = require('fs');
const path = require('path');
const os = require('os');

const SERVERS_DIR = path.join(os.homedir(), '.pixel-agents', 'servers');
const PROJECT_DIR = path.join(os.homedir(), '.claude', 'projects', 'C--Users-DouglasAlexandreGome-Documents-Github-senac-ia2026-senac-ia2026');
const CWD = 'C:\\Users\\DouglasAlexandreGome\\Documents\\Github\\senac-ia2026\\senac-ia2026';

fs.mkdirSync(PROJECT_DIR, { recursive: true });

function getServers() {
  if (!fs.existsSync(SERVERS_DIR)) return [];
  const files = fs.readdirSync(SERVERS_DIR).filter(f => f.endsWith('.json'));
  const servers = [];
  for (const f of files) {
    try {
      const data = JSON.parse(fs.readFileSync(path.join(SERVERS_DIR, f), 'utf-8'));
      if (data.port && data.token) servers.push(data);
    } catch (e) {}
  }
  return servers;
}

function sendToAll(data) {
  const payload = JSON.stringify(data);
  const servers = getServers();
  for (const s of servers) {
    const req = http.request({
      hostname: '127.0.0.1',
      port: s.port,
      path: '/api/hooks/claude',
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(payload),
        'Authorization': `Bearer ${s.token}`
      },
      timeout: 2000
    }, res => res.resume());
    req.on('error', () => {});
    req.write(payload);
    req.end();
  }
}

const agents = [
  { id: 'agent-1', name: 'Douglas (Antigravity Senior Dev)' },
  { id: 'agent-2', name: 'QA & Reviewer Agent' }
];

// Inicializa os arquivos de sessão JSONL
agents.forEach(a => {
  const p = path.join(PROJECT_DIR, `${a.id}.jsonl`);
  if (!fs.existsSync(p)) {
    fs.writeFileSync(p, JSON.stringify({ type: 'user', message: { role: 'user', content: 'Iniciando desenvolvimento...' } }) + '\n');
  }
  sendToAll({
    hook_event_name: 'SessionStart',
    session_id: a.id,
    transcript_path: p,
    cwd: CWD
  });
});

const tools = [
  { tool: 'WriteFile', input: { path: 'crud.py' } },
  { tool: 'ReadFile', input: { path: 'aula1.py' } },
  { tool: 'Bash', input: { command: 'git status' } },
  { tool: 'WriteFile', input: { path: 'calculadora.py' } }
];

let cycle = 0;

setInterval(() => {
  const agent = agents[cycle % agents.length];
  const t = tools[cycle % tools.length];
  cycle++;

  // Inicia o uso da ferramenta (boneco senta e digita no computador)
  sendToAll({
    hook_event_name: 'PreToolUse',
    session_id: agent.id,
    tool_name: t.tool,
    tool_input: t.input
  });

  // Finaliza a ação após 2.5s
  setTimeout(() => {
    sendToAll({
      hook_event_name: 'PostToolUse',
      session_id: agent.id
    });
  }, 2500);

}, 4000);

console.log('[Pixel Agents Bridge] Rodando continuamente!');
