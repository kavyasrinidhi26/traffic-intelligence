"""Launch the complete AI Traffic Intelligence Platform locally."""

import uvicorn

if __name__ == "__main__":
    print("\n=======================================================")
    print("STARTING AI TRAFFIC INTELLIGENCE & DIGITAL TWIN")
    print("=======================================================")
    print("Web Command Center Dashboard: http://127.0.0.1:8000")
    print("REST API & Interactive Docs:  http://127.0.0.1:8000/docs")
    print("Press Ctrl+C to stop the server.")
    print("=======================================================\n")
    uvicorn.run("digital_twin.api:create_app", factory=True, host="127.0.0.1", port=8000, reload=False)
