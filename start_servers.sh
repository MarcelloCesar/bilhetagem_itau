#!/bin/bash
export DB_BILHETAGEM_PATH=$(pwd)/app/service_bilhetagem/service_bilhetagem.db

echo "Iniciando service_bilhetagem na porta 80..."
(
  cd app/service_bilhetagem && \
  nohup python -m uvicorn service_bilhetagem:app --host 0.0.0.0 --port 80 --reload --log-level debug > ../../server_logs/service_bilhetagem.log 2>&1 &
)

echo "Os logs de cada processo estão nos arquivos webserver1.log, webserver2.log e script_proc.log na raiz do seu projeto."
echo "Para verificar os processos, use: ps -W | grep python"
echo "Para parar os servidores Uvicorn, use: taskkill -f 'uvicorn'"
echo "Para parar os scripts Python, use: taskkill -f 'python' (cuidado!)"
echo "---"