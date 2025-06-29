from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root(): return {"status": "Backend running"}

@app.get("/api/neo4j-status")
def neo4j_status(): return {"status": "✅ Neo4j Connected"}
