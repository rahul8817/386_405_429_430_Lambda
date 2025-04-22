import requests

BASE_URL = "http://localhost:8000"

def upload_function(name, language, timeout, code):
    payload = {
        "name": name,
        "language": language,
        "timeout": timeout,
        "code": code
    }
    res = requests.post(f"{BASE_URL}/functions/", json=payload)
    return res.json()

def get_functions():
    res = requests.get(f"{BASE_URL}/functions/")
    return res.json()

def run_function(function_id, use_gvisor=False):
    data = {"use_gvisor": str(use_gvisor).lower()}
    try:
        res = requests.post(f"{BASE_URL}/functions/{function_id}/run", json=data)
        print("Request sent to:", f"{BASE_URL}/functions/{function_id}/run")
        print("Status Code:", res.status_code)
        print("Response Text:", res.text)
        return res.json()
    except requests.exceptions.JSONDecodeError:
        print("❌ Failed to parse JSON response.")
        print("⚠️ Full response text:")
        print(res.text)
        return {"error": "Invalid JSON response from server"}
    except Exception as e:
        print("💥 Other exception:", e)
        return {"error": str(e)}



def delete_function(function_id):
    res = requests.delete(f"{BASE_URL}/functions/{function_id}")
    return res.json()

def get_logs(function_id):
    res = requests.get(f"{BASE_URL}/functions/{function_id}/logs")
    return res.json()

def get_metrics(function_id):
    res = requests.get(f"{BASE_URL}/functions/{function_id}/metrics")
    return res.json()

def get_code(function_id):
    res = requests.get(f"{BASE_URL}/functions/{function_id}/code")
    return res.json()

def update_code(function_id, new_code):
    print(f"Updating Function {function_id} with code: {new_code[:100]}")
    res = requests.put(f"{BASE_URL}/functions/{function_id}", json={"code": new_code})
    return res.json()
