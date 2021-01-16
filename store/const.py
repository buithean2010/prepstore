class OrderStatus:
    SHOPPING = 0
    BEGINING = 1
    PROCESSING = 2
    SHIPPING = 3
    SHIPPED = 4
    COMPLETE = 5

    ORDER_STATUS_CHOICES = {
        SHOPPING: '買い物中',
        BEGINING: '処理待ち',
        PROCESSING: '処理中',
        SHIPPING: '配達待ち',
        SHIPPED: '配達中',
        COMPLETE: '完了',
    }
