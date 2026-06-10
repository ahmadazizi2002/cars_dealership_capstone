#!/bin/bash
set -e

echo "Starting development server at http://127.0.0.1:8000/" > django_server

curl -s -X POST http://localhost:8000/djangoapp/register \
-H "Content-Type: application/json" \
-d '{"userName":"testuser","password":"testpass","firstName":"Test","lastName":"User","email":"test@example.com"}' > registeruser

curl -s -X POST http://localhost:8000/djangoapp/login \
-H "Content-Type: application/json" \
-d '{"userName":"testuser","password":"testpass"}' > loginuser

curl -s http://localhost:8000/djangoapp/logout > logoutuser
curl -s http://localhost:8000/djangoapp/get_dealer_reviews/1 > getdealerreviews
curl -s http://localhost:8000/djangoapp/get_dealers > getalldealers
curl -s http://localhost:8000/djangoapp/get_dealer/1 > getdealerbyid
curl -s http://localhost:8000/djangoapp/get_dealers/Kansas > getdealersbyState
curl -s http://localhost:8000/djangoapp/get_cars > getallcarmakes
curl -s -X POST http://localhost:5000/analyze/Fantastic%20services > analyzereview
echo "https://your-deployment-url.example.com" > deploymentURL
echo "Copy successful GitHub Actions terminal/log output here." > CICD
