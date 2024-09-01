function add(num1_input, num2_input) {
    var num1 = parseFloat(document.getElementById(num1_input).value);
    var num2 = parseFloat(document.getElementById(num2_input).value);
    var result = num1 + num2;
    alert('Resultado: ' + result);
}

function subtract(num1_input, num2_input) {
    var num1 = parseFloat(document.getElementById(num1_input).value);
    var num2 = parseFloat(document.getElementById(num2_input).value);
    var result = num1 - num2;
    alert('Resultado: ' + result);
}

function multiply(num1_input, num2_input) {
    var num1 = parseFloat(document.getElementById(num1_input).value);
    var num2 = parseFloat(document.getElementById(num2_input).value);
    var result = num1 * num2;
    alert('Resultado: ' + result);
}

function divide(num1_input, num2_input) {
    var num1 = parseFloat(document.getElementById(num1_input).value);
    var num2 = parseFloat(document.getElementById(num2_input).value);
    if (num2 !== 0) {
        var result = num1 / num2;
        alert('Resultado: ' + result);
    } else {
        alert('Divisor não pode ser nulo.');
    }
}
