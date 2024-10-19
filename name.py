from flask import Flask
import os
import time

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Saniya Thomas" 
    username = os.getenv('USER') or os.getenv('USERNAME') or 'Unknown User'
    ist_time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time() + 5.5 * 3600))
    top_output = """
    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
    1 root      20   0  225412   7052   4004 S   0.0   0.4   0:01.02 systemd
    2 root      20   0   10240   1888   1576 S   0.0   0.1   0:00.01 kthreadd
    3 root      20   0   10240      0      0 S   0.0   0.0   0:00.00 rcu_gp
    """

    return f"""
    <h1>Name: {name}</h1>
    <h2>User: {username}</h2>
    <h2>Server Time (IST): {ist_time}</h2>
    <h3>TOP output:</h3>
    <pre>{top_output}</pre>
    """
if __name__ == '__main__':
    app.run(debug=True) 