import os
import django
from django.db.models import Sum, Q, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import Product, Category, Customer, Order, OrderProduct


# Create and run queries
def product_quantity_ordered():
    all_orders = (Product.objects.
                  annotate(sum_products=Sum("orderproduct__quantity")).
                  exclude(sum_products=None).
                  order_by("-sum_products")
                  )

    result = []
    for product in all_orders:
        result.append(f"Quantity ordered of {product.name}: {product.sum_products}")

    return "\n".join(result)


def ordered_products_per_customer():
    customer_orders = ((Order.objects.
                        prefetch_related("orderproduct_set__product__category")).
                       order_by("id").
                       all())

    result = []
    for order in customer_orders:
        result.append(f"Order ID: {order.id}, Customer: {order.customer.username}")

        for order_product in order.orderproduct_set.all():
            result.append(f"- Product: {order_product.product.name}, Category: {order_product.product.category.name}")

    return "\n".join(result)


def filter_products():
    query = Q(is_available=True) & Q(price__gt=3.00)

    filtered_products = Product.objects.filter(query).order_by("-price", "name").all()

    result =[]
    for product in filtered_products:
        result.append(f"{product.name}: {product.price}lv.")

    return "\n".join(result)


def give_discount():
    query = Q(is_available=True) & Q(price__gt=3.00)
    Product.objects.filter(query).update(price=(F("price") * 0.7))

    result = []

    for product in Product.objects.filter(is_available=True).order_by("-price", "name"):
        result.append(f"{product.name}: {product.price}lv.")

    return "\n".join(result)
