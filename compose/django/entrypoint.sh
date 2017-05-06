#!/bin/bash
set -e
cmd="$@"

# This entrypoint is used to play nicely with the current cookiecutter configuration.
# Since docker-compose relies heavily on environment variables itself for configuration, we'd have to define multiple
# environment variables just to support cookiecutter out of the box. That makes no sense, so this little entrypoint
# does all this for us.
export REDIS_URL=redis://redis:6379










function mysql_ready(){
python << END
import sys
import pymysql.cursors

try:
	cnx = pymysql.connector.connect(user='$MYSQL_USER', password='$MYSQL_PASSWORD',
                              host='mysql',
                              db='$MYSQL_DATABASE', cursorclass=pymysql.cursors.DictCursor)
    
except:
    sys.exit(-1)
sys.exit(0)
END
}


until mysql_ready; do
  >&2 echo "Mysql is unavailable - sleeping"
  sleep 1
done

>&2 echo "Mysql is up - continuing..."
exec $cmd



