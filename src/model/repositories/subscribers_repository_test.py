import pytest

from .subscribers_repository import SubscribersRepository

@pytest.mark.skip("Insert in DB")
def test_insert_eventos():
  subscriber_info = {
    "name": "meuNome222",
    "email": "teste22@gmail.com",
    "evento_id": 2
  }
  
  subs_repo = SubscribersRepository()
  subs_repo.insert(subscriber_info)
  
def test_select_subscriber():
  email = "teste@gmail.com"
  evento_id = 2
  
  subs_repo = SubscribersRepository()
  resp = subs_repo.select_subscriber(email, evento_id)
  
  print(resp.nome)