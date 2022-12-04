

function getdata() {
    var query = document.getElementById("queryfield").value
    alert(query)

    let options = {
        scriptPath: "",
        args: [query]
    }

    const { PythonShell } = require('python-shell')


    PythonShell.run('\main.py', options, (err, res) => {
        if (res) {
            document.writeln('relevant code is: ' + res) 
        }
        if (err) {
            document.writeln('relevant code is: ' + err) 
        }
    });
}


