var control = document.getElementById("textupload");
    var send = document.getElementById("sendButton");
    control.addEventListener("change", myFunction, false);
    send.addEventListener("click", sendFunc);

    function myFunction()  
    {
        var i = 0,
        file = control.files;

            console.log("Filename: " + file[i].name);
            console.log("Type: " + file[i].type);
            console.log("Size: " + file[i].size + " bytes");
    }

    function sendFunc()
    {
        var files = control.files;
        if(files.length < 1)
        {
            document.getElementById("filename").innerHTML = "";
            document.getElementById("filetype").innerHTML = "";
            document.getElementById("filesize").innerHTML = "";
            alert("Please choose a file before sending");
            return;
        }
        var file = files[0],
            index = file.name.lastIndexOf('.'),
            extension = file.name.substring(index+1);

        if(extension != "txt")
        {
            
            document.getElementById("filename").innerHTML = "";
            document.getElementById("filetype").innerHTML = "";
            document.getElementById("filesize").innerHTML = "";
            alert("File must be a .txt file");
            return;
        }
            document.getElementById("filename").innerHTML = "Filename: " + file.name;
            document.getElementById("filetype").innerHTML = "Type: " + file.type;
            document.getElementById("filesize").innerHTML = "Size: " + file.size + " bytes";
            /*console.log("Filename: " + file[0].name);
            console.log("Type: " + file[0].type);
            console.log("Size: " + file[0].size + " bytes");*/
    }