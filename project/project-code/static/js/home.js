$("#file-picker").change(function(){
    var input = document.getElementById('file-picker');
    for (var i=0; i<input.files.length; i++)
    {
    //koala.jpg, koala.JPG substring(index) lastIndexOf('a') koala.1.jpg
        var ext= input.files[i].name.substring(input.files[i].name.lastIndexOf('.')+1).toLowerCase()
        if ((ext == 'txt'))
        {
            $("#msg").text("File is supported")
        }
        else
        {
            $("#msg").text("File is NOT supported")
            document.getElementById("file-picker").value ="";
        }
    }
} );