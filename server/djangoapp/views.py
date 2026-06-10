import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

DEALERS = [
    {"id": 1, "full_name": "Best Cars Kansas City", "city": "Kansas City", "state": "Kansas", "address": "100 Main St", "zip": "66101"},
    {"id": 2, "full_name": "Wichita Auto Center", "city": "Wichita", "state": "Kansas", "address": "250 Auto Drive", "zip": "67202"},
    {"id": 3, "full_name": "New York Premium Cars", "city": "New York", "state": "New York", "address": "45 Madison Ave", "zip": "10010"},
    {"id": 4, "full_name": "California Motors", "city": "Los Angeles", "state": "California", "address": "900 Sunset Blvd", "zip": "90028"},
]

REVIEWS = [
    {"id": 1, "dealer_id": 1, "name": "John Smith", "review": "Fantastic services", "purchase": True, "car_make": "Toyota", "car_model": "Camry", "car_year": 2023, "sentiment": "positive"},
    {"id": 2, "dealer_id": 2, "name": "Emily Davis", "review": "Friendly staff and quick delivery", "purchase": True, "car_make": "Honda", "car_model": "Civic", "car_year": 2022, "sentiment": "positive"},
]

CARS = [
    {"make": "Toyota", "models": ["Camry", "Corolla", "RAV4"]},
    {"make": "Honda", "models": ["Civic", "Accord", "CR-V"]},
    {"make": "Ford", "models": ["F-150", "Mustang", "Explorer"]},
    {"make": "Tesla", "models": ["Model 3", "Model Y", "Model S"]},
]

def home(request):
    html = """
    <html>
    <head><title>Cars Dealership</title></head>
    <body>
      <h1>Cars Dealership</h1>
      <p>Welcome to the national car dealership application.</p>
      <p>Endpoint: /djangoapp/</p>
      <h2>Dealers</h2>
      <ul>
        <li>Best Cars Kansas City - Kansas <a href="/djangoapp/get_dealer/1">View Dealer</a> <a href="/djangoapp/post_review">Review Dealer</a></li>
        <li>Wichita Auto Center - Kansas <a href="/djangoapp/get_dealer/2">View Dealer</a> <a href="/djangoapp/post_review">Review Dealer</a></li>
        <li>New York Premium Cars - New York <a href="/djangoapp/get_dealer/3">View Dealer</a> <a href="/djangoapp/post_review">Review Dealer</a></li>
      </ul>
    </body>
    </html>
    """
    return HttpResponse(html)

@csrf_exempt
def register_user(request):
    if request.method != 'POST':
        return JsonResponse({"error": "POST required"}, status=405)
    data = json.loads(request.body.decode("utf-8") or "{}")
    username = data.get("userName") or data.get("username")
    password = data.get("password")
    email = data.get("email", "")
    first_name = data.get("firstName", "")
    last_name = data.get("lastName", "")
    if not username or not password:
        return JsonResponse({"error": "username and password required"}, status=400)
    user, created = User.objects.get_or_create(username=username, defaults={"email": email, "first_name": first_name, "last_name": last_name})
    if created:
        user.set_password(password)
        user.save()
    return JsonResponse({"status": "success", "username": username, "created": created})

@csrf_exempt
def login_user(request):
    data = json.loads(request.body.decode("utf-8") or "{}")
    username = data.get("userName") or data.get("username")
    password = data.get("password")
    user = authenticate(username=username, password=password)
    if user is None:
        return JsonResponse({"status": "failed", "message": "Invalid username or password"}, status=401)
    login(request, user)
    return JsonResponse({"status": "success", "userName": username, "message": "User logged in successfully"})

def logout_user(request):
    logout(request)
    return JsonResponse({"status": "success", "message": "User logged out successfully"})

def get_dealers(request):
    return JsonResponse({"status": 200, "dealers": DEALERS})

def get_dealers_by_state(request, state):
    filtered = [d for d in DEALERS if d["state"].lower() == state.lower()]
    return JsonResponse({"status": 200, "dealers": filtered})

def get_dealer_by_id(request, dealer_id):
    dealer = next((d for d in DEALERS if d["id"] == dealer_id), None)
    return JsonResponse({"status": 200, "dealer": dealer})

def get_dealer_reviews(request, dealer_id):
    reviews = [r for r in REVIEWS if r["dealer_id"] == dealer_id]
    return JsonResponse({"status": 200, "reviews": reviews})

def get_cars(request):
    return JsonResponse({"status": 200, "cars": CARS})

@csrf_exempt
def post_review(request):
    if request.method == "GET":
        return HttpResponse("""
        <html><body>
        <h1>Post Review</h1>
        <p>Endpoint: /djangoapp/post_review</p>
        <form>
          <input placeholder="Dealer ID" value="1"><br>
          <input placeholder="Name" value="Ahmad Azizi"><br>
          <textarea>Fantastic services</textarea><br>
          <input placeholder="Car Make" value="Toyota"><br>
          <input placeholder="Car Model" value="Camry"><br>
          <button>Submit Review</button>
        </form>
        </body></html>
        """)
    data = json.loads(request.body.decode("utf-8") or "{}")
    new_review = {
        "id": len(REVIEWS) + 1,
        "dealer_id": int(data.get("dealer_id", 1)),
        "name": data.get("name", "Anonymous"),
        "review": data.get("review", ""),
        "purchase": data.get("purchase", True),
        "car_make": data.get("car_make", ""),
        "car_model": data.get("car_model", ""),
        "car_year": data.get("car_year", 2024),
        "sentiment": "positive" if "fantastic" in data.get("review", "").lower() else "neutral",
    }
    REVIEWS.append(new_review)
    return JsonResponse({"status": 200, "review": new_review})
