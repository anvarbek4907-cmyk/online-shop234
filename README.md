# Online Shop - Model qismi (Django)

## Ishga tushirish

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

python manage.py makemigrations shop
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Admin panel: http://127.0.0.1:8000/admin/

## Tuzilishi

```
onlineshop/
├── manage.py
├── requirements.txt
├── config/          # sozlamalar (settings, urls)
└── shop/
    ├── models.py    # Category, Product, ProductImage, Customer, Cart,
    │                # CartItem, Order, OrderItem, Payment, Review
    ├── admin.py     # admin panel sozlamalari
    └── signals.py   # User yaratilganda Customer va Cart avtomatik yaratiladi
```
