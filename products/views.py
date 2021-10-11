from django.shortcuts import render


# Create your views here.


def index(request):
    context = {
        'title': 'GeekShop',
        'header': 'GeekShop Store',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Каталог',
        'header': 'GeekShop',
        'product_categories': [
            'Новинки',
            'Одежда',
            'Обувь',
            'Аксессуары',
            'Подарки',
        ],
        'products': [
            {
                'name': 'Худи черного цвета с монограммами adidas Originals',
                'price': 6090,
                'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
                'image': 'vendor/img/products/Adidas-hoodie.png',
                'in_basket': False
            },
            {
                'name': 'Синяя куртка The North Face',
                'price': 23725,
                'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
                'image': 'vendor/img/products/Blue-jacket-The-North-Face.png',
                'in_basket': True
            },
            {
                'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                'price': 3390,
                'description': 'Материал с плюшевой текстурой. Удобный и мягкий.',
                'image': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
                'in_basket': False
            },
            {
                'name': 'Черный рюкзак Nike Heritage',
                'price': 2340,
                'description': 'Плотная ткань. Легкий материал.',
                'image': 'vendor/img/products/Black-Nike-Heritage-backpack.png',
                'in_basket': False
            },
            {
                'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
                'price': 13590,
                'description': 'Гладкий кожаный верх. Натуральный материал.',
                'image': 'vendor/img/products/Black-Dr-Martens-shoes.png',
                'in_basket': False
            },
            {
                'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
                'price': 2890,
                'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
                'image': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
                'in_basket': False
            },
        ],
    }
    return render(request, 'products/products.html', context)
