async function load(){let r=await fetch('/api/info');let j=await r.json();window.ip=j.ip;upd();}
function upd(){document.getElementById('url').innerText='http://'+window.ip+':'+document.getElementById('port').value;}
document.addEventListener('input',upd);
async function startSrv(){await fetch('/api/start',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({folder:folder.value,port:port.value})});}
async function stopSrv(){await fetch('/api/stop',{method:'POST'});}
load();