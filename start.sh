
if [ ! -s "/var/lib/postgresql/data/PG_VERSION" ]; then
  mkdir -p /var/lib/postgresql/data
  chown postgres:postgres /var/lib/postgresql/data
  su - postgres -c "initdb -D /var/lib/postgresql/data"
  su - postgres -c "pg_ctl -D /var/lib/postgresql/data -l /var/log/postgresql.log start"
  su - postgres -c "psql -c \"CREATE DATABASE filemanager;\""
  su - postgres -c "psql -c \"ALTER USER postgres WITH PASSWORD 'your_secure_password';\""
else
  su - postgres -c "pg_ctl -D /var/lib/postgresql/data -l /var/log/postgresql.log start"
fi

# Start FastAPI backend in the background
uvicorn main:app --host 0.0.0.0 --port 8000 &

# Start Nginx in the foreground
nginx -g "daemon off;"