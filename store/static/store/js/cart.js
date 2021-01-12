function addCart(productId) {
    if (user == 'AnonymousUser') {
        addCookieItem(productId, action)
    } else {
        updateUserOrder(productId, action)
    }
}

$(document).ready(function () {

    $(".update-cart").on("click", function (event) {
        $(this).prop('disabled', true);
        var productId = $(this).attr("data-product");
        var action = $(this).attr("data-action");

        if (user == 'AnonymousUser') {
            // addCookieItem(productId, action)
        } else {
            updateUserOrder(productId, action)
        }
    });
});

function updateUserOrder(productId, action) {
    console.log('User is authenticated, sending data...')

    $.ajax({
        url: "/update_cart/",
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        type: "post",
        async: true,
        data: JSON.stringify({ 'productId': productId, 'action': action }),
        success: function (result, status, xhr) {
            location.reload();
        },
        error: function (xhr, status, error) {
            console.log(error)
        }
    });
}

