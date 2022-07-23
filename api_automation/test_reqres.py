import requests
import json

class TestCases_ReqRes(object):
    def test_get_request(self):
        response=requests.get("https://reqres.in/api/users?page=2")
        print(dir(response))
        assert response.status_code==200, "status code should be {}".format(response.status_code)
        print(response.elapsed)
        print(response.headers)
        print("Date and Time",response.headers['Date'])
        print("Server Info-->", response.headers['server'])
        #fetch cookies
        print(response.cookies)
        print(response.elapsed)# elasped time is taken by sending request and getting response

    def test_post_example(self):
        session = requests.Session()
        request_users={
            "name": "Mounika",
            "age": 25
        }
        response=session.post('https://reqres.in/api/users', json=request_users)
        print(response.headers['Content-Length'])
        print("response---->", dir(response.content))
        print(session)
        id = json.loads(response.text)['id']
        print("id--->", id)
        response=session.get('https://reqres.in/api/users/{id}'.format(id=id))
        print("response after the post the data----->", response)


    def test_put_example(self):
        updated_data={
            "name": "Mounika",
            "age": 25
        }
        session = requests.Session()
        response = session.put('https://reqres.in/api/users/2', data=updated_data)
        print(response)
        print(dir(response))
        res = requests.post('https://jsonplaceholder.typicode.com/users', data=
        {'id': '9', 'username': 'Mounika'})
        print(res)
        res = requests.get('https://jsonplaceholder.typicode.com/users/9')
        print(res)
        res = requests.put('https://jsonplaceholder.typicode.com/users/9', data=
        {'id': '11', 'username': 'Mounika'})
        print(res)
        res=requests.get('https://jsonplaceholder.typicode.com/users/9')
        print(res.content)

