# What’s a socket?

A socket is like a phone line between two programs.  
- One side is the **server** (waiting for calls).  
- The other side is the **client** (making calls).  

On the web, that line is defined by:  
- an **IP address** (the house number),  
- and a **port** (the room number).  

Example: `127.0.0.1:8000` = “call my own computer on port 8000.”

With a socket, your program can **listen** for a call (like from Postman or a browser) and then **send back** a reply.

---

## Why bother if frameworks exist?

Frameworks (like Flask or FastAPI) hide the details.  
But under the hood, they still use sockets to open a port and handle requests.  
The Python standard library has two ways to do this:  
- `socket` → super low-level, you deal with raw data.  
- `http.server` → already knows the basics of HTTP, easier to start with.

---

## Think of it like this

- **Socket** = the raw phone line.  
- **http.server** = a simple answering machine.  
- **Flask/FastAPI** = a personal assistant who answers the phone, logs the call, and makes you coffee.  
