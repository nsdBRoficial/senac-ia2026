/**
 * Pixel Agents Bridge Daemon
 * Emite periodicamente eventos de agentes trabalhando para manter o escritório 8-bit com agentes ativos
 */

const http = require('http');
const fs = require('fs');
const path = require('path');
const os = require('os');

const SERVERS_DIR = path.join(os.homedir(), '.pixel-agents', 'servers');

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

function sendEvent(server, event) {
  const payload = JSON.stringify(event);
  const req = http.request({
    hostname: '127.0.0.1',
    port: server.port,
    path: '/api/hooks/claude',
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Content-Length': Buffer.byteLength(payload),
      'Authorization': `Bearer ${server.token}`
    },
    timeout: 3000
  }, (res) => {
    res.resume();
  });
  req.on('error', () => {});
  req.write(payload);
  req.end();
}

function broadcast(event) {
  const servers = getServers();
  for (const s of servers) {
    sendEvent(s, event);
  }
}

const agents = [
  { id: 'agent-dev-crud', name: 'Dev Antigravity', task: 'Writing crud.py' },
  { id: 'agent-reviewer', name: 'Code Reviewer', task: 'Validating logic' }
];

console.log('[Bridge] Starting agents in Pixel Office...');

// Inicializa os agentes
for (const a of agents) {
  broadcast({
    hook_event_name: 'SessionStart',
    session_id: a.id,
    cwd: process.cwd()
  });
}

const tools = ['WriteFile', 'ReadFile', 'Bash', 'Grep'];
let step = 0;

setInterval(() => {
  const a = agents[step % agents.length];
  const tool = tools[step % tools.length];
  step++;

  broadcast({
    hook_event_name: 'PreToolUse',
    session_id: a.id,
    tool_name: tool,
    tool_input: { path: 'crud.py', command: 'python crud.py' }
  });
}, 3000);
