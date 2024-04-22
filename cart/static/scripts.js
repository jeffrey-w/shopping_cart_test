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
        setInnerText('cart-subtotal', json.payload.subtotal);
        setInnerText('cart-tax', json.payload.tax);
        setInnerText('cart-total', json.payload.total);
    } else {
        console.log(json.error);
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
