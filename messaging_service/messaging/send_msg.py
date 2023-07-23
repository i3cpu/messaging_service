import requests

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjEzMTYyMjYsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6Imh0dHBzOi8vdC5tZS9pM2NwdSJ9.GGMfF-hHKuZorwUkWcfZea8b0X9o9C0MMFKaPvYL_O8' 
}

def url(id):
    url = f'https://probe.fbrq.cloud/v1/send/{id}'
    return url


def send(id, phone, text):
    try:
        data = {
            "id": id,
            "phone": phone,  
            "text": text
        }
        response = requests.post(url=url(id), headers=headers, json=data)
        return response.status_code
    except requests.Timeout:
        return "Error: Timeout"
    except requests.ConnectionError:
        return "Error: Connecting to server"
    except requests.RequestException as e:
        return f"Error: Sending request {e}"
    except Exception as e:
        return f"Error: unknown {e}"

# print(send(id=1, phone='996670578', text='test'))