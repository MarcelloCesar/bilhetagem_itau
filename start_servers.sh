#!/bin/bash

echo "Iniciando Webserver 1 na porta 80..."
(
  cd app && \
  nohup python -m uvicorn service_bilhetagem:app --host 0.0.0.0 --port 80 --reload > ../server_logs/service_bilhetagem.log 2>&1 &
)

echo "Iniciando Webserver 2 na porta 81..."
(
  cd app && \
  nohup python -m uvicorn web_server2:app --host 0.0.0.0 --port 81 --reload > ../server_logs/webserver2.log 2>&1 &
)


echo "Os logs de cada processo estão nos arquivos webserver1.log, webserver2.log e script_proc.log na raiz do seu projeto."
echo "Para verificar os processos, use: ps -W | grep python"
echo "Para parar os servidores Uvicorn, use: taskkill -f 'uvicorn'"
echo "Para parar os scripts Python, use: taskkill -f 'python' (cuidado!)"
echo "---"