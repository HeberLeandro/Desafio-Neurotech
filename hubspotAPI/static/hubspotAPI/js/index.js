var formContato = document.getElementById("formContato");

formContato.addEventListener("submit",function(e){
    e.preventDefault();
    var contato = {
        "email": document.getElementById("email").value,
        "phone": document.getElementById("phone").value,
        "date_of_birth": document.getElementById("date_of_birth").value,
        "peso": document.getElementById("peso").value
    }

    console.log(contato)
        
    var url = "http://localhost:8000/api/";
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var obj = JSON.parse(this.responseText);
            console.log(obj);
            alert('Contato Criando com Sucesso!')
            formContato.reset();
        }

        if (this.readyState == 4 && this.status == 201) {
            var obj = JSON.parse(this.responseText);
            console.log(obj);
            alert('Contato Atualizado com Sucesso!')
            formContato.reset();
        }
    
        else if (this.readyState == 4 && this.status == 401) {
            var obj = JSON.parse(this.responseText);
            alert('Sua Sessão Expirou.')
            console.log(obj);
            document.getElementById("signOut").click();
        }

        else if (this.readyState == 4 && this.status == 409) {
            var obj = JSON.parse(this.responseText);
            alert('Erro ao atualizar Contato.')
            console.log(obj);
            formContato.reset();
        }
    }

    xhttp.open("POST", url, true);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.send(JSON.stringify(contato));

})
