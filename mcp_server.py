import sys
import json
from client import TreeOfThoughtsReasoner

tot = TreeOfThoughtsReasoner(beam_width=2, max_depth=3)

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "tree_of_thoughts_search",
                        "description": "Execute Tree of Thoughts beam search exploration given initial state and branches",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "root": {"type": "string"},
                                "depth": {"type": "integer", "default": 2}
                            },
                            "required": ["root"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "tree_of_thoughts_search":
            r = args["root"]
            d = args.get("depth", 2)
            searcher = TreeOfThoughtsReasoner(beam_width=2, max_depth=d)
            def expand_fn(s, lvl):
                return [f"{s}::branch_1", f"{s}::branch_2"]
            def eval_fn(s):
                return float(len(s))
            best, sc = searcher.search(r, expand_fn, eval_fn)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps({"best_trajectory": best, "score": sc})}]}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        if line.strip():
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
