
# ⚠️ INTENTIONALLY VULNERABLE — for SAST demo only
import sqlite3

@app.route("/search")
def search():
    from flask import request
    query = request.args.get("q", "")
    # BAD: string formatting in SQL = SQL injection vulnerability
    # Semgrep/CodeQL SHOULD flag this
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    sql = "SELECT * FROM users WHERE name = '" + query + "'"
    cursor.execute(sql)   # ← SAST tools will flag this line
    results = cursor.fetchall()
    return jsonify({"results": results})
