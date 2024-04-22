async function updateQuantity(e)
{
    const response = await fetch(
        e.target.dataset.href,
        { 
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCsrfMiddlewareToken(),
            },
            body: JSON.stringify({ quantity: e.target.value }),
        });
    const json = await response.json();
    if (json.success) {
        const error = document.getElementById(`cart-quantity-error-${e.target.dataset.itemId}`);
        error.style.display = 'none';
        setInnerText('cart-subtotal', json.payload.subtotal);
        setInnerText('cart-tax', json.payload.tax);
        setInnerText('cart-total', json.payload.total);
    } else {
        const error = document.getElementById(`cart-quantity-error-${e.target.dataset.itemId}`);
        error.innerText = json.error;
        error.style.display = 'block';
    }
}

function getCsrfMiddlewareToken()
{
    return document.getElementsByName('csrfmiddlewaretoken')[0].value;
}

function setInnerText(id, text)
{
    const element = document.getElementById(id);
    element.innerText = text;
}

window.onload = () => {
    for (const element of document.querySelectorAll('input[id^=cart-quantity]')) {
        element.addEventListener('change', updateQuantity);
    }
}
