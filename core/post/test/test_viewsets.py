import json

from rest_framework import status



class TestPostViewSet:
    endpoint="/api/post/"

    def _auth_client(self, client, user):
        response = client.post(
            "/api/auth/login/",
            data=json.dumps(
                {
                    "email": user.email,
                    "password": "test_password",
                }
            ),
            content_type="application/json",
        )
        assert response.status_code == status.HTTP_200_OK
        token = response.json()["access"]
        client.defaults["HTTP_AUTHORIZATION"] = f"Bearer {token}"
        return client
    
    def test_list(self,client,user,post):
        client = self._auth_client(client, user)
        response=client.get(self.endpoint)
        assert response.status_code==status.HTTP_200_OK
        assert response.data['count']==1
    
    def test_create(self,client,user):
        client = self._auth_client(client, user)
        data={
            "body":"Test post body",
            "author":str(user.public_id)
        
        }
        response=client.post(self.endpoint,data)
        assert response.status_code==status.HTTP_201_CREATED
        assert response.data['body']==data['body']
        assert response.data['author']['id']==user.public_id.hex
        
    def test_update(self,client,user,post):
        client = self._auth_client(client, user)
        data={
            "body":"Test post body",
            "author":str(user.public_id)
        }
        response =client.put(
            self.endpoint+str(post.public_id)+"/",
            data=json.dumps(data),
            content_type="application/json",
        )
        assert response.status_code==status.HTTP_200_OK
        assert response.data['body']==data['body']
        
    def test_delete(self,client,user,post):
        client = self._auth_client(client, user)
        response=client.delete(self.endpoint+str(post.public_id)+"/")
        assert response.status_code==status.HTTP_204_NO_CONTENT
    
    
    def test_list_anonymous(self,client,post):
        response=client.get(self.endpoint)
        assert response.status_code==status.HTTP_401_UNAUTHORIZED
    
    def test_retrieve(self,client,post):
        response=client.get(self.endpoint+str(post.public_id)+"/")
        assert response.status_code==status.HTTP_401_UNAUTHORIZED
        
    
    
    def test_create_anonnymous(self,client):
        data={
            "body":"Test post body",
            "author":"test_user"
        }
        
        response=client.post(self.endpoint,data)
        assert response.status_code==status.HTTP_401_UNAUTHORIZED
    
    def test_delete_anonymous(self,client,post):
        response=client.delete(self.endpoint+str(post.public_id)+"/")
        assert response.status_code==status.HTTP_401_UNAUTHORIZED
