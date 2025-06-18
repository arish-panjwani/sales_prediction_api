# Sales Prediction API

This API uses linear regression to predict sales based on temperature and promotions.

## How to run

## Example request
POST `/predict`
```json
{
  "temperature": 25.0,
  "promotions": 5.0
}
```

---

## **5️⃣ Create virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
# OR
venv\Scripts\activate     # Windows
