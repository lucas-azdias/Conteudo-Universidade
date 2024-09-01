function compare(num1_input, num2_input, result_span) {
    num1 = parseFloat(document.getElementById(num1_input).value);
    num2 = parseFloat(document.getElementById(num2_input).value);
    if (num1 > num2) {
        document.getElementById(result_span).innerText = "Número 1";
    } else if (num1 < num2) {
        document.getElementById(result_span).innerText = "Número 2";
    } else {
        document.getElementById(result_span).innerText = "Iguais";
    }
}
