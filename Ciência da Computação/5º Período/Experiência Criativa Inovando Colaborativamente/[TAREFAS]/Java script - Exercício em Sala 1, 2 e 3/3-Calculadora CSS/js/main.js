function add(num1_input, num2_input, result_input) {
    var num1 = parseFloat(document.getElementById(num1_input).value);
    var num2 = parseFloat(document.getElementById(num2_input).value);
    var result = num1 + num2;
    document.getElementById(result_input).value = result;
}

function subtract(num1_input, num2_input, result_input) {
    var num1 = parseFloat(document.getElementById(num1_input).value);
    var num2 = parseFloat(document.getElementById(num2_input).value);
    var result = num1 - num2;
    document.getElementById(result_input).value = result;
}

function multiply(num1_input, num2_input, result_input) {
    var num1 = parseFloat(document.getElementById(num1_input).value);
    var num2 = parseFloat(document.getElementById(num2_input).value);
    var result = num1 * num2;
    document.getElementById(result_input).value = result;
}

function divide(num1_input, num2_input, result_input) {
    var num1 = parseFloat(document.getElementById(num1_input).value);
    var num2 = parseFloat(document.getElementById(num2_input).value);
    if (num2 !== 0) {
        var result = num1 / num2;
        document.getElementById(result_input).value = result;
    } else {
        document.getElementById(result_input).value = "Indefinido";
    }
}

function clearInput(input1, input2, inputResult) {
    document.getElementById(input1).value = "";
    document.getElementById(input2).value = "";
    document.getElementById(inputResult).value = "";
}
