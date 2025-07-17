from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """Modelo de usuario personalizado con soporte para membresías educativas"""
    MEMBERSHIP_CHOICES = [
        ('regular', 'Usuario regular'),
        ('teacher', 'Docente'),
        ('institution', 'Institución educativa'),
    ]
    
    membership_type = models.CharField(
        max_length=20,
        choices=MEMBERSHIP_CHOICES,
        default='regular'
    )
    is_verified = models.BooleanField(default=False)
    verification_document = models.FileField(
        upload_to='verification_docs/',
        null=True,
        blank=True
    )
    institutional_email = models.EmailField(null=True, blank=True)
    
    def is_educational_member(self):
        return self.membership_type in ['teacher', 'institution']

class Product(models.Model):
    """Modelo para productos/juguetes didácticos"""
    MATERIAL_CHOICES = [
        ('madera', 'Madera'),
        ('plastico', 'Plástico'),
        ('tela', 'Tela'),
        ('metal', 'Metal'),
        ('mixto', 'Material mixto'),
    ]
    
    LEARNING_TYPE_CHOICES = [
        ('motricidad', 'Motricidad'),
        ('cognitivo', 'Desarrollo cognitivo'),
        ('social', 'Habilidades sociales'),
        ('emocional', 'Inteligencia emocional'),
        ('linguistico', 'Lenguaje'),
    ]
    
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    material = models.CharField(max_length=50, choices=MATERIAL_CHOICES)
    recommended_age = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    learning_type = models.CharField(
        max_length=50,
        choices=LEARNING_TYPE_CHOICES,
        null=True,
        blank=True
    )
    discount_for_members = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
        help_text="Porcentaje de descuento para miembros educativos"
    )
    
    def average_rating(self):
        from django.db.models import Avg
        return self.reviews.aggregate(Avg('rating'))['rating__avg'] or 0
    
    def _str_(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at']

class ProductImage(models.Model):
    """Imágenes asociadas a productos"""
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(upload_to='products/')
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']

class Review(models.Model):
    """Reseñas y calificaciones de productos por usuarios"""
    RATING_CHOICES = [
        (1, '1 - Muy malo'),
        (2, '2 - Malo'),
        (3, '3 - Regular'),
        (4, '4 - Bueno'),
        (5, '5 - Excelente'),
    ]
    
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('product', 'user')
        ordering = ['-created_at']

class Cart(models.Model):
    """Carrito de compras de usuario"""
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='cart'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    @property
    def total(self):
        return sum(item.subtotal for item in self.items.all())
    
    @property
    def total_items(self):
        return sum(item.quantity for item in self.items.all())

class CartItem(models.Model):
    """Items individuales en el carrito de compras"""
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='items'
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    @property
    def subtotal(self):
        if self.cart.user.is_educational_member():
            discount = self.product.discount_for_members / 100
            discounted_price = self.product.price * (1 - discount)
            return discounted_price * self.quantity
        return self.product.price * self.quantity

class Order(models.Model):
    """Órdenes de compra completadas"""
    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('processing', 'Procesando'),
        ('completed', 'Completada'),
        ('cancelled', 'Cancelada'),
    ]
    
    PAYMENT_METHOD_CHOICES = [
        ('credit_card', 'Tarjeta de crédito'),
        ('debit_card', 'Tarjeta de débito'),
        ('paypal', 'PayPal'),
        ('bank_transfer', 'Transferencia bancaria'),
    ]
    
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        related_name='orders'
    )
    order_number = models.CharField(max_length=20, unique=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHOD_CHOICES
    )
    shipping_address = models.TextField()
    billing_address = models.TextField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    email_sent = models.BooleanField(default=False)
    
    def _str_(self):
        return self.order_number

class OrderItem(models.Model):
    """Items individuales en una orden de compra"""
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
    )
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    @property
    def subtotal(self):
        return self.price * self.quantity

class ContactMessage(models.Model):
    """Mensajes del formulario de contacto"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_answered = models.BooleanField(default=False)
    
    def _str_(self):
        return f"Mensaje de {self.name}"

class BlogCategory(models.Model):
    """Categorías para artículos del blog"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    
    def _str_(self):
        return self.name

class BlogPost(models.Model):
    """Artículos del blog educativo"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True
    )
    categories = models.ManyToManyField(BlogCategory)
    content = models.TextField()
    featured_image = models.ImageField(
        upload_to='blog/',
        null=True,
        blank=True
    )
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)
    
    def _str_(self):
        return self.title
    
    class Meta:
        ordering = ['-published_at']