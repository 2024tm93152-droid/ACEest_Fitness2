import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ACEest_Fitness import create_app

def test_home_route():
    app = create_app()
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert response.json['service'] == 'ACEest Fitness'

def test_members_route():
    app = create_app()
    client = app.test_client()
    response = client.get('/members')
    assert response.status_code == 200
    assert 'members' in response.json
