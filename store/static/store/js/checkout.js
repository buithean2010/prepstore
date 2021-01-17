$(document).ready(function () {
    $('.shipping_addr').each(function () {
        if ($(this).data("shipping") == $("#shippingSelect").val()) {
            $(this).show();
        }
    });
});
function updateOrderAddress() {
    $('.shipping_addr').each(function () {
        if ($(this).data("shipping") == $("#shippingSelect").val()) {
            $(this).show();
        } else {
            $(this).hide();
        }
    });
}