

from flask import Flask, request, jsonify
import os, jwt, datetime
from dotenv import load_dotenv
import os

load_dotenv()

SECRET = os.environ.get("JWT_SECRET", "change_me_fallback_secret")



app = Flask(__name__)


users=[{"id":1,"email":"admin@example.com","password":"admin123","role":"admin"},
       {"id":2,"email":"user@example.com", "password":"user123", "role":"user"}]


def require_auth(f):
    def wrap(*a, **kw):
        auth = request.headers.get("Authorization", "")
        if not auth.startswith("Bearer "): return jsonify({"error": "Missing token"}), 401

        token_received = auth[7:]

        print(f"--- ПРИЙНЯТИЙ ТОКЕН: {token_received[:30]}... ---")

        try:
            request.user = jwt.decode(token_received, SECRET,
                                      algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            print("--- ПОМИЛКА: Токен прострочений! ---")
            return jsonify({"error": "Expired token"}), 401
        except Exception as e:
            print(f"--- ПОМИЛКА ДЕКОДУВАННЯ: {e} ---")
            return jsonify({"error": "Invalid or expired token"}), 401
        return f(*a, **kw)

    wrap.__name__ = f.__name__;
    return wrap


def check_role(roles):
    def deco(f):
        def wrap(*a,**kw):
            if request.user.get("role") not in roles: return jsonify({"error":"Forbidden"}),403
            return f(*a,**kw)
        wrap.__name__=f.__name__; return wrap
    return deco


@app.post("/login")
def login():
    b = request.get_json() or {}
    u = next((x for x in users if x["email"] == b.get("email") and x["password"] == b.get("password")), None)
    if not u: return jsonify({"error": "Invalid credentials"}), 401

    exp = datetime.datetime.utcnow() + datetime.timedelta(minutes=15)


    token = jwt.encode({
        "sub": str(u["id"]),
        "role": u["role"],
        "exp": exp
    }, SECRET, algorithm="HS256")

    return {"access_token": token, "token_type": "Bearer", "expires_in": 900}
@app.get("/profile")
@require_auth
def profile():

    return {"user_id":request.user["sub"],"role":request.user["role"]}

@app.delete("/users/<int:id>")
@require_auth
@check_role(["admin"])
def delete_user(id):
    return {"message":f"User {id} deleted (demo)"}

if __name__=="__main__": app.run(port=3000, debug=True)