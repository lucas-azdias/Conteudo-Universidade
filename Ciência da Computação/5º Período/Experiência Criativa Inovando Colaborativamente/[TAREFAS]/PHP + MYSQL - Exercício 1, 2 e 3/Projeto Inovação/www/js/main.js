function goTo(url) {
    window.location.href = url;
}

async function login(formId) {
    const response = await sendData(formId, '../php/verify_login.php');

    if (response) {
        alert("Logado com sucesso.");
        goTo("../home");
    } else {
        alert("Falha na login.");
    }
}

async function register(formId) {
    if (document.getElementById("senha").value == document.getElementById("confirmarSenha").value) {
        const response = await sendData(formId, '../php/register_user.php');

        if (response) {
            alert("Cadastrado com sucesso.");
            goTo("../login");
        } else {
            alert("Falha no cadastro.");
        }
    } else {
        alert("Senhas não estão iguais.")
    }
}

async function sendData(formId, end_url) {
    try {
        const formData = new FormData(document.getElementById(formId));

        const response = await fetch(end_url, {
            method: "POST",
            body: formData
        })

        if (!response.ok) {
            throw new Error("Form not sent.");
        } else {
            return await response.json();
        }
    } catch (error) {
        console.log("Something went wrong. " + error);
    }
}
