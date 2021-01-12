class OrderStatus:
    BEGINING = 0
    PROCESSING = 1
    SHIPPING = 2
    SHIPPED = 3
    COMPLETE = 4

    ORDER_STATUS_CHOICES = {
        BEGINING: '処理待ち',
        PROCESSING: '処理中',
        SHIPPING: '配達待ち',
        SHIPPED: '配達中',
        COMPLETE: '完了',
    }
